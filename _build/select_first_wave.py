import json, re, shutil
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parent
LIST=Path(r'C:\Users\mohamed.hashish\.codex\attachments\641a845f-4e76-4566-aec7-86e5c1edca4c\Pasted text.txt')
OUT=ROOT/'Generated_Stills'/'First_Wave_Only'
OUT.mkdir(exist_ok=True)
entries=[]
for line in LIST.read_text(encoding='utf-8-sig').splitlines():
    p=Path(line.strip().strip('"'))
    if p.suffix.lower()=='.png' and re.match(r'^(NOV|DEC|JAN)-[FS]\d{2}',p.name):
        entries.append(p)
groups=defaultdict(list)
for p in entries:
    groups[re.match(r'([A-Z]+-[FS]\d{2})',p.name).group(1)].append(p)
selected=[]
for id,files in sorted(groups.items()):
    # Earlier image wave wins: unsuffixed original, then v3, then v4, then a labelled draft.
    def rank(p):
        n=p.stem
        return (0 if n==id else 1 if n==id+'-v3' else 2 if n==id+'-v4' else 3,n)
    p=min(files,key=rank)
    if not p.exists(): raise FileNotFoundError(p)
    dst=OUT/(id+'.png')
    shutil.copy2(p,dst)
    selected.append({'id':id,'selected_from':str(p),'output':str(dst),'variants_listed':[f.name for f in files]})
(OUT/'selection_manifest.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'README.md').write_text('# First-wave image selection\n\nOne chosen image per post ID from the user-provided path list. Contact sheets and unchosen variants are excluded. These are design drafts, not authenticated photographs of Sudair facilities or employees. Verify image context, Arabic, logo and rights before publication.\n',encoding='utf-8')
print('listed',len(entries),'selected',len(selected),'folder',OUT)
