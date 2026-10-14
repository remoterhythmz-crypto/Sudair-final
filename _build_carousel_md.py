# -*- coding: utf-8 -*-
"""Build Sudair_Carousel_All_Slides_Review.md from the prompt book workbook."""
import openpyxl, io, os, collections

BOOK = r"D:\Medical communications- 2025\Sudair\Corporate_Sudair_Social\Sudair_3Month_Pack\Sudair_3Month_Prompt_Book.xlsx"
OUT  = r"D:\Medical communications- 2025\Sudair\Corporate_Sudair_Social\Sudair_3Month_Pack\Content_Review\Sudair_Carousel_All_Slides_Review.md"

# claim-flagged pieces (from Claims review sheet)
wb = openpyxl.load_workbook(BOOK, data_only=True)
claims = {}
ws = wb['Claims review']
for r in ws.iter_rows(min_row=2, values_only=True):
    if r[0]:
        claims[r[0]] = (r[7], r[8])  # claim type, what to verify

ws = wb['Carousel slides']
hdr = [c.value for c in ws[1]]
rows = [dict(zip(hdr, r)) for r in ws.iter_rows(min_row=2, values_only=True) if r[0]]

pieces = collections.OrderedDict()
for r in rows:
    pid = r['Piece ID']
    pieces.setdefault(pid, []).append(r)

by_id = {}
wsc = wb['Calendar']
chdr = [c.value for c in wsc[1]]
for r in wsc.iter_rows(min_row=2, values_only=True):
    if r[0]:
        d = dict(zip(chdr, r))
        by_id[d['ID']] = d

out = io.open(OUT, 'w', encoding='utf-8')
w = out.write

w("""# Sudair Pharma — all carousel slides, full review edition
**Window:** November 2026 – January 2027 · **Source:** `Sudair_3Month_Prompt_Book.xlsx` → sheet *Carousel slides* (172 slides across 33 carousels)
**Generated:** 13 October 2026 (content review pass)

Every carousel piece, every slide, with the exact Arabic/English strings, the typography specification and the generation prompt.
Status per piece: **APPROVE** = design and copy fine · **EDIT** = usable after the listed fix · **REBUILD** = do not generate until fixed.
Claim-flagged January pieces (⚠) additionally require client regulatory sign-off — see `Sudair_3Month_Claims_and_Approval_Review.md`.

---
""")

month_names = {'NOV': 'November 2026', 'DEC': 'December 2026', 'JAN': 'January 2027'}
cur_month = None
for pid, slides in pieces.items():
    mon = pid.split('-')[0]
    if mon != cur_month:
        cur_month = mon
        w(f"\n## {month_names.get(mon, mon)}\n\n")
    meta = by_id.get(pid, {})
    title = slides[0]['Piece title']
    date = str(slides[0]['Date'])[:10]
    channel = slides[0]['Channel']
    flag = pid in claims
    badge = " ⚠ CLAIM REVIEW" if flag else ""
    w(f"### {pid} — {title}{badge}\n")
    w(f"- **Date:** {date}  |  **Channel:** {channel}  |  **Format:** Carousel, {len(slides)} slides  |  **Pillar:** {meta.get('Pillar','—')}\n")
    if flag:
        w(f"- ⚠ **Client must verify:** {claims[pid][1]}\n")
    cap_ar = next((s['Piece caption (AR)'] for s in slides if s.get('Piece caption (AR)') not in (None,'None','')), '')
    cap_en = next((s['Piece caption (EN)'] for s in slides if s.get('Piece caption (EN)') not in (None,'None','')), '')
    tags  = next((s['Hashtags'] for s in slides if s.get('Hashtags') not in (None,'None','')), '')
    if cap_ar:
        w(f"- **Caption (AR):**\n\n> {str(cap_ar).strip().replace(chr(10), chr(10)+'> ')}\n\n")
    if cap_en:
        w(f"- **Caption (EN):**\n\n> {str(cap_en).strip().replace(chr(10), chr(10)+'> ')}\n\n")
    if tags:
        w(f"- **Hashtags:** {tags}\n")
    w("\n")
    for s in slides:
        n = s['Slide']; tot = s['of']; role = s['Role']
        w(f"#### Slide {n}/{tot} — {role}\n")
        w(f"**Treatment:** {s['Treatment']} · **Canvas:** {s['Canvas']}\n\n")
        w(f"**Hero:** {s['Hero (what the picture shows)']}\n\n")
        if s.get('Asset paths (relative to Sudair Assets)'):
            paths = str(s['Asset paths (relative to Sudair Assets)']).replace('\n', '\n  - ')
            w(f"**Assets (root = `Sudair Assets`):**\n  - {paths}\n\n")
        w(f"| Element | String |\n|---|---|\n")
        w(f"| Arabic headline 1 | {s['Arabic headline 1']} |\n")
        w(f"| Arabic headline 2 | {s['Arabic headline 2'] or '—'} |\n")
        w(f"| Kashida word | {s['Kashida word'] or '—'} |\n")
        w(f"| English headline | {s['English headline']} |\n")
        w(f"| Arabic body | {s['Arabic body'] or '—'} |\n")
        w(f"| English body | {s['English body'] or '—'} |\n\n")
        ty = str(s['Typography spec'] or '').strip()
        if ty:
            w("**Typography spec:**\n\n")
            for line in ty.split('\n'):
                w(f"  {line}\n")
            w("\n")
        pr = str(s['Slide image prompt (full)'] or '').strip()
        if pr:
            w("<details><summary>Full slide image prompt</summary>\n\n```\n" + pr + "\n```\n\n</details>\n\n")
        w("---\n\n")

out.close()
print("written", OUT, len(pieces), "carousels,", len(rows), "slides")
