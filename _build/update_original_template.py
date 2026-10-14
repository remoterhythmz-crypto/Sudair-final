from __future__ import annotations

import json, re
from datetime import date
from pathlib import Path
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

R=Path(__file__).resolve().parent
SRC=R/'Sudair_3Month_Strategy_and_Image_Placeholders.pptx'
OUT=R/'Sudair_3Month_Strategy_First_Wave_Template_v2.pptx'
IMAGES=R/'Generated_Stills'/'First_Wave_Only'
cal=json.loads((R/'Sudair_3Month_Content_Calendar_v2.json').read_text(encoding='utf-8'))
byid={x['id']:x for x in cal}
p=Presentation(SRC)

def set_text(shape, value):
    if not shape.has_text_frame:return
    # Preserve paragraph/run styling when possible.
    for para in shape.text_frame.paragraphs:
        for run in para.runs:
            if run.text == shape.text:
                run.text=value;return
    shape.text=value

def replace_runs(shape, old, new):
    if not shape.has_text_frame:return
    for para in shape.text_frame.paragraphs:
        for run in para.runs:
            if old in run.text:run.text=run.text.replace(old,new)

def replace_shape(slide, needle, new):
    for sh in slide.shapes:
        if sh.has_text_frame and needle in sh.text:
            if sh.text.strip()==needle:set_text(sh,new)
            else:replace_runs(sh,needle,new)

def clear_shape(slide, sh):
    elm=sh._element;elm.getparent().remove(elm)

# Keep the supplied template's theme, grids and section hierarchy. Correct its first pages.
replace_shape(p.slides[0],'Instagram · Facebook · LinkedIn · X','Instagram · LinkedIn · X  |  Facebook optional')
replace_shape(p.slides[0],'Prompt placeholders for every post. Images to be generated and placed by the team.','First-wave visuals selected for stills and Stories; carousel and Reel frames remain prompts.')
replace_shape(p.slides[5],'Client-approved volume: 32 core pieces a month, 96 over the quarter','Proposed volume: 32 pieces a month, 96 over the quarter')
replace_shape(p.slides[5],'Instagram + Facebook','Instagram · Facebook optional')
replace_shape(p.slides[8],'No claim, no SFDA approval','Facts and claims held for review')
replace_shape(p.slides[8],'Nothing needs referencing; the few descriptive pieces sit in January and are flagged','15 January concepts need company fact review before any publication decision')
for sh in p.slides[8].shapes:
    if sh.has_text_frame and sh.text.startswith('• November and December:'):
        set_text(sh,'• November and December: people, place and neutral observance messages; no product claims.\n• January: 15 process, technology and quality descriptions are held until Sudair confirms the real sequence, equipment and wording.\n• Review the separate claims file and obtain the client’s regulatory decision where applicable. A text scan cannot replace that review.')
replace_shape(p.slides[10],'Real first, generated only when no asset fits','Website facts are a starting point; current operating data and image identity still need confirmation')
for sh in p.slides[10].shapes:
    if sh.has_text_frame and sh.text.startswith('• Written consent for real staff'):
        set_text(sh,'• Confirm the current facility map, areas and operational status; website figures may be historic or planned.\n• Provide line-by-line capacity, actual output period and denominator (one shift / annual).\n• Identify QC, QA and technology shown in supplied images; do not label a department from appearance alone.\n• Name department leads and verify experience, affiliations and image consent.\n• Supply the current logo master, staff/event rights and public-use approval for every figure.')

# Update titles, dates and channels in the template's existing monthly content tables and detail slides.
for slide in p.slides:
    for sh in slide.shapes:
        if not sh.has_text_frame:continue
        if 'Instagram + Facebook' in sh.text:replace_runs(sh,'Instagram + Facebook','Instagram · Facebook optional')
        if 'Instagram · Facebook optional feed' in sh.text:replace_runs(sh,'Instagram · Facebook optional feed','Instagram feed · Facebook optional')
        if 'Instagram · Facebook optional stories' in sh.text:replace_runs(sh,'Instagram · Facebook optional stories','Instagram Stories · Facebook optional')
        for row in cal:
            old=row['existing_title'];new=row['proposed_title']
            if old!=new and old in sh.text:replace_runs(sh,old,new)
            if row['id'] in sh.text:
                old_date=None
                # Original date appears in an ID-bearing label as YYYY-MM-DD or MM-DD.
                new_dt=date.fromisoformat(row['date'])
                m=re.search(r'20\d\d-\d\d-\d\d',sh.text)
                if m and m.group()!=row['date']:
                    replace_runs(sh,m.group(),row['date'])
                m=re.search(r'(?<!\d)(?:11|12|01)-\d\d(?!\d)',sh.text)
                if m and m.group()!=row['date'][5:]:
                    replace_runs(sh,m.group(),row['date'][5:])

# The calendar table row immediately after each ID contains the weekday. Fix the changed dates.
for slide in p.slides:
    for i,sh in enumerate(slide.shapes):
        if not sh.has_text_frame:continue
        for id,row in byid.items():
            if id in sh.text and re.search(r'\b(?:11|12|01)-\d\d\b',sh.text) and i+1<len(slide.shapes):
                nxt=slide.shapes[i+1]
                if nxt.has_text_frame:
                    weekday=date.fromisoformat(row['date']).strftime('%a')
                    for w in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']:
                        if nxt.text.startswith(w+' · '):replace_runs(nxt,w+' · ',weekday+' · ');break

# Swap row positions for November date changes so the existing template tables stay chronological.
def swap_calendar_rows(slide,id1,id2):
    starts={}
    for i,sh in enumerate(slide.shapes):
        if sh.has_text_frame:
            if sh.text.startswith(id1+'  '):starts[id1]=i
            if sh.text.startswith(id2+'  '):starts[id2]=i
    if len(starts)!=2:return
    a,b=starts[id1],starts[id2]
    all_shapes=list(slide.shapes)
    grp1=all_shapes[a-1:a+5];grp2=all_shapes[b-1:b+5]
    dy=grp2[0].top-grp1[0].top
    for sh in grp1:sh.top+=dy
    for sh in grp2:sh.top-=dy
for s in list(p.slides)[:16]:
    swap_calendar_rows(s,'NOV-F04','NOV-F07')
    swap_calendar_rows(s,'NOV-S04','NOV-S07')
    swap_calendar_rows(s,'NOV-L03','NOV-L04')

# Replace only image placeholders with the user's first-wave files. No source-composite image is inserted.
placed=[]
for slide in p.slides:
    for sh in list(slide.shapes):
        if not sh.has_text_frame:continue
        m=re.search(r'^IMAGE · ((?:NOV|DEC|JAN)-[FS]\d{2})',sh.text)
        if not m:continue
        id=m.group(1);img=IMAGES/(id+'.png')
        if not img.exists():raise FileNotFoundError(img)
        # Original placeholder's photo well is the shape immediately before its label.
        idx=list(slide.shapes).index(sh)
        well=slide.shapes[idx-1]
        x,y,w,h=well.left,well.top,well.width,well.height
        clear_shape(slide,sh)
        clear_shape(slide,well)
        slide.shapes.add_picture(str(img),x,y,width=w,height=h)
        placed.append(id)

# Red corner marker on held concepts and on illustrative images that purport to depict the real site/team.
review_ids={x['id'] for x in cal if x['claim_review']}
source_manifest=json.loads((R/'Generated_Stills'/'Source_Verified'/'source_verified_manifest.json').read_text(encoding='utf-8'))
# First-wave art is preferred aesthetically, but its photographed-looking scenes must be
# matched to the literal Sudair source before anyone describes them as documentary.
review_ids|={x['id'] for x in source_manifest if x.get('source')=='REAL'}
review_ids|={'NOV-S03','NOV-F12','DEC-F06','JAN-F11'}
for slide in p.slides:
    ids=set()
    for sh in slide.shapes:
        if sh.has_text_frame:
            ids.update(re.findall(r'\b(?:NOV|DEC|JAN)-[FSL]\d{2}\b',sh.text))
    if not ids.intersection(review_ids):continue
    flag=slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,Inches(12.35),Inches(0.0),Inches(.98),Inches(.30))
    flag.fill.solid();flag.fill.fore_color.rgb=RGBColor(185,35,42);flag.line.fill.background()
    tf=flag.text_frame;tf.clear();tf.paragraphs[0].text='REVIEW'
    for r in tf.paragraphs[0].runs:r.font.size=Pt(9);r.font.bold=True;r.font.color.rgb=RGBColor(255,255,255)

# A text-only observance decision slide uses the original template's white/green language.
obs=p.slides.add_slide(p.slide_layouts[6])
top=obs.shapes.add_shape(MSO_SHAPE.RECTANGLE,0,0,p.slide_width,Inches(.1))
top.fill.solid();top.fill.fore_color.rgb=RGBColor(0,153,93);top.line.fill.background()
def tx(value,x,y,w,h,size=18,bold=False,color=RGBColor(0,79,53)):
    sh=obs.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
    sh.text=value
    sh.text_frame.word_wrap=True
    for para in sh.text_frame.paragraphs:
        for run in para.runs:
            run.font.name='Aptos';run.font.size=Pt(size);run.font.bold=bold;run.font.color.rgb=color
    return sh
tx('Important days: planned, optional and held',.55,.33,12.2,.55,26,True)
tx('November 2026–January 2027 · editorial decisions, not extra compulsory posts',.55,.93,12.2,.4,13,color=RGBColor(80,98,90))
items=[
 ('SCHEDULED','14 Nov · World Diabetes Day','NOV-F04, with a lead-in and Story; solidarity only.'),
 ('OPTIONAL SWAPS','15 Nov · Prematurity  |  17 Nov · Cervical cancer elimination\n3 Dec · Disability  |  12 Dec · UHC  |  18 Dec · Arabic Language\n24 Jan · Education','Add only if a relevant, approved Sudair story or respectful neutral message serves the audience.'),
 ('HOLD / MONITOR','AMR, disease-specific claims, epidemic preparedness, accessible packaging','Do not imply a product, service, capability or partnership absent from the source record.'),
 ('NEXT QUARTER','22 Feb · Saudi Founding Day  |  Ramadan / Eid: official Saudi dates\n11 Mar · Saudi Flag Day','Reserve these dates; they are outside this November–January plan.'),
]
y=1.55
for label,days,note in items:
    h=1.05 if label!='OPTIONAL SWAPS' else 1.42
    b=obs.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(.55),Inches(y),Inches(12.15),Inches(h))
    b.fill.solid();b.fill.fore_color.rgb=RGBColor(237,246,240);b.line.fill.background()
    tx(label,.8,y+.16,2.3,.35,13,True)
    tx(days,3.03,y+.1,9.2,.55 if h==1.05 else .82,14,True)
    tx(note,3.03,y+(.61 if h==1.05 else .91),9.2,.31,10,color=RGBColor(68,85,78))
    y+=h+.18
tx('Date sources: WHO campaigns, Saudi MOH health-days calendar, Saudi official holiday calendar. Confirm lunar dates before scheduling.',.58,7.13,12.0,.2,8,color=RGBColor(95,105,99))

# Front-load all nine existing monthly content tables; keep their artwork and section slides unchanged.
all_ids=list(p.slides._sldIdLst)
tables=[13,14,15,49,50,51,85,86,87]  # original zero-based indices
order=list(range(12))+[len(all_ids)-1]+tables+[i for i in range(len(all_ids)-1) if i not in set(range(12))|set(tables)]
for el in all_ids:p.slides._sldIdLst.remove(el)
for i in order:p.slides._sldIdLst.append(all_ids[i])
for number,slide in enumerate(p.slides,1):
    for sh in slide.shapes:
        if sh.has_text_frame and sh.text.strip().isdigit() and sh.left>Inches(12.0) and sh.top>Inches(7.0):
            set_text(sh,str(number))

p.save(OUT)
print(OUT,'slides',len(p.slides),'first-wave images',len(placed),'unique',len(set(placed)))
