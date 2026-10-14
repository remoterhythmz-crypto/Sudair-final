import json
from pathlib import Path

R=Path(__file__).resolve().parent
cal=json.loads((R/'Sudair_3Month_Content_Calendar_v2.json').read_text(encoding='utf-8'))
sel=json.loads((R/'Generated_Stills/First_Wave_Only/selection_manifest.json').read_text(encoding='utf-8'))
src=json.loads((R/'Generated_Stills/Source_Verified/source_verified_manifest.json').read_text(encoding='utf-8'))
by={x['id']:x for x in sel}; real={x['id'] for x in src if x.get('source')=='REAL'}
issues={
 'NOV-F02':'Visual may represent a real lab team, but the depicted faces are generated/reconstructed; replace with a literal approved photograph or label as illustration.',
 'NOV-S03':'Generated facility and family scene can be mistaken for the actual Sudair site; use a literal campus photo or remove the place-specific wording.',
 'NOV-F12':'Generated recap combines an invented-looking building and people; use dated Sudair source photos.',
 'DEC-F06':'Conference group needs exact event/photo identity, participant consent and revised conference-specific copy.',
 'DEC-F07':'People and campus are illustrative; verify before presenting as Sudair colleagues or a real site view.',
 'JAN-F11':'Generated group portrait must not be called Sudair’s quality team. Replace with consented team image and approved names/roles.',
}
lines=['# First-wave visual selection and required edits','',
'The user-selected **first image wave** is the only still/Story image source for the revised presentation. It contains 54 chosen PNGs, one per post ID, in `Generated_Stills/First_Wave_Only/`. Contact sheets, duplicate variants and later source-composite images are not used in that deck. The original generator outputs remain archived in their existing folders; they are excluded from the selected set.','',
'## What the visuals are','',
'These images are creative concepts. Some depict photographic-looking facilities, equipment, events or people, but the prompt alone does not prove that every depicted detail is a literal Sudair photograph. Where a prompt names an actual Sudair asset, the final publication artwork must be checked against that source file or the caption must clearly avoid documentary claims. The red REVIEW mark in the deck identifies asset/fact checks; it does not mean the visual design is rejected.','',
'## Priority edits','',
'| ID | Edit |','|---|---|']
for k,v in issues.items():lines.append(f'| {k} | {v} |')
lines+=['',
'**Across all 54:** typeset Arabic and English again in the layout tool where any glyph, kashida, diacritic or small subtitle is uncertain; use the supplied logo master at adequate resolution; test Story safe zones and feed crops. Keep the emerald wave, depth and single-hero compositions that made this first wave stronger. Avoid using the generated facility as factual evidence in an investor-facing post.','',
'## Selection register','',
'| ID | Channel | Chosen first-wave source | Check before release |','|---|---|---|']
for r in cal:
    id=r['id']
    if id not in by:continue
    source=Path(by[id]['selected_from']).name
    review=[]
    if id in real:review.append('literal asset match')
    if r['claim_review']:review.append('facility/process fact')
    if id in issues:review.append('specific edit above')
    if not review:review.append('design, type and rights proof')
    lines.append(f"| {id} | {r['channel'].split(';')[0]} | `{source}` | {', '.join(review)} |")
lines+=['',
'## Website facts already available; remaining data to request','',
'The [Sudair operations page](https://sudairpharma.com/operations/) publishes a 72,000 m² site and 12,000 m² built area. The [projects page](https://sudairpharma.com/projects/) publishes separate oncology production/storage areas and one-shift line capacities. These do not establish the current operating map, actual output, equipment identity, departmental leaders, or consent to show an employee. The concise request is in `Sudair_Client_Data_Requirements_Simple_v2.docx` and `.md`.','']
out=R/'Sudair_First_Wave_Selection_and_Review.md';out.write_text('\n'.join(lines),encoding='utf-8')
print(out,'selected',len(sel),'source-match-review',len(real))
