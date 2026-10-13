# 04 Prompt formulas

All prompts are written in English. Arabic strings stay in Arabic and are quoted exactly. Prompts target image generators (ChatGPT image, Gemini, Midjourney v7, Flux) and image-to-video tools (Veo, Kling, Runway, Seedance, Sora).

## A. Still tile (feed, LinkedIn, X)
Ten blocks, always in this order. A short prompt is a bad prompt.

1. **FORMAT**: `Square-safe social tile, 1080 × 1350 px (4:5), designed for Instagram, Facebook, LinkedIn and X.`
2. **BRAND**: `Sudair Pharma corporate post. Main theme: Visible capability. Measurable impact.`
3. **HERO** (the message first): what the picture must show, in one precise sentence, then the detail (subject, action, setting, props, wardrobe, expression).
4. **TREATMENT**: the code from file 03 and its prompt block.
5. **COMPOSITION**: zones with pixel ranges (hero zone, text zone, logo zone), camera angle and lens (`35 mm, eye level`), depth.
6. **LIGHT AND GRADE**: key light, rim light, colour grade, mood.
7. **COLOUR**: gradient hexes from file 01; one accent only.
8. **TEXT (render exactly)**: every string with language, font, weight, size, colour, alignment, position and effect. Arabic is right-to-left. Include the kashida word if used.
9. **LOGO AND UI**: `Reserve a clean 190 × 190 px area at the top-left for the logo. Do not draw any logo or tagline.` (place the real file afterwards). Add a 24 px hairline inset frame if the treatment uses one.
10. **NEGATIVE**: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills or packs, medical claims, distorted hands, uncanny faces, saturated neon, text outside the safe zones.

When a real asset is used, add a line before the HERO: `INPUT IMAGE: upload "Sudair Assets/<relative path>". Keep faces, clothing and architecture exactly as photographed. Only regrade colour and extend the background.`

### Text block template
```
TEXT (render exactly, right-to-left for Arabic):
1. Arabic headline line 1 «...» — AE_Sharjah style heavy kufi, 124 px, white #FFFFFF, right-aligned at x=1020, y=210.
2. Arabic headline line 2 «...» — same family, 84 px, mint #8EF0B0, kashida on «...».
3. English line «...» — Friz Quadrata Bold Italic style, 28 px uppercase, white 90%, centred, y=380.
4. Chip «...» — rounded pill, outline 1 px #85C66F, text 24 px white, y=1180.
Keep all text inside x 60–1020 and y 150–1230.
```

## B. Carousel (IG/FB and LinkedIn/X)
- 5 slides is the default, up to 7 for process posts. 1080 × 1350 each.
- **Slide 1 (hook)**: one question or one claim in the headline; hero visual; a small "swipe" arrow chip at the bottom right.
- **Slides 2 to N-1**: one idea per slide, the same treatment family, a slide counter «٢/٥» top-right (Arabic-Indic digits) and `2/5` in small English.
- **Last slide (CTA)**: theme line, soft call to action, website, logo large.
- Continuity: the background gradient flows across slides (the glow moves 15% per slide), the hero object recurs in a different position, the headline baseline stays at y=210.
- Each slide gets its own full prompt, written with blocks 1–10. Do not write "same as slide 1".

## C. Story (1080 × 1920)
Blocks 1–10 with these changes: the safe area is y 250–1580; the headline in the upper third; one sticker zone (poll, question box, countdown) drawn as an empty rounded rectangle labelled `STICKER ZONE` for the app to place; a 24 px inset frame; progress dots are not drawn.

## D. Reel (9:16, 15 to 30 s)
Per reel provide:
1. **Concept** (one sentence) and **objective**.
2. **Format**: duration, aspect 9:16, fps 30, resolution 1080 × 1920, cut rhythm.
3. **Shot list**. Each shot has: number, seconds, **still prompt** (a block 1–10 prompt for the key frame, 9:16, without text), **animation prompt** (see below), **on-screen text** (AR and EN with font, size, position, entry and exit animation), **voice-over or caption** (AR and EN), **asset** (real footage with its timecode when available).
4. **Audio**: music mood and tempo (no named tracks), sound effects (soft ambience, no dramatic risers), voice-over style.
5. **Cover frame**: a still tile prompt for the Reel cover (grid-safe 1:1 centre).
6. **End card**: logo, theme line, website, 2 seconds.

### Animation prompt formula (image-to-video)
`Start from the supplied key frame. [CAMERA MOVE: slow push-in / lateral dolly / orbit 20° / locked off]. [SUBJECT MOTION: what moves, how, at what speed]. [ENVIRONMENT: light shift, particles, steam, reflections]. [TEMPO: duration in seconds, ease-in-out]. Keep the subject, faces, clothing, signage and layout identical to the key frame. No new objects, no text changes, no morphing, no flicker. Output 9:16, 24 fps, 5 s.`
Typical camera verbs: `slow push-in 8%`, `parallax of foreground petals`, `rack focus from foreground flasks to the technician`, `slow rotation of the glass object 25°`, `light sweep across the facade`.

## E. Prompt hygiene
- One hero per prompt. No more than 8 strings of text. Keep Arabic lines under 5 words.
- Never ask a generator to draw the Sudair logo. Never ask it to write a URL longer than the domain name; set small text in the layout tool.
- Specify real hexes and pixel positions. Generators follow position words (`upper third`, `lower left`) better than abstract style words.
- Ask for 4 variations, choose one, fix the text in a layout tool with the brand fonts. Treat generated Arabic as a draft.
- Photoreal people: say `Saudi`, name the wardrobe, say `natural skin texture, no beauty filter`.
