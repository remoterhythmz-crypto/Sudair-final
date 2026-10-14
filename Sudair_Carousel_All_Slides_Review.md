# Sudair Pharma — all carousel slides, full review edition
**Window:** November 2026 – January 2027 · **Source:** `Sudair_3Month_Prompt_Book.xlsx` → sheet *Carousel slides* (172 slides across 33 carousels)
**Generated:** 13 October 2026 (content review pass)

Every carousel piece, every slide, with the exact Arabic/English strings, the typography specification and the generation prompt.
Status per piece: **APPROVE** = design and copy fine · **EDIT** = usable after the listed fix · **REBUILD** = do not generate until fixed.
Claim-flagged January pieces (⚠) additionally require client regulatory sign-off — see `Sudair_3Month_Claims_and_Approval_Review.md`.

---

## November 2026

### NOV-L01 — Inside Sudair City: the site, the people, the day
- **Date:** 2026-11-02  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Meet the makers
- **Caption (AR):**

> داخل مدينة سدير للصناعات الدوائية، يبدأ اليوم قبل أن تُضاء الواجهة.
> مكانٌ يتسع للمختبر وقاعة التعبئة والممرات والنخيل، ويتسع قبل ذلك كله لناسٍ يعرفون بعضهم بالاسم.
> جولة قصيرة بين المكان والناس واليوم.
> تابعوا الصفحة لنرافقكم أكثر من الداخل.

- **Caption (EN):**

> Inside Sudair City, the day begins before the facade lights come on.
> The site holds the lab, the packaging hall, the corridors and the palms. Before all that, it holds people who know each other by name.
> A short walk through the place, the people and the day.
> Follow the page and see more from the inside.

- **Hashtags:** #سدير_للأدوية #SudairPharma #مدينة_سدير #SudairCity

#### Slide 1/5 — hook
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Petal-window key visual over the real golden-hour campus: three glowing petals showing people at work; headline in the dark left column. Keep the top-left corner clear for the logo.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | داخل مدينة سدير |
| Arabic headline 2 | المكان والناس |
| Kashida word | مدينة |
| English headline | Inside Sudair City |
| Arabic body | جولة قصيرة في المكان والناس واليوم. |
| English body | A short walk through the place, the people and the day. |

**Typography spec:**

  1. Arabic headline line 1 «داخل مدينة سدير» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «المكان والناس» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «مدينة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «جولة قصيرة في المكان والناس واليوم.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «Inside Sudair City» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «A short walk through the place, the people and the day.» — Roboto Light, 34 px, white 80%, y=626.
  6. Chip «SUDAIR CITY» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A001: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A005: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Petal-window key visual over the real golden-hour campus: three glowing petals showing people at work; headline in the dark left column. Keep the top-left corner clear for the logo.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «داخل مدينة سدير» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «المكان والناس» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «مدينة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «جولة قصيرة في المكان والناس واليوم.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «Inside Sudair City» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «A short walk through the place, the people and the day.» — Roboto Light, 34 px, white 80%, y=626.
6. Chip «SUDAIR CITY» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The real drone view of the whole site in the desert, graded to emerald and teal; wide and calm, headline over the dark sky area, no people.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | مكانٌ في قلب نجد |
| Arabic headline 2 | اسمه سدير |
| Kashida word | قلب |
| English headline | A place in Najd called Sudair |
| Arabic body | موقعٌ واسع، وواجهةٌ بين النخيل. |
| English body | A wide site, and a facade among palms. |

**Typography spec:**

  1. Arabic headline line 1 «مكانٌ في قلب نجد» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «اسمه سدير» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «قلب» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «موقعٌ واسع، وواجهةٌ بين النخيل.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «A place in Najd called Sudair» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «A wide site, and a facade among palms.» — Roboto Light, 34 px, white 80%, y=626.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The real drone view of the whole site in the desert, graded to emerald and teal; wide and calm, headline over the dark sky area, no people.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «مكانٌ في قلب نجد» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «اسمه سدير» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «قلب» with kashida (tatweel) for rhythm.
3. Arabic supporting line «موقعٌ واسع، وواجهةٌ بين النخيل.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «A place in Najd called Sudair» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «A wide site, and a facade among palms.» — Roboto Light, 34 px, white 80%, y=626.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Women and men of the packaging hall standing together at the line, wide, teal-green grade, natural faces; crop so no container or label is readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | وفيه ناس |
| Arabic headline 2 | نساء ورجال |
| Kashida word | رجال |
| English headline | And in it, people |
| Arabic body | كلٌّ في محطته، والفريق واحد. |
| English body | Women and men, each at a station, one team. |

**Typography spec:**

  1. Arabic headline line 1 «وفيه ناس» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «نساء ورجال» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «رجال» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «كلٌّ في محطته، والفريق واحد.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «And in it, people» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Women and men, each at a station, one team.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Women and men of the packaging hall standing together at the line, wide, teal-green grade, natural faces; crop so no container or label is readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وفيه ناس» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «نساء ورجال» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «رجال» with kashida (tatweel) for rhythm.
3. Arabic supporting line «كلٌّ في محطته، والفريق واحد.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «And in it, people» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Women and men, each at a station, one team.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab analyst at the bench in profile, calm and focused, daylight, dark green panel on the right for text; no readable label on any container.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | ومن الصباح |
| Arabic headline 2 | إلى المساء |
| Kashida word | الصباح |
| English headline | From morning to evening |
| Arabic body | يومٌ كاملٌ، بأيدي أهله. |
| English body | A full day, in the hands of its people. |

**Typography spec:**

  1. Arabic headline line 1 «ومن الصباح» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «إلى المساء» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «الصباح» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يومٌ كاملٌ، بأيدي أهله.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «From morning to evening» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «A full day, in the hands of its people.» — Roboto Light, 26 px, white 80%, y=746.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab analyst at the bench in profile, calm and focused, daylight, dark green panel on the right for text; no readable label on any container.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ومن الصباح» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «إلى المساء» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «الصباح» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يومٌ كاملٌ، بأيدي أهله.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «From morning to evening» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «A full day, in the hands of its people.» — Roboto Light, 26 px, white 80%, y=746.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, centred two-level Arabic theme line, thin mint rule, small white line icon; hairline inset frame. No photograph. Real logo placed by the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | صناعة |
| English headline | Visible capability. Measurable impact. |
| Arabic body | تابعوا الصفحة لمزيدٍ من الداخل. |
| English body | Follow the page for more from the inside. |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «صناعة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تابعوا الصفحة لمزيدٍ من الداخل.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Follow the page for more from the inside.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, centred two-level Arabic theme line, thin mint rule, small white line icon; hairline inset frame. No photograph. Real logo placed by the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «صناعة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تابعوا الصفحة لمزيدٍ من الداخل.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Follow the page for more from the inside.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### NOV-L02 — Careers at Sudair: what working here looks like
- **Date:** 2026-11-04  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** People and careers
- **Caption (AR):**

> كيف يبدو العمل في سدير للأدوية؟
> فريقٌ بجانبك في كل محطة، ومكانٌ تراه بعينك، وزمالةٌ تكبر بالأيام.
> هذه نظرة هادئة إلى يوم عملٍ بين الناس.
> تابعوا الصفحة لتعرفوا المزيد عن العمل معنا.

- **Caption (EN):**

> What does working at Sudair Pharma look like?
> A team beside you at every station, a place you can see for yourself, and colleagues who become friends over the days.
> A quiet look at a working day among people.
> Follow the page to see more of working with us.

- **Hashtags:** #سدير_للأدوية #SudairPharma #وظائف #Careers #SudairCareers

#### Slide 1/5 — hook
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Staff portrait panel: the lab analyst at the bench, three-quarter view, soft light from the left, dark green panel with a faint vertical line pattern on the right for the headline. Keep the top-left corner clear for the logo.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | كيف يبدو العمل |
| Arabic headline 2 | في سدير؟ |
| Kashida word | العمل |
| English headline | What working here looks like |
| Arabic body | فريقٌ، وطاولة عمل، ويوم كامل. |
| English body | A team, a bench, a full day. |

**Typography spec:**

  1. Arabic headline line 1 «كيف يبدو العمل» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «في سدير؟» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «العمل» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «فريقٌ، وطاولة عمل، ويوم كامل.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «What working here looks like» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «A team, a bench, a full day.» — Roboto Light, 26 px, white 80%, y=746.
  6. Chip «CAREERS» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Staff portrait panel: the lab analyst at the bench, three-quarter view, soft light from the left, dark green panel with a faint vertical line pattern on the right for the headline. Keep the top-left corner clear for the logo.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «كيف يبدو العمل» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «في سدير؟» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «العمل» with kashida (tatweel) for rhythm.
3. Arabic supporting line «فريقٌ، وطاولة عمل، ويوم كامل.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «What working here looks like» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «A team, a bench, a full day.» — Roboto Light, 26 px, white 80%, y=746.
6. Chip «CAREERS» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab team standing together in the lab, wide, teal-green grade, relaxed and natural, no retouching beyond colour; no readable label in frame.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4

| Element | String |
|---|---|
| Arabic headline 1 | فريقٌ بجانبك |
| Arabic headline 2 | في كل محطة |
| Kashida word | فريق |
| English headline | A team beside you at every station |
| Arabic body | ولا أحد يعمل وحده. |
| English body | Nobody works alone. |

**Typography spec:**

  1. Arabic headline line 1 «فريقٌ بجانبك» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «في كل محطة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «فريق» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «ولا أحد يعمل وحده.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «A team beside you at every station» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Nobody works alone.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A005: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab team standing together in the lab, wide, teal-green grade, relaxed and natural, no retouching beyond colour; no readable label in frame.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «فريقٌ بجانبك» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «في كل محطة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «فريق» with kashida (tatweel) for rhythm.
3. Arabic supporting line «ولا أحد يعمل وحده.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «A team beside you at every station» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Nobody works alone.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The real palm-lined campus at golden light, calm and wide, headline over the sky; no people.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | مكانٌ تراه |
| Arabic headline 2 | وعملٌ تلمسه |
| Kashida word | تراه |
| English headline | A place you can see, work you can touch |
| Arabic body | ليس مكتباً بعيداً، بل مصنعٌ بين النخيل. |
| English body | Not a distant office: a plant among palms. |

**Typography spec:**

  1. Arabic headline line 1 «مكانٌ تراه» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «وعملٌ تلمسه» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «تراه» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «ليس مكتباً بعيداً، بل مصنعٌ بين النخيل.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «A place you can see, work you can touch» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «Not a distant office: a plant among palms.» — Roboto Light, 34 px, white 80%, y=626.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A001: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The real palm-lined campus at golden light, calm and wide, headline over the sky; no people.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «مكانٌ تراه» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «وعملٌ تلمسه» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «تراه» with kashida (tatweel) for rhythm.
3. Arabic supporting line «ليس مكتباً بعيداً، بل مصنعٌ بين النخيل.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «A place you can see, work you can touch» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «Not a distant office: a plant among palms.» — Roboto Light, 34 px, white 80%, y=626.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The large team group at the booth with many women in abayas and ID badges, warm and proud, wide frame, graded to the emerald palette.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG

| Element | String |
|---|---|
| Arabic headline 1 | وزمالةٌ |
| Arabic headline 2 | تكبر بالأيام |
| Kashida word | زمالة |
| English headline | Colleagues who grow close over the days |
| Arabic body | من يعمل معاً يعرف بعضه أكثر كل يوم. |
| English body | People who work together get to know each other. |

**Typography spec:**

  1. Arabic headline line 1 «وزمالةٌ» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «تكبر بالأيام» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «زمالة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «من يعمل معاً يعرف بعضه أكثر كل يوم.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Colleagues who grow close over the days» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «People who work together get to know each other.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A048: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The large team group at the booth with many women in abayas and ID badges, warm and proud, wide frame, graded to the emerald palette.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وزمالةٌ» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «تكبر بالأيام» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «زمالة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «من يعمل معاً يعرف بعضه أكثر كل يوم.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Colleagues who grow close over the days» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «People who work together get to know each other.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, centred two-level Arabic headline, thin mint rule, small white line icon; hairline inset frame. No photograph. Real logo placed by the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | تعال وشاركنا |
| Arabic headline 2 | يومنا |
| Kashida word | شاركنا |
| English headline | Come and share our day. |
| Arabic body | تابعوا صفحتنا لتعرفوا المزيد عن العمل في سدير. |
| English body | Follow the page to see more of working life at Sudair. |

**Typography spec:**

  1. Arabic headline line 1 «تعال وشاركنا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «يومنا» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شاركنا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تابعوا صفحتنا لتعرفوا المزيد عن العمل في سدير.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Come and share our day.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Follow the page to see more of working life at Sudair.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, centred two-level Arabic headline, thin mint rule, small white line icon; hairline inset frame. No photograph. Real logo placed by the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «تعال وشاركنا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «يومنا» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شاركنا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تابعوا صفحتنا لتعرفوا المزيد عن العمل في سدير.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Come and share our day.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Follow the page to see more of working life at Sudair.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### NOV-F03 — Made here, in the Kingdom
- **Date:** 2026-11-05  |  **Channel:** Instagram + Facebook  |  **Format:** Carousel, 5 slides  |  **Pillar:** Local manufacturing
- **Caption (AR):**

> ليس شعارًا، بل عنوان: مدينة سدير، المملكة العربية السعودية.
> هنا نعمل، وهنا يعمل أهلنا بين النخيل وفي قلب نجد.
> مرّروا لتروا المكان، وتابعوا الشهر لتعرفوه أكثر.

- **Caption (EN):**

> Not a slogan, an address: Sudair City, Saudi Arabia.
> This is where we work, among the palms in the heart of Najd.
> Swipe to see the place, and follow the month to know it better.

- **Hashtags:** #سدير_للأدوية #SudairPharma #صنع_في_السعودية #MadeInSaudi

#### Slide 1/5 — hook
**Treatment:** T1 Glass object · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** 3D glass-and-metal palm on emerald, the Kingdom's outline etched into the floor, headline above.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صُنع هنا |
| Arabic headline 2 | في المملكة |
| Kashida word | هنا |
| English headline | Made here, in the Kingdom |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «صُنع هنا» — AE_Sharjah-style heavy geometric kufi, 128 px, #FFFFFF, centred at y=170.
  2. Arabic headline line 2 «في المملكة» — same family, 84 px, mint #8EF0B0, y=320. Stretch the word «هنا» with kashida (tatweel) for rhythm.
  3. English line «Made here, in the Kingdom» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=430.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): 3D glass-and-metal palm on emerald, the Kingdom's outline etched into the floor, headline above.

TREATMENT T1, Glass object: Premium 3D render of the hero object, semi-transparent glass and brushed metal, soft studio light from the upper left, mint rim light, clean reflections on a glossy emerald floor, shallow depth of field. Emerald gradient background from #09A45B (top-left glow) to #04301F (bottom-right), faint rounded-diamond lattice at 8% opacity. Hero centred, 55% of tile height, 90 px free space around it.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صُنع هنا» — AE_Sharjah-style heavy geometric kufi, 128 px, #FFFFFF, centred at y=170.
2. Arabic headline line 2 «في المملكة» — same family, 84 px, mint #8EF0B0, y=320. Stretch the word «هنا» with kashida (tatweel) for rhythm.
3. English line «Made here, in the Kingdom» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=430.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T7 People hero · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A generated Saudi woman in a deep green hijab and abaya beside a generated Saudi man in a white thobe and red-white shemagh, calm, looking up and to the right, above the real drone photo of the whole site in the desert filling the lower third.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | في قلب نجد |
| Arabic headline 2 | مدينة سدير |
| Kashida word | نجد |
| English headline | In the heart of Najd, Sudair City |
| Arabic body | مدينة سدير للصناعات الدوائية في منطقة سدير. |
| English body | Sudair City for Pharma Industry, in the Sudair region. |

**Typography spec:**

  1. Arabic headline line 1 «في قلب نجد» — AE_Sharjah-style heavy geometric kufi, 76 px, #FFFFFF, centred at y=1130.
  2. Arabic headline line 2 «مدينة سدير» — same family, 52 px, mint #8EF0B0, y=1215. Stretch the word «نجد» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «مدينة سدير للصناعات الدوائية في منطقة سدير.» — Muna Regular, 40 px, white 90%, centred, y=1315.
  4. English line «In the heart of Najd, Sudair City» — Friz Quadrata Bold / italic condensed sans, 28 px, uppercase, white 90%, tracking +40, y=1280.
  5. English support line «Sudair City for Pharma Industry, in the Sudair region.» — Roboto Light, 24 px, white 80%, y=1326.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A generated Saudi woman in a deep green hijab and abaya beside a generated Saudi man in a white thobe and red-white shemagh, calm, looking up and to the right, above the real drone photo of the whole site in the desert filling the lower third.

TREATMENT T7, People hero: People-hero treatment: photoreal portrait of Saudi people (man in white thobe and red-white shemagh, woman in deep green hijab and abaya), arms crossed, proud and calm, looking up and to the right, cinematic light, teal night-sky gradient; below them a real photograph of the landmark or stage fills the lower third.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «في قلب نجد» — AE_Sharjah-style heavy geometric kufi, 76 px, #FFFFFF, centred at y=1130.
2. Arabic headline line 2 «مدينة سدير» — same family, 52 px, mint #8EF0B0, y=1215. Stretch the word «نجد» with kashida (tatweel) for rhythm.
3. Arabic supporting line «مدينة سدير للصناعات الدوائية في منطقة سدير.» — Muna Regular, 40 px, white 90%, centred, y=1315.
4. English line «In the heart of Najd, Sudair City» — Friz Quadrata Bold / italic condensed sans, 28 px, uppercase, white 90%, tracking +40, y=1280.
5. English support line «Sudair City for Pharma Industry, in the Sudair region.» — Roboto Light, 24 px, white 80%, y=1326.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — proof
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real drone photo of the palm-lined campus in golden light, full bleed, teal-green sky grade.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | بين النخيل |
| Arabic headline 2 | يعمل الناس |
| Kashida word | النخيل |
| English headline | Among the palms, people at work |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «بين النخيل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «يعمل الناس» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «النخيل» with kashida (tatweel) for rhythm.
  3. English line «Among the palms, people at work» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A001: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real drone photo of the palm-lined campus in golden light, full bleed, teal-green sky grade.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «بين النخيل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «يعمل الناس» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «النخيل» with kashida (tatweel) for rhythm.
3. English line «Among the palms, people at work» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — proof
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real photo of the women and men of the packaging hall team at the line, framed to faces and hands, no pack or label readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | نساءٌ ورجال |
| Arabic headline 2 | في موقعٍ واحد |
| Kashida word | ورجال |
| English headline | Women and men, one site |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «نساءٌ ورجال» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «في موقعٍ واحد» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «ورجال» with kashida (tatweel) for rhythm.
  3. English line «Women and men, one site» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real photo of the women and men of the packaging hall team at the line, framed to faces and hands, no pack or label readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «نساءٌ ورجال» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «في موقعٍ واحد» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «ورجال» with kashida (tatweel) for rhythm.
3. English line «Women and men, one site» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, two-level headline, thin mint rule, small palm line icon in white.

**Assets (root = `Sudair Assets`):**
  - Website slogan collection/Ar slogan.png

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | تُرى |
| English headline | Visible capability. Measurable impact. |
| Arabic body | تابعوا حكايات المكان والناس. |
| English body | Follow the stories of the place and its people. |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تابعوا حكايات المكان والناس.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Follow the stories of the place and its people.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «sudairpharma.com» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A129: upload "Sudair Assets/Website slogan collection/Ar slogan.png". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Type card on deep emerald, two-level headline, thin mint rule, small palm line icon in white.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تابعوا حكايات المكان والناس.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Follow the stories of the place and its people.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «sudairpharma.com» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### NOV-L03 — World Diabetes Day: a thank-you to the people who care
- **Date:** 2026-11-09  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Awareness days
- **Caption (AR):**

> في الرابع عشر من نوفمبر، اليوم العالمي للسكري، نقف مع كل من يعيش مع السكري.
> ونقول شكراً لمن يقف بجانبهم كل يوم: أسرةً وأصدقاء وزملاء.
> كلمة شكرٍ صغيرة وصادقة من فريق سدير للأدوية.
> شاركونا كلمة شكر لمن بجانبكم.

- **Caption (EN):**

> On World Diabetes Day, 14 November, we stand with everyone living with diabetes.
> And we say thank you to the people beside them every day: family, friends and colleagues.
> A small, sincere word of thanks from the team at Sudair Pharma.
> Share a word of thanks with someone beside you.

- **Hashtags:** #سدير_للأدوية #SudairPharma #اليوم_العالمي_للسكري #WorldDiabetesDay

#### Slide 1/5 — hook
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Deep emerald type card, centred two-level Arabic headline with the mint accent on the key word; thin mint rule; small flat blue ring icon, small; hairline inset frame. No photograph. Keep the top-left corner clear for the logo.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | نقف مع كل من يعيش |
| Arabic headline 2 | مع السكري |
| Kashida word | يعيش |
| English headline | We stand with everyone living with diabetes |
| Arabic body | اليوم العالمي للسكري، الرابع عشر من نوفمبر. |
| English body | World Diabetes Day, 14 November. |

**Typography spec:**

  1. Arabic headline line 1 «نقف مع كل من يعيش» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «مع السكري» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «يعيش» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «اليوم العالمي للسكري، الرابع عشر من نوفمبر.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «We stand with everyone living with diabetes» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «World Diabetes Day, 14 November.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «WORLD DIABETES DAY» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Deep emerald type card, centred two-level Arabic headline with the mint accent on the key word; thin mint rule; small flat blue ring icon, small; hairline inset frame. No photograph. Keep the top-left corner clear for the logo.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «نقف مع كل من يعيش» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «مع السكري» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «يعيش» with kashida (tatweel) for rhythm.
3. Arabic supporting line «اليوم العالمي للسكري، الرابع عشر من نوفمبر.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «We stand with everyone living with diabetes» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «World Diabetes Day, 14 November.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «WORLD DIABETES DAY» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on emerald, two-level Arabic headline centred, thin mint rule, small white line icon of two simple overlapping circles (people beside each other). No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | وخلف كل شخص |
| Arabic headline 2 | ناسٌ بجانبه |
| Kashida word | خلف |
| English headline | Behind every person, people beside them |
| Arabic body | أسرةٌ، وأصدقاء، وزملاء. |
| English body | Family, friends, colleagues. |

**Typography spec:**

  1. Arabic headline line 1 «وخلف كل شخص» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «ناسٌ بجانبه» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «خلف» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «أسرةٌ، وأصدقاء، وزملاء.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Behind every person, people beside them» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Family, friends, colleagues.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on emerald, two-level Arabic headline centred, thin mint rule, small white line icon of two simple overlapping circles (people beside each other). No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وخلف كل شخص» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «ناسٌ بجانبه» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «خلف» with kashida (tatweel) for rhythm.
3. Arabic supporting line «أسرةٌ، وأصدقاء، وزملاء.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Behind every person, people beside them» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Family, friends, colleagues.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on emerald, centred headline, the word for thanks in mint accent, thin mint rule, small white line icon of a heart outline. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | شكراً لمن يهتم |
| Arabic headline 2 | ويُصغي ويبقى |
| Kashida word | شكراً |
| English headline | Thank you to those who care, listen and stay |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «شكراً لمن يهتم» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «ويُصغي ويبقى» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكراً» with kashida (tatweel) for rhythm.
  3. English line «Thank you to those who care, listen and stay» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on emerald, centred headline, the word for thanks in mint accent, thin mint rule, small white line icon of a heart outline. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكراً لمن يهتم» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «ويُصغي ويبقى» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكراً» with kashida (tatweel) for rhythm.
3. English line «Thank you to those who care, listen and stay» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on emerald, centred headline, thin mint rule, small white symbol-only logo mark, small. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | وفي سدير، فريقٌ |
| Arabic headline 2 | معكم اليوم |
| Kashida word | فريق |
| English headline | At Sudair, a team with you today |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «وفي سدير، فريقٌ» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «معكم اليوم» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «فريق» with kashida (tatweel) for rhythm.
  3. English line «At Sudair, a team with you today» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on emerald, centred headline, thin mint rule, small white symbol-only logo mark, small. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وفي سدير، فريقٌ» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «معكم اليوم» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «فريق» with kashida (tatweel) for rhythm.
3. English line «At Sudair, a team with you today» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, centred two-level Arabic thank-you, thin mint rule, real logo placed by the layout tool, small flat blue ring icon. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | شكراً لكم |
| Arabic headline 2 | ونحن معكم |
| Kashida word | شكراً |
| English headline | Thank you. We are with you. |
| Arabic body | شاركونا كلمة شكر لمن بجانبكم. |
| English body | Share a word of thanks with someone beside you. |

**Typography spec:**

  1. Arabic headline line 1 «شكراً لكم» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «ونحن معكم» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكراً» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «شاركونا كلمة شكر لمن بجانبكم.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Thank you. We are with you.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Share a word of thanks with someone beside you.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, centred two-level Arabic thank-you, thin mint rule, real logo placed by the layout tool, small flat blue ring icon. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكراً لكم» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «ونحن معكم» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكراً» with kashida (tatweel) for rhythm.
3. Arabic supporting line «شاركونا كلمة شكر لمن بجانبكم.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Thank you. We are with you.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Share a word of thanks with someone beside you.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### NOV-L04 — Thank you, pharmacists
- **Date:** 2026-11-11  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Year and community
- **Caption (AR):**

> شكراً للصيادلة والصيدلانيات.
> لوقتكم الذي تمنحونه، ولاهتمامكم، وللاسم الذي تتذكرونه حين يعود الناس.
> من فريق سدير للأدوية، تحية شكرٍ وتقدير.
> قولوا لنا: من هو صيدلاني حيّكم الذي لا تنسونه؟

- **Caption (EN):**

> Thank you, pharmacists.
> For the time you give, the attention you pay, and the name you remember when people come back.
> From the team at Sudair Pharma, with respect.
> Tell us: who is the pharmacist in your neighbourhood you never forget?

- **Hashtags:** #سدير_للأدوية #SudairPharma #شكراً_للصيادلة #ThankYouPharmacists

#### Slide 1/5 — hook
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Cover card: one rounded cream card with a friendly rendered character in green clothing at a plain counter (lamp and notebook only), warm light, emerald gradient background with faint lattice. No packs, no labels. Keep the top-left corner clear for the logo.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | شكراً للصيادلة |
| Arabic headline 2 | والصيدلانيات |
| Kashida word | شكراً |
| English headline | Thank you, pharmacists |
| Arabic body | للوقت والاهتمام والاسم الذي تتذكرونه. |
| English body | For the time, the attention and the name you remember. |

**Typography spec:**

  1. Arabic headline line 1 «شكراً للصيادلة» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «والصيدلانيات» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «شكراً» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «للوقت والاهتمام والاسم الذي تتذكرونه.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Thank you, pharmacists» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  5. English support line «For the time, the attention and the name you remember.» — Roboto Light, 26 px, white 80%, y=406.
  6. Chip «THANK YOU» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Cover card: one rounded cream card with a friendly rendered character in green clothing at a plain counter (lamp and notebook only), warm light, emerald gradient background with faint lattice. No packs, no labels. Keep the top-left corner clear for the logo.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكراً للصيادلة» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «والصيدلانيات» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «شكراً» with kashida (tatweel) for rhythm.
3. Arabic supporting line «للوقت والاهتمام والاسم الذي تتذكرونه.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Thank you, pharmacists» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
5. English support line «For the time, the attention and the name you remember.» — Roboto Light, 26 px, white 80%, y=406.
6. Chip «THANK YOU» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Card with a friendly rendered character at a plain counter greeting a customer who has just walked in; lamp and notebook only; cream card with lime edge on emerald. No packs or labels.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | وقتٌ تمنحونه |
| Arabic headline 2 | لكل من يدخل |
| Kashida word | وقتٌ |
| English headline | Time you give to everyone who walks in |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «وقتٌ تمنحونه» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «لكل من يدخل» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «وقتٌ» with kashida (tatweel) for rhythm.
  3. English line «Time you give to everyone who walks in» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Card with a friendly rendered character at a plain counter greeting a customer who has just walked in; lamp and notebook only; cream card with lime edge on emerald. No packs or labels.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وقتٌ تمنحونه» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «لكل من يدخل» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «وقتٌ» with kashida (tatweel) for rhythm.
3. English line «Time you give to everyone who walks in» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Card with a friendly rendered character smiling at an elderly neighbour, both at a plain counter; notebook open with handwriting as plain scribble (no readable words); cream card on emerald.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | اسمٌ تتذكرونه |
| Arabic headline 2 | ووجهٌ يألفه الحي |
| Kashida word | اسمٌ |
| English headline | A name you remember, a face the neighbourhood knows |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «اسمٌ تتذكرونه» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «ووجهٌ يألفه الحي» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «اسمٌ» with kashida (tatweel) for rhythm.
  3. English line «A name you remember, a face the neighbourhood knows» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Card with a friendly rendered character smiling at an elderly neighbour, both at a plain counter; notebook open with handwriting as plain scribble (no readable words); cream card on emerald.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «اسمٌ تتذكرونه» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «ووجهٌ يألفه الحي» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «اسمٌ» with kashida (tatweel) for rhythm.
3. English line «A name you remember, a face the neighbourhood knows» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Card with a friendly rendered character at the end of a long day, switching off the counter lamp, a small smile; cream card on emerald; no packs or labels.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | يومٌ يطول |
| Arabic headline 2 | وابتسامةٌ تبقى |
| Kashida word | يوم |
| English headline | A long day, and a smile that stays |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «يومٌ يطول» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «وابتسامةٌ تبقى» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «يوم» with kashida (tatweel) for rhythm.
  3. English line «A long day, and a smile that stays» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Card with a friendly rendered character at the end of a long day, switching off the counter lamp, a small smile; cream card on emerald; no packs or labels.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «يومٌ يطول» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «وابتسامةٌ تبقى» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «يوم» with kashida (tatweel) for rhythm.
3. English line «A long day, and a smile that stays» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, centred two-level Arabic thank-you, thin mint rule, real logo placed by the layout tool, small white line icon. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | شكراً من القلب |
| Arabic headline 2 | فريق سدير |
| Kashida word | شكراً |
| English headline | Thank you, from the whole team. |
| Arabic body | من هو صيدلاني حيّكم؟ شاركونا اسمه. |
| English body | Who is your pharmacist? Tell us. |

**Typography spec:**

  1. Arabic headline line 1 «شكراً من القلب» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «فريق سدير» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكراً» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «من هو صيدلاني حيّكم؟ شاركونا اسمه.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Thank you, from the whole team.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Who is your pharmacist? Tell us.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, centred two-level Arabic thank-you, thin mint rule, real logo placed by the layout tool, small white line icon. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكراً من القلب» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «فريق سدير» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكراً» with kashida (tatweel) for rhythm.
3. Arabic supporting line «من هو صيدلاني حيّكم؟ شاركونا اسمه.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Thank you, from the whole team.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Who is your pharmacist? Tell us.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### NOV-F07 — A word of thanks to our partners
- **Date:** 2026-11-15  |  **Channel:** Instagram + Facebook  |  **Format:** Carousel, 5 slides  |  **Pillar:** Recognition and events
- **Caption (AR):**

> خلف كل اتفاقية وجوهٌ جلست وتحاورت ثم تصافحت.
> نشكر كل شريكٍ جلس معنا إلى الطاولة، وكل جهةٍ فتحت لنا بابها.
> شاركونا بكلمة شكر لشريكٍ تعتزّون به.

- **Caption (EN):**

> Behind every agreement there are people who sat down, talked and shook hands.
> We thank every partner who sat at the table with us, and every body that opened its door to us.
> Share a word of thanks for a partner you value.

- **Hashtags:** #سدير_للأدوية #SudairPharma #شكرا_لشركائنا #ThankYouPartners

#### Slide 1/5 — hook
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real photo of the signing line-up on stage, wide, teal-green sky grade, host signage small.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-strategic-agreement-global-health-2025.JPG

| Element | String |
|---|---|
| Arabic headline 1 | كلمة شكر صادقة |
| Arabic headline 2 | إلى شركائنا |
| Kashida word | شكر |
| English headline | A word of thanks to our partners |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «كلمة شكر صادقة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «إلى شركائنا» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «شكر» with kashida (tatweel) for rhythm.
  3. English line «A word of thanks to our partners» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A054: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-strategic-agreement-global-health-2025.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real photo of the signing line-up on stage, wide, teal-green sky grade, host signage small.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «كلمة شكر صادقة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «إلى شركائنا» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «شكر» with kashida (tatweel) for rhythm.
3. English line «A word of thanks to our partners» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T5 Speaker or event · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real photo of a local content agreement signing, event photo with a date-free caption row.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-local-content-agreement-global-health-2025.JPG

| Element | String |
|---|---|
| Arabic headline 1 | شراكاتٌ |
| Arabic headline 2 | على منصّات المعارض |
| Kashida word | شراكاتٌ |
| English headline | Partnerships, on exhibition stages |
| Arabic body | شكرًا لمن جلس معنا إلى الطاولة. |
| English body | Thank you to everyone who sat down with us at the table. |

**Typography spec:**

  1. Arabic headline line 1 «شراكاتٌ» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «على منصّات المعارض» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «شراكاتٌ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «شكرًا لمن جلس معنا إلى الطاولة.» — Muna Regular, 40 px, white 90%, centred, y=380.
  4. English line «Partnerships, on exhibition stages» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
  5. English support line «Thank you to everyone who sat down with us at the table.» — Roboto Light, 28 px, white 80%, y=426.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A052: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-local-content-agreement-global-health-2025.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real photo of a local content agreement signing, event photo with a date-free caption row.

TREATMENT T5, Speaker or event: Event card treatment: black-and-white head-and-shoulders portraits or one event photograph with a diagonal lime corner accent, emerald background with a faint large SPC logotype behind, calendar icon with date, location pin with city, a rounded outlined bar for the contact line.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شراكاتٌ» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «على منصّات المعارض» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «شراكاتٌ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «شكرًا لمن جلس معنا إلى الطاولة.» — Muna Regular, 40 px, white 90%, centred, y=380.
4. English line «Partnerships, on exhibition stages» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
5. English support line «Thank you to everyone who sat down with us at the table.» — Roboto Light, 28 px, white 80%, y=426.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — proof
**Treatment:** T5 Speaker or event · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real photo of an academic partnership signing on the Saudi Made stage.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/معرض صنع في السعودية/sudair-pharma-academic-partnership-saudi-made-2025.JPG

| Element | String |
|---|---|
| Arabic headline 1 | ومع الجامعات |
| Arabic headline 2 | طاولةٌ واحدة |
| Kashida word | الجامعات |
| English headline | And with universities, one table |
| Arabic body | شكرًا للجهات الأكاديمية التي شاركتنا. |
| English body | Thank you to the academic partners who joined us. |

**Typography spec:**

  1. Arabic headline line 1 «ومع الجامعات» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «طاولةٌ واحدة» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «الجامعات» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «شكرًا للجهات الأكاديمية التي شاركتنا.» — Muna Regular, 40 px, white 90%, centred, y=380.
  4. English line «And with universities, one table» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
  5. English support line «Thank you to the academic partners who joined us.» — Roboto Light, 28 px, white 80%, y=426.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A103: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/معرض صنع في السعودية/sudair-pharma-academic-partnership-saudi-made-2025.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real photo of an academic partnership signing on the Saudi Made stage.

TREATMENT T5, Speaker or event: Event card treatment: black-and-white head-and-shoulders portraits or one event photograph with a diagonal lime corner accent, emerald background with a faint large SPC logotype behind, calendar icon with date, location pin with city, a rounded outlined bar for the contact line.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ومع الجامعات» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «طاولةٌ واحدة» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «الجامعات» with kashida (tatweel) for rhythm.
3. Arabic supporting line «شكرًا للجهات الأكاديمية التي شاركتنا.» — Muna Regular, 40 px, white 90%, centred, y=380.
4. English line «And with universities, one table» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
5. English support line «Thank you to the academic partners who joined us.» — Roboto Light, 28 px, white 80%, y=426.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — proof
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real photo of a row of leaders and staff, women among them, standing at the booth, warm and relaxed.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/مشاركة CPHI ME 2024/sudair-pharma-leadership-team-cphi-2025.JPG

| Element | String |
|---|---|
| Arabic headline 1 | وشكرًا لفريقنا |
| Arabic headline 2 | خلف الطاولة |
| Kashida word | لفريقنا |
| English headline | And to our own team, behind the table |
| Arabic body | الذين استقبلوا وأصغوا وصافحوا. |
| English body | Who welcomed, listened and shook hands. |

**Typography spec:**

  1. Arabic headline line 1 «وشكرًا لفريقنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «خلف الطاولة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «لفريقنا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الذين استقبلوا وأصغوا وصافحوا.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «And to our own team, behind the table» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Who welcomed, listened and shook hands.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A094: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/مشاركة CPHI ME 2024/sudair-pharma-leadership-team-cphi-2025.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real photo of a row of leaders and staff, women among them, standing at the booth, warm and relaxed.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وشكرًا لفريقنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «خلف الطاولة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «لفريقنا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الذين استقبلوا وأصغوا وصافحوا.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «And to our own team, behind the table» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Who welcomed, listened and shook hands.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, two-level headline, thin mint rule, small palm line icon.

**Assets (root = `Sudair Assets`):**
  - Website slogan collection/Ar slogan.png

| Element | String |
|---|---|
| Arabic headline 1 | شكرًا لكم |
| Arabic headline 2 | من القلب |
| Kashida word | شكرًا |
| English headline | Thank you, from the heart |
| Arabic body | صناعة تُرى، وأثر يُقاس. |
| English body | Visible capability. Measurable impact. |

**Typography spec:**

  1. Arabic headline line 1 «شكرًا لكم» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «من القلب» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكرًا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Thank you, from the heart» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Event photographs from past participations.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A129: upload "Sudair Assets/Website slogan collection/Ar slogan.png". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Type card on deep emerald, two-level headline, thin mint rule, small palm line icon.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكرًا لكم» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «من القلب» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكرًا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Thank you, from the heart» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Event photographs from past participations.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### NOV-L05 — Women and men of Sudair: a working day
- **Date:** 2026-11-16  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Meet the makers
- **Caption (AR):**

> نساءٌ ورجالٌ من سدير، ويومُ عملٍ يمرّ بكل محطة.
> بعضهم عند الطاولة بتركيز هادئ، وبعضهم عند الخط يداً بيد، وفي آخر اليوم فريقٌ واحد.
> صورةٌ لعملٍ عاديّ يصنعه ناسٌ حقيقيون.
> أخبرونا: أي جزء من المكان تودّون أن تروه؟

- **Caption (EN):**

> Women and men of Sudair, and a working day that passes through every station.
> Some at the bench in quiet focus, some at the line hand in hand, and at the end of the day, one team.
> A picture of ordinary work, made by real people.
> Tell us which part of the place you would like to see.

- **Hashtags:** #سدير_للأدوية #SudairPharma #نساء_ورجال_سدير #PeopleOfSudair

#### Slide 1/5 — hook
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Wide team photograph of women and men at the packaging line, graded teal-green, golden side light, natural faces; no label readable. Keep the top-left corner clear for the logo.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | نساء ورجال من سدير |
| Arabic headline 2 | يوم عمل |
| Kashida word | رجال |
| English headline | Women and men of Sudair |
| Arabic body | محطةً بعد محطة. |
| English body | Station by station. |

**Typography spec:**

  1. Arabic headline line 1 «نساء ورجال من سدير» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «يوم عمل» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «رجال» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «محطةً بعد محطة.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Women and men of Sudair» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Station by station.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «A WORKING DAY» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Wide team photograph of women and men at the packaging line, graded teal-green, golden side light, natural faces; no label readable. Keep the top-left corner clear for the logo.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «نساء ورجال من سدير» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «يوم عمل» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «رجال» with kashida (tatweel) for rhythm.
3. Arabic supporting line «محطةً بعد محطة.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Women and men of Sudair» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Station by station.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «A WORKING DAY» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab analyst at the bench in profile, calm, quiet focus, daylight, dark green panel for text; no label legible.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | بعضهم عند الطاولة |
| Arabic headline 2 | بتركيز هادئ |
| Kashida word | تركيز |
| English headline | Some at the bench, in quiet focus |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «بعضهم عند الطاولة» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «بتركيز هادئ» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «تركيز» with kashida (tatweel) for rhythm.
  3. English line «Some at the bench, in quiet focus» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab analyst at the bench in profile, calm, quiet focus, daylight, dark green panel for text; no label legible.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «بعضهم عند الطاولة» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «بتركيز هادئ» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «تركيز» with kashida (tatweel) for rhythm.
3. English line «Some at the bench, in quiet focus» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A closer crop of the packaging-hall team working side by side, hands and shoulders, warm light; no container or label readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | وبعضهم عند الخط |
| Arabic headline 2 | يداً بيد |
| Kashida word | الخط |
| English headline | Some at the line, hand in hand |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «وبعضهم عند الخط» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «يداً بيد» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الخط» with kashida (tatweel) for rhythm.
  3. English line «Some at the line, hand in hand» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A closer crop of the packaging-hall team working side by side, hands and shoulders, warm light; no container or label readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وبعضهم عند الخط» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «يداً بيد» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الخط» with kashida (tatweel) for rhythm.
3. English line «Some at the line, hand in hand» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab team standing together, relaxed, proud, wide frame, graded to the emerald palette; or the large team at the booth as an alternate crop.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG

| Element | String |
|---|---|
| Arabic headline 1 | وفي آخر اليوم |
| Arabic headline 2 | فريقٌ واحد |
| Kashida word | آخر |
| English headline | At the end of the day, one team |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «وفي آخر اليوم» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «فريقٌ واحد» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «آخر» with kashida (tatweel) for rhythm.
  3. English line «At the end of the day, one team» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A005: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A048: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab team standing together, relaxed, proud, wide frame, graded to the emerald palette; or the large team at the booth as an alternate crop.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وفي آخر اليوم» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «فريقٌ واحد» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «آخر» with kashida (tatweel) for rhythm.
3. English line «At the end of the day, one team» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, centred two-level Arabic thank-you, thin mint rule, small white line icon, real logo placed by the layout tool. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | شكراً لكل من |
| Arabic headline 2 | يقف في محطته |
| Kashida word | شكراً |
| English headline | Thank you to everyone at their station. |
| Arabic body | أخبرونا: أي جزء من المكان تودّون أن تروه؟ |
| English body | Tell us which part of the place you would like to see. |

**Typography spec:**

  1. Arabic headline line 1 «شكراً لكل من» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «يقف في محطته» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكراً» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «أخبرونا: أي جزء من المكان تودّون أن تروه؟» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Thank you to everyone at their station.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Tell us which part of the place you would like to see.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, centred two-level Arabic thank-you, thin mint rule, small white line icon, real logo placed by the layout tool. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكراً لكل من» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «يقف في محطته» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكراً» with kashida (tatweel) for rhythm.
3. Arabic supporting line «أخبرونا: أي جزء من المكان تودّون أن تروه؟» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Thank you to everyone at their station.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Tell us which part of the place you would like to see.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### NOV-L06 — Why we build here: local industry, in plain words
- **Date:** 2026-11-18  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Local manufacturing
- **Caption (AR):**

> لماذا نبني هنا؟ بكلماتٍ بسيطة: لأنها بلادنا، ولأن ناسنا هنا.
> مدينة سدير للصناعات الدوائية مكانٌ في نجد، وفيه عملٌ يصنعه أهله.
> صنعٌ في المملكة، من سدير.
> قولوا لنا: ما الذي يعنيه لكم أن يُصنع الشيء في بلادكم؟

- **Caption (EN):**

> Why do we build here? In plain words: because it is our country, and our people are here.
> Sudair City is a place in Najd, with work done by its own people.
> Made in the Kingdom, from Sudair.
> Tell us: what does it mean to you when something is made in your own country?

- **Hashtags:** #سدير_للأدوية #SudairPharma #صنع_في_المملكة #MadeInKSA #مدينة_سدير

#### Slide 1/5 — hook
**Treatment:** T7 People hero · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Illustrative Saudi woman and man above the real whole-site drone view filling the lower third; teal dusk sky; headline in the lower band. Keep the top-left corner clear for the logo.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | لماذا نبني هنا؟ |
| Arabic headline 2 | بكلماتٍ بسيطة |
| Kashida word | نبني |
| English headline | Why we build here |
| Arabic body | الصناعة المحلية بكلماتٍ بسيطة. |
| English body | Local industry, in plain words. |

**Typography spec:**

  1. Arabic headline line 1 «لماذا نبني هنا؟» — AE_Sharjah-style heavy geometric kufi, 76 px, #FFFFFF, centred at y=1130.
  2. Arabic headline line 2 «بكلماتٍ بسيطة» — same family, 52 px, mint #8EF0B0, y=1215. Stretch the word «نبني» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الصناعة المحلية بكلماتٍ بسيطة.» — Muna Regular, 40 px, white 90%, centred, y=1315.
  4. English line «Why we build here» — Friz Quadrata Bold / italic condensed sans, 28 px, uppercase, white 90%, tracking +40, y=1280.
  5. English support line «Local industry, in plain words.» — Roboto Light, 24 px, white 80%, y=1326.
  6. Chip «MADE IN THE KINGDOM» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1296.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Illustrative Saudi woman and man above the real whole-site drone view filling the lower third; teal dusk sky; headline in the lower band. Keep the top-left corner clear for the logo.

TREATMENT T7, People hero: People-hero treatment: photoreal portrait of Saudi people (man in white thobe and red-white shemagh, woman in deep green hijab and abaya), arms crossed, proud and calm, looking up and to the right, cinematic light, teal night-sky gradient; below them a real photograph of the landmark or stage fills the lower third.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «لماذا نبني هنا؟» — AE_Sharjah-style heavy geometric kufi, 76 px, #FFFFFF, centred at y=1130.
2. Arabic headline line 2 «بكلماتٍ بسيطة» — same family, 52 px, mint #8EF0B0, y=1215. Stretch the word «نبني» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الصناعة المحلية بكلماتٍ بسيطة.» — Muna Regular, 40 px, white 90%, centred, y=1315.
4. English line «Why we build here» — Friz Quadrata Bold / italic condensed sans, 28 px, uppercase, white 90%, tracking +40, y=1280.
5. English support line «Local industry, in plain words.» — Roboto Light, 24 px, white 80%, y=1326.
6. Chip «MADE IN THE KINGDOM» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1296.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The real drone view of the whole site in the desert, graded emerald and teal, wide and calm, headline over the sky; no people.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | لأنها بلادنا |
| Arabic headline 2 | ونصنع فيها |
| Kashida word | بلادنا |
| English headline | Because it is our country, and we make things here |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «لأنها بلادنا» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «ونصنع فيها» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «بلادنا» with kashida (tatweel) for rhythm.
  3. English line «Because it is our country, and we make things here» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The real drone view of the whole site in the desert, graded emerald and teal, wide and calm, headline over the sky; no people.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «لأنها بلادنا» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «ونصنع فيها» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «بلادنا» with kashida (tatweel) for rhythm.
3. English line «Because it is our country, and we make things here» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Women and men of the packaging hall standing together at the line, wide, teal-green grade; no container or label readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | ولأن ناسنا هنا |
| Arabic headline 2 | وخبراتهم معنا |
| Kashida word | ناسنا |
| English headline | And because our people are here, with their skills |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «ولأن ناسنا هنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «وخبراتهم معنا» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «ناسنا» with kashida (tatweel) for rhythm.
  3. English line «And because our people are here, with their skills» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Women and men of the packaging hall standing together at the line, wide, teal-green grade; no container or label readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ولأن ناسنا هنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «وخبراتهم معنا» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «ناسنا» with kashida (tatweel) for rhythm.
3. English line «And because our people are here, with their skills» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The real palm-lined campus at golden light, calm and wide, headline over the sky; no people.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | صُنع في المملكة |
| Arabic headline 2 | من سدير |
| Kashida word | المملكة |
| English headline | Made in the Kingdom, from Sudair |
| Arabic body | حقيقةٌ بسيطة: المكان هنا، والعمل هنا. |
| English body | A plain fact: the place is here, and the work is here. |

**Typography spec:**

  1. Arabic headline line 1 «صُنع في المملكة» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «من سدير» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «المملكة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «حقيقةٌ بسيطة: المكان هنا، والعمل هنا.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «Made in the Kingdom, from Sudair» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «A plain fact: the place is here, and the work is here.» — Roboto Light, 34 px, white 80%, y=626.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A001: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The real palm-lined campus at golden light, calm and wide, headline over the sky; no people.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صُنع في المملكة» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «من سدير» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «المملكة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «حقيقةٌ بسيطة: المكان هنا، والعمل هنا.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «Made in the Kingdom, from Sudair» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «A plain fact: the place is here, and the work is here.» — Roboto Light, 34 px, white 80%, y=626.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, centred two-level Arabic theme line, thin mint rule, small white line icon; hairline inset frame. No photograph. Real logo placed by the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | صناعة |
| English headline | Visible capability. Measurable impact. |
| Arabic body | ما الذي يعنيه لكم أن يُصنع الشيء في بلادكم؟ |
| English body | What does it mean to you when something is made in your own country? |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «صناعة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «ما الذي يعنيه لكم أن يُصنع الشيء في بلادكم؟» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «What does it mean to you when something is made in your own country?» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, centred two-level Arabic theme line, thin mint rule, small white line icon; hairline inset frame. No photograph. Real logo placed by the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «صناعة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «ما الذي يعنيه لكم أن يُصنع الشيء في بلادكم؟» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «What does it mean to you when something is made in your own country?» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### NOV-F10 — Why people join us
- **Date:** 2026-11-22  |  **Channel:** Instagram + Facebook  |  **Format:** Carousel, 5 slides  |  **Pillar:** People and careers
- **Caption (AR):**

> لا يأتي الناس إلى مكانٍ بسبب جدرانه، بل بسبب من يعمل فيه.
> هذه بعض أسباب انضمام زملائنا إلينا كما نراها.
> وأنتم، ما الذي يجعل مكان العمل بيتًا؟

- **Caption (EN):**

> People do not come to a place for its walls, but for the people who work in it.
> These are some of the reasons our colleagues joined us, as we see them.
> And you: what makes a workplace feel like home?

- **Hashtags:** #سدير_للأدوية #SudairPharma #وظائف #CareersAtSudair #WorkAtSudair

#### Slide 1/5 — hook
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card, deep emerald, two-level headline, small door-ajar line icon in white.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | لماذا ينضمّ الناس |
| Arabic headline 2 | إلى سدير؟ |
| Kashida word | الناس |
| English headline | Why people join Sudair |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «لماذا ينضمّ الناس» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «إلى سدير؟» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «الناس» with kashida (tatweel) for rhythm.
  3. English line «Why people join Sudair» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card, deep emerald, two-level headline, small door-ajar line icon in white.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «لماذا ينضمّ الناس» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «إلى سدير؟» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «الناس» with kashida (tatweel) for rhythm.
3. English line «Why people join Sudair» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real photo of women and men of the packaging hall team at the line, framed to faces and hands, no pack or label readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | ليكونوا في فريقٍ |
| Arabic headline 2 | يعمل معًا |
| Kashida word | فريقٍ |
| English headline | To be part of a team that works together |
| Arabic body | وجوهٌ تتقاسم الطاولة والخط والقاعة. |
| English body | Faces that share the table, the line and the hall. |

**Typography spec:**

  1. Arabic headline line 1 «ليكونوا في فريقٍ» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «يعمل معًا» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «فريقٍ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «وجوهٌ تتقاسم الطاولة والخط والقاعة.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «To be part of a team that works together» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Faces that share the table, the line and the hall.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real photo of women and men of the packaging hall team at the line, framed to faces and hands, no pack or label readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ليكونوا في فريقٍ» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «يعمل معًا» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «فريقٍ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «وجوهٌ تتقاسم الطاولة والخط والقاعة.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «To be part of a team that works together» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Faces that share the table, the line and the hall.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real portrait of the lab analyst at the bench, hands in frame, dark green panel on the right.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | ليتعلّموا من |
| Arabic headline 2 | زميلٍ بجوارهم |
| Kashida word | ليتعلّموا |
| English headline | To learn from the colleague beside them |
| Arabic body | خبرةٌ تنتقل باليد قبل الكلام. |
| English body | Experience that passes from hand to hand before words. |

**Typography spec:**

  1. Arabic headline line 1 «ليتعلّموا من» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «زميلٍ بجوارهم» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «ليتعلّموا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «خبرةٌ تنتقل باليد قبل الكلام.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «To learn from the colleague beside them» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «Experience that passes from hand to hand before words.» — Roboto Light, 26 px, white 80%, y=746.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real portrait of the lab analyst at the bench, hands in frame, dark green panel on the right.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ليتعلّموا من» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «زميلٍ بجوارهم» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «ليتعلّموا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «خبرةٌ تنتقل باليد قبل الكلام.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «To learn from the colleague beside them» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «Experience that passes from hand to hand before words.» — Roboto Light, 26 px, white 80%, y=746.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — proof
**Treatment:** T7 People hero · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A generated Saudi woman and man, calm and proud, above the real drone photo of the whole site in the desert.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | ليعملوا في |
| Arabic headline 2 | صناعةٍ من بلدهم |
| Kashida word | صناعةٍ |
| English headline | To work in industry made at home |
| Arabic body | في مدينة سدير، على أرض المملكة. |
| English body | In Sudair City, on the Kingdom's land. |

**Typography spec:**

  1. Arabic headline line 1 «ليعملوا في» — AE_Sharjah-style heavy geometric kufi, 76 px, #FFFFFF, centred at y=1130.
  2. Arabic headline line 2 «صناعةٍ من بلدهم» — same family, 52 px, mint #8EF0B0, y=1215. Stretch the word «صناعةٍ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «في مدينة سدير، على أرض المملكة.» — Muna Regular, 40 px, white 90%, centred, y=1315.
  4. English line «To work in industry made at home» — Friz Quadrata Bold / italic condensed sans, 28 px, uppercase, white 90%, tracking +40, y=1280.
  5. English support line «In Sudair City, on the Kingdom's land.» — Roboto Light, 24 px, white 80%, y=1326.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A generated Saudi woman and man, calm and proud, above the real drone photo of the whole site in the desert.

TREATMENT T7, People hero: People-hero treatment: photoreal portrait of Saudi people (man in white thobe and red-white shemagh, woman in deep green hijab and abaya), arms crossed, proud and calm, looking up and to the right, cinematic light, teal night-sky gradient; below them a real photograph of the landmark or stage fills the lower third.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ليعملوا في» — AE_Sharjah-style heavy geometric kufi, 76 px, #FFFFFF, centred at y=1130.
2. Arabic headline line 2 «صناعةٍ من بلدهم» — same family, 52 px, mint #8EF0B0, y=1215. Stretch the word «صناعةٍ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «في مدينة سدير، على أرض المملكة.» — Muna Regular, 40 px, white 90%, centred, y=1315.
4. English line «To work in industry made at home» — Friz Quadrata Bold / italic condensed sans, 28 px, uppercase, white 90%, tracking +40, y=1280.
5. English support line «In Sudair City, on the Kingdom's land.» — Roboto Light, 24 px, white 80%, y=1326.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald with the website in a rounded outlined bar and the white logo top-left.

**Assets (root = `Sudair Assets`):**
  - Website slogan collection/Ar slogan.png

| Element | String |
|---|---|
| Arabic headline 1 | بابنا مفتوح |
| Arabic headline 2 | لمن يحبّ العمل بيديه |
| Kashida word | مفتوح |
| English headline | Our door is open |
| Arabic body | تعرّفوا على فريقنا في موقعنا. |
| English body | Meet our team on our website. |

**Typography spec:**

  1. Arabic headline line 1 «بابنا مفتوح» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «لمن يحبّ العمل بيديه» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «مفتوح» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تعرّفوا على فريقنا في موقعنا.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Our door is open» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Meet our team on our website.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «sudairpharma.com» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A129: upload "Sudair Assets/Website slogan collection/Ar slogan.png". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Type card on deep emerald with the website in a rounded outlined bar and the white logo top-left.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «بابنا مفتوح» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «لمن يحبّ العمل بيديه» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «مفتوح» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تعرّفوا على فريقنا في موقعنا.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Our door is open» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Meet our team on our website.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «sudairpharma.com» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### NOV-L07 — Graduates and early careers: what we look for
- **Date:** 2026-11-23  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** People and careers
- **Caption (AR):**

> ماذا نبحث عنه في الخريجين والخريجات؟
> فضولٌ يسأل، وعنايةٌ بالتفاصيل الصغيرة، وروحُ فريقٍ تفرح بنجاح زميلها.
> هذه هي الصفات التي نصغي لها قبل أي شيء.
> تابعوا الصفحة لتعرفوا المزيد عن العمل في سدير.

- **Caption (EN):**

> What do we look for in graduates?
> Curiosity that asks why, care for the small details, and a team spirit that is glad when a colleague succeeds.
> These are the traits we listen for before anything else.
> Follow the page to see more about working at Sudair.

- **Hashtags:** #سدير_للأدوية #SudairPharma #الخريجون #EarlyCareers #SudairCareers

#### Slide 1/5 — hook
**Treatment:** T1 Glass object · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Centred glass-and-brushed-metal compass on glossy emerald floor, mint rim light, soft reflections; no text on the dial. Keep the top-left corner clear for the logo.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | نبحث عن فضولٍ |
| Arabic headline 2 | قبل الخبرة |
| Kashida word | فضولٍ |
| English headline | Curiosity before experience |
| Arabic body | الخريجون وبدايات المسيرة: ما الذي نبحث عنه. |
| English body | Graduates and early careers: what we look for. |

**Typography spec:**

  1. Arabic headline line 1 «نبحث عن فضولٍ» — AE_Sharjah-style heavy geometric kufi, 128 px, #FFFFFF, centred at y=170.
  2. Arabic headline line 2 «قبل الخبرة» — same family, 84 px, mint #8EF0B0, y=320. Stretch the word «فضولٍ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الخريجون وبدايات المسيرة: ما الذي نبحث عنه.» — Muna Regular, 40 px, white 90%, centred, y=420.
  4. English line «Curiosity before experience» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=430.
  5. English support line «Graduates and early careers: what we look for.» — Roboto Light, 28 px, white 80%, y=476.
  6. Chip «EARLY CAREERS» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Centred glass-and-brushed-metal compass on glossy emerald floor, mint rim light, soft reflections; no text on the dial. Keep the top-left corner clear for the logo.

TREATMENT T1, Glass object: Premium 3D render of the hero object, semi-transparent glass and brushed metal, soft studio light from the upper left, mint rim light, clean reflections on a glossy emerald floor, shallow depth of field. Emerald gradient background from #09A45B (top-left glow) to #04301F (bottom-right), faint rounded-diamond lattice at 8% opacity. Hero centred, 55% of tile height, 90 px free space around it.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «نبحث عن فضولٍ» — AE_Sharjah-style heavy geometric kufi, 128 px, #FFFFFF, centred at y=170.
2. Arabic headline line 2 «قبل الخبرة» — same family, 84 px, mint #8EF0B0, y=320. Stretch the word «فضولٍ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الخريجون وبدايات المسيرة: ما الذي نبحث عنه.» — Muna Regular, 40 px, white 90%, centred, y=420.
4. English line «Curiosity before experience» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=430.
5. English support line «Graduates and early careers: what we look for.» — Roboto Light, 28 px, white 80%, y=476.
6. Chip «EARLY CAREERS» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on emerald, centred two-level Arabic headline, the opening word in mint accent, thin mint rule, small white line icon of a question mark in a circle. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | فضولٌ يسأل |
| Arabic headline 2 | ثم يسأل مجدداً |
| Kashida word | فضولٌ |
| English headline | Curiosity |
| Arabic body | تسأل لماذا، ثم تسأل مرةً أخرى. |
| English body | You ask why, then you ask again. |

**Typography spec:**

  1. Arabic headline line 1 «فضولٌ يسأل» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «ثم يسأل مجدداً» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «فضولٌ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تسأل لماذا، ثم تسأل مرةً أخرى.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Curiosity» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «You ask why, then you ask again.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on emerald, centred two-level Arabic headline, the opening word in mint accent, thin mint rule, small white line icon of a question mark in a circle. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «فضولٌ يسأل» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «ثم يسأل مجدداً» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «فضولٌ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تسأل لماذا، ثم تسأل مرةً أخرى.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Curiosity» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «You ask why, then you ask again.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on emerald, centred two-level Arabic headline, thin mint rule, small white line icon of a magnifier. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | عنايةٌ بالتفاصيل |
| Arabic headline 2 | الصغيرة |
| Kashida word | عنايةٌ |
| English headline | Care for the small details |
| Arabic body | تلاحظ ما لا يلاحظه غيرك. |
| English body | You notice what others miss. |

**Typography spec:**

  1. Arabic headline line 1 «عنايةٌ بالتفاصيل» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «الصغيرة» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «عنايةٌ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تلاحظ ما لا يلاحظه غيرك.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Care for the small details» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «You notice what others miss.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on emerald, centred two-level Arabic headline, thin mint rule, small white line icon of a magnifier. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «عنايةٌ بالتفاصيل» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «الصغيرة» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «عنايةٌ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تلاحظ ما لا يلاحظه غيرك.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Care for the small details» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «You notice what others miss.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The large team group at the booth with many women in abayas and ID badges, warm and proud, wide frame, graded to the emerald palette.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG

| Element | String |
|---|---|
| Arabic headline 1 | وروحُ فريق |
| Arabic headline 2 | تفرح بنجاح زميلها |
| Kashida word | فريق |
| English headline | A team spirit, glad when a colleague succeeds |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «وروحُ فريق» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «تفرح بنجاح زميلها» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «فريق» with kashida (tatweel) for rhythm.
  3. English line «A team spirit, glad when a colleague succeeds» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A048: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The large team group at the booth with many women in abayas and ID badges, warm and proud, wide frame, graded to the emerald palette.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وروحُ فريق» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «تفرح بنجاح زميلها» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «فريق» with kashida (tatweel) for rhythm.
3. English line «A team spirit, glad when a colleague succeeds» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, centred two-level Arabic invitation, thin mint rule, small white line icon, real logo placed by the layout tool. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | هذا أنت؟ |
| Arabic headline 2 | نحب أن نعرفك |
| Kashida word | أنت |
| English headline | Is this you? We would like to know you. |
| Arabic body | تابعوا الصفحة لتعرفوا المزيد عن العمل في سدير. |
| English body | Follow the page to see more about working at Sudair. |

**Typography spec:**

  1. Arabic headline line 1 «هذا أنت؟» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «نحب أن نعرفك» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «أنت» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تابعوا الصفحة لتعرفوا المزيد عن العمل في سدير.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Is this you? We would like to know you.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Follow the page to see more about working at Sudair.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, centred two-level Arabic invitation, thin mint rule, small white line icon, real logo placed by the layout tool. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «هذا أنت؟» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «نحب أن نعرفك» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «أنت» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تابعوا الصفحة لتعرفوا المزيد عن العمل في سدير.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Is this you? We would like to know you.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Follow the page to see more about working at Sudair.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### NOV-L08 — Careers: join the line
- **Date:** 2026-11-25  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** People and careers
- **Caption (AR):**

> انضموا إلى صفّنا في سدير للأدوية.
> مكانٌ يتسع لمن يحب التعلّم، وفريقٌ يرحّب بكم، وناسٌ نحب أن تكونوا بينهم.
> من أين تبدؤون؟ من هنا.
> تابعوا الصفحة، وتعرّفوا على الفريق، وقولوا مرحباً.

- **Caption (EN):**

> Join our line at Sudair Pharma.
> A place with room for those who like to learn, a team that welcomes you, and people we would like you to be among.
> Where to start? Here.
> Follow the page, get to know the team, and say hello.

- **Hashtags:** #سدير_للأدوية #SudairPharma #انضموا_إلينا #JoinTheLine #SudairCareers

#### Slide 1/5 — hook
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Wide team photograph of the Sudair team standing in a single row, graded teal-green, golden side light, natural faces. Keep the top-left corner clear for the logo.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG

| Element | String |
|---|---|
| Arabic headline 1 | انضموا إلى صفّنا |
| Arabic headline 2 | في سدير |
| Kashida word | انضموا |
| English headline | Join the line |
| Arabic body | مسيرةٌ مهنية بين الناس. |
| English body | A career among people. |

**Typography spec:**

  1. Arabic headline line 1 «انضموا إلى صفّنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «في سدير» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «انضموا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «مسيرةٌ مهنية بين الناس.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Join the line» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «A career among people.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «CAREERS» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A048: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Wide team photograph of the Sudair team standing in a single row, graded teal-green, golden side light, natural faces. Keep the top-left corner clear for the logo.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «انضموا إلى صفّنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «في سدير» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «انضموا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «مسيرةٌ مهنية بين الناس.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Join the line» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «A career among people.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «CAREERS» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab analyst at the bench, three-quarter view, soft light from the left, dark green panelled wall on the right for text; no label legible.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | مكانٌ يتسع |
| Arabic headline 2 | لمن يحب التعلّم |
| Kashida word | يتسع |
| English headline | A place with room for those who like to learn |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «مكانٌ يتسع» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «لمن يحب التعلّم» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «يتسع» with kashida (tatweel) for rhythm.
  3. English line «A place with room for those who like to learn» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab analyst at the bench, three-quarter view, soft light from the left, dark green panelled wall on the right for text; no label legible.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «مكانٌ يتسع» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «لمن يحب التعلّم» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «يتسع» with kashida (tatweel) for rhythm.
3. English line «A place with room for those who like to learn» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab team standing together, relaxed and welcoming, wide frame, teal-green grade; no label readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4

| Element | String |
|---|---|
| Arabic headline 1 | وفريقٌ يرحّب بك |
| Arabic headline 2 | في كل يوم |
| Kashida word | يرحّب |
| English headline | And a team that welcomes you |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «وفريقٌ يرحّب بك» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «في كل يوم» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «يرحّب» with kashida (tatweel) for rhythm.
  3. English line «And a team that welcomes you» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A005: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab team standing together, relaxed and welcoming, wide frame, teal-green grade; no label readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وفريقٌ يرحّب بك» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «في كل يوم» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «يرحّب» with kashida (tatweel) for rhythm.
3. English line «And a team that welcomes you» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — step
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Three plain, rounded step cards joined by a thin mint line with small glowing nodes, each with a number in a circle, a two-word label and a soft crop of a real photo; emerald background with faint lattice. Labels read: Follow, Meet, Say hello.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG

| Element | String |
|---|---|
| Arabic headline 1 | من أين تبدأ؟ |
| Arabic headline 2 | من هنا |
| Kashida word | تبدأ |
| English headline | Where to start? Here. |
| Arabic body | تابعوا الصفحة، وتعرّفوا على الفريق، وقولوا مرحباً. |
| English body | Follow the page, get to know the team, and say hello. |

**Typography spec:**

  1. Arabic headline line 1 «من أين تبدأ؟» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «من هنا» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «تبدأ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تابعوا الصفحة، وتعرّفوا على الفريق، وقولوا مرحباً.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Where to start? Here.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Follow the page, get to know the team, and say hello.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A005: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A048: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Three plain, rounded step cards joined by a thin mint line with small glowing nodes, each with a number in a circle, a two-word label and a soft crop of a real photo; emerald background with faint lattice. Labels read: Follow, Meet, Say hello.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «من أين تبدأ؟» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «من هنا» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «تبدأ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تابعوا الصفحة، وتعرّفوا على الفريق، وقولوا مرحباً.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Where to start? Here.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Follow the page, get to know the team, and say hello.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, centred two-level Arabic theme line, thin mint rule, small white line icon; hairline inset frame. No photograph. Real logo placed by the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | صناعة |
| English headline | Visible capability. Measurable impact. |
| Arabic body | وخلفها ناسٌ، ونحب أن تكون بينهم. |
| English body | Behind it are people. We would like you among them. |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «صناعة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «وخلفها ناسٌ، ونحب أن تكون بينهم.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Behind it are people. We would like you among them.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, centred two-level Arabic theme line, thin mint rule, small white line icon; hairline inset frame. No photograph. Real logo placed by the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «صناعة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «وخلفها ناسٌ، ونحب أن تكون بينهم.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Behind it are people. We would like you among them.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---


## December 2026

### DEC-L01 — Sudair City in six views
- **Date:** 2026-12-01  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 6 slides  |  **Pillar:** Local manufacturing
- **Caption (AR):**

> مدينة سدير كما تبدو من الأعلى، ثم من طريق الموقع، ثم من الداخل.
> لقطات للمكان الذي نعمل فيه، تتابعونها شريحة بعد شريحة.
> أيّ لقطة أعجبتكم؟ شاركونا رأيكم.

- **Caption (EN):**

> Sudair City, from above, then from the site road, then from inside.
> Six views of the place where we work, one slide at a time.
> Which view stays with you? Tell us.

- **Hashtags:** #سدير_للأدوية #SudairPharma #مدينة_سدير #SudairCity

#### Slide 1/6 — hook
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Key-visual petal frame over the real drone view of the whole site in the desert (A002), the campus and palms (A001) glowing inside one petal. Dusk grade, mint rim light, clear 190 x 190 px area top-left for the logo.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | مدينة سدير |
| Arabic headline 2 | في ست لقطات |
| Kashida word | سدير |
| English headline | Sudair City, in six views |
| Arabic body | من السماء إلى عتبة الباب. |
| English body | From the sky to the doorway. |

**Typography spec:**

  1. Arabic headline line 1 «مدينة سدير» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «في ست لقطات» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «سدير» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «من السماء إلى عتبة الباب.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «Sudair City, in six views» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «From the sky to the doorway.» — Roboto Light, 34 px, white 80%, y=626.
  6. Chip «VIEW 1 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A001: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Key-visual petal frame over the real drone view of the whole site in the desert (A002), the campus and palms (A001) glowing inside one petal. Dusk grade, mint rim light, clear 190 x 190 px area top-left for the logo.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «مدينة سدير» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «في ست لقطات» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «سدير» with kashida (tatweel) for rhythm.
3. Arabic supporting line «من السماء إلى عتبة الباب.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «Sudair City, in six views» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «From the sky to the doorway.» — Roboto Light, 34 px, white 80%, y=626.
6. Chip «VIEW 1 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٦» in small Arabic-Indic digits and 1/6 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/6 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Wide drone view of the palm-lined building and campus in golden light (A001), graded teal-green sky, horizon at 60 percent of the tile, no overlays on the building.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | بين النخيل |
| Arabic headline 2 | في الضوء الذهبي |
| Kashida word | النخيل |
| English headline | Among the palms |
| Arabic body | المبنى والممشى وأشجار النخيل، من الأعلى. |
| English body | The building, the walkway and the palms, from above. |

**Typography spec:**

  1. Arabic headline line 1 «بين النخيل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «في الضوء الذهبي» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «النخيل» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «المبنى والممشى وأشجار النخيل، من الأعلى.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Among the palms» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «The building, the walkway and the palms, from above.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «VIEW 2 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A001: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Wide drone view of the palm-lined building and campus in golden light (A001), graded teal-green sky, horizon at 60 percent of the tile, no overlays on the building.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «بين النخيل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «في الضوء الذهبي» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «النخيل» with kashida (tatweel) for rhythm.
3. Arabic supporting line «المبنى والممشى وأشجار النخيل، من الأعلى.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Among the palms» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «The building, the walkway and the palms, from above.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «VIEW 2 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٦» in small Arabic-Indic digits and 2/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/6 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Leaders walking on the plant road beside the long facade (A030), cropped wide so the facade and the road lead and the figures stay small. Natural grade, teal sky.

**Assets (root = `Sudair Assets`):**
  - News Photos-20261001T081151Z-1-001/News Photos/IMG_1326.JPG

| Element | String |
|---|---|
| Arabic headline 1 | الواجهة |
| Arabic headline 2 | على طريق الموقع |
| Kashida word | الواجهة |
| English headline | The facade, from the site road |
| Arabic body | الطريق الذي يقود إلى المدخل. |
| English body | The road that leads to the entrance. |

**Typography spec:**

  1. Arabic headline line 1 «الواجهة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «على طريق الموقع» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الواجهة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الطريق الذي يقود إلى المدخل.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The facade, from the site road» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «The road that leads to the entrance.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «VIEW 3 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A030: upload "Sudair Assets/News Photos-20261001T081151Z-1-001/News Photos/IMG_1326.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Leaders walking on the plant road beside the long facade (A030), cropped wide so the facade and the road lead and the figures stay small. Natural grade, teal sky.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الواجهة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «على طريق الموقع» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الواجهة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الطريق الذي يقود إلى المدخل.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The facade, from the site road» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «The road that leads to the entrance.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «VIEW 3 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٦» in small Arabic-Indic digits and 3/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/6 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The interior corridor (A003): long, evenly lit, empty, graded to the emerald palette. No text on the walls, no equipment in focus.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | ممرّ في الداخل |
| Arabic headline 2 | هادئ ومُضاء |
| Kashida word | الداخل |
| English headline | A corridor, inside |
| Arabic body | الوجه الآخر للمكان: من الداخل. |
| English body | The other face of the place: the inside. |

**Typography spec:**

  1. Arabic headline line 1 «ممرّ في الداخل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «هادئ ومُضاء» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الداخل» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الوجه الآخر للمكان: من الداخل.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «A corridor, inside» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «The other face of the place: the inside.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «VIEW 4 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A003: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The interior corridor (A003): long, evenly lit, empty, graded to the emerald palette. No text on the walls, no equipment in focus.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ممرّ في الداخل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «هادئ ومُضاء» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الداخل» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الوجه الآخر للمكان: من الداخل.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «A corridor, inside» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «The other face of the place: the inside.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «VIEW 4 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٦» in small Arabic-Indic digits and 4/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/6 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Group standing outside the plant among palms (A041), wide crop so the building and the palms fill most of the frame and the people stay small. Warm light, teal sky.

**Assets (root = `Sudair Assets`):**
  - News Photos-20261001T081151Z-1-001/News Photos/IMG_1337.JPG

| Element | String |
|---|---|
| Arabic headline 1 | عند المدخل |
| Arabic headline 2 | بين النخيل |
| Kashida word | المدخل |
| English headline | At the entrance, among the palms |
| Arabic body | ضيوفٌ يقفون أمام المبنى. |
| English body | Visitors standing in front of the building. |

**Typography spec:**

  1. Arabic headline line 1 «عند المدخل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «بين النخيل» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «المدخل» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «ضيوفٌ يقفون أمام المبنى.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «At the entrance, among the palms» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Visitors standing in front of the building.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «VIEW 5 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A041: upload "Sudair Assets/News Photos-20261001T081151Z-1-001/News Photos/IMG_1337.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Group standing outside the plant among palms (A041), wide crop so the building and the palms fill most of the frame and the people stay small. Warm light, teal sky.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «عند المدخل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «بين النخيل» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «المدخل» with kashida (tatweel) for rhythm.
3. Arabic supporting line «ضيوفٌ يقفون أمام المبنى.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «At the entrance, among the palms» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Visitors standing in front of the building.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «VIEW 5 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٦» in small Arabic-Indic digits and 5/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 6/6 — cta
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The site scale model (A021) cropped close on the model itself, the plant seen as a table-top landscape; officials leaning in are cropped out or softly out of focus. Emerald grade, space at the bottom for the closing line.

**Assets (root = `Sudair Assets`):**
  - News Photos-20261001T081151Z-1-001/News Photos/IMG_1317.JPG

| Element | String |
|---|---|
| Arabic headline 1 | الموقع كلّه |
| Arabic headline 2 | على طاولة |
| Kashida word | الموقع |
| English headline | The whole site, on a table |
| Arabic body | أيّ لقطة أعجبتكم أكثر؟ اكتبوها لنا. صناعة تُرى، وأثر يُقاس. |
| English body | Which view do you like most? Tell us. Visible capability. Measurable impact. |

**Typography spec:**

  1. Arabic headline line 1 «الموقع كلّه» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «على طاولة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الموقع» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «أيّ لقطة أعجبتكم أكثر؟ اكتبوها لنا. صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The whole site, on a table» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Which view do you like most? Tell us. Visible capability. Measurable impact.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «Visible capability. Measurable impact.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A021: upload "Sudair Assets/News Photos-20261001T081151Z-1-001/News Photos/IMG_1317.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The site scale model (A021) cropped close on the model itself, the plant seen as a table-top landscape; officials leaning in are cropped out or softly out of focus. Emerald grade, space at the bottom for the closing line.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الموقع كلّه» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «على طاولة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الموقع» with kashida (tatweel) for rhythm.
3. Arabic supporting line «أيّ لقطة أعجبتكم أكثر؟ اكتبوها لنا. صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The whole site, on a table» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Which view do you like most? Tell us. Visible capability. Measurable impact.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «Visible capability. Measurable impact.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 6 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٦/٦» in small Arabic-Indic digits and 6/6 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### DEC-L02 — Meet the functions: who does what on site
- **Date:** 2026-12-02  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 6 slides  |  **Pillar:** Meet the makers
- **Caption (AR):**

> من يعمل في موقعنا؟ فِرق كثيرة تجتمع في المكان نفسه.
> المختبر، والخط، والتعبئة، والهندسة، والإمداد: لكل فريق مكانه ووجوهه.
> أيّ فريق تحبون أن تتعرّفوا عليه أكثر؟

- **Caption (EN):**

> Who works at our site? Many teams, in the same place.
> The lab, the line, packaging, engineering and logistics: each team has a place and faces.
> Which team would you like to meet?

- **Hashtags:** #سدير_للأدوية #SudairPharma #فريق_سدير #MeetTheTeam

#### Slide 1/6 — hook
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Five rounded cream cards on emerald with a lime-green edge, each with a friendly 3D character in green work clothes and a one-word label: the bench, the line, packaging, engineering, logistics. Cards on a two-column grid, the last full width. Empty area top-left for the logo.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | مَن يعمل |
| Arabic headline 2 | في الموقع؟ |
| Kashida word | يعمل |
| English headline | Who does what on site? |
| Arabic body | فِرق كثيرة، وموقع تجتمع فيه. |
| English body | Different teams, the same place. |

**Typography spec:**

  1. Arabic headline line 1 «مَن يعمل» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «في الموقع؟» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «يعمل» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «فِرق كثيرة، وموقع تجتمع فيه.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Who does what on site?» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  5. English support line «Different teams, the same place.» — Roboto Light, 26 px, white 80%, y=406.
  6. Chip «THE TEAMS · 1 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Five rounded cream cards on emerald with a lime-green edge, each with a friendly 3D character in green work clothes and a one-word label: the bench, the line, packaging, engineering, logistics. Cards on a two-column grid, the last full width. Empty area top-left for the logo.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «مَن يعمل» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «في الموقع؟» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «يعمل» with kashida (tatweel) for rhythm.
3. Arabic supporting line «فِرق كثيرة، وموقع تجتمع فيه.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Who does what on site?» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
5. English support line «Different teams, the same place.» — Roboto Light, 26 px, white 80%, y=406.
6. Chip «THE TEAMS · 1 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٦» in small Arabic-Indic digits and 1/6 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/6 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab analyst at the bench (A007), three-quarter view, calm and focused, soft key light from the left; dark green panel on the right for text. No readable label on any container.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | المختبر |
| Arabic headline 2 | عند الطاولة |
| Kashida word | المختبر |
| English headline | The laboratory |
| Arabic body | فريق المختبر في مكانه، عند الطاولة. |
| English body | The lab team, at the bench. |

**Typography spec:**

  1. Arabic headline line 1 «المختبر» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «عند الطاولة» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «المختبر» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «فريق المختبر في مكانه، عند الطاولة.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «The laboratory» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «The lab team, at the bench.» — Roboto Light, 26 px, white 80%, y=746.
  6. Chip «THE TEAMS · 2 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab analyst at the bench (A007), three-quarter view, calm and focused, soft key light from the left; dark green panel on the right for text. No readable label on any container.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «المختبر» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «عند الطاولة» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «المختبر» with kashida (tatweel) for rhythm.
3. Arabic supporting line «فريق المختبر في مكانه، عند الطاولة.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «The laboratory» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «The lab team, at the bench.» — Roboto Light, 26 px, white 80%, y=746.
6. Chip «THE TEAMS · 2 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٦» in small Arabic-Indic digits and 2/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/6 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Operator in a full suit at the glove port (A011 or A012), cropped to the person and the work position; no readable label, no text. Dark green panel on the right.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الإنتاج |
| Arabic headline 2 | على الخط |
| Kashida word | الإنتاج |
| English headline | Production |
| Arabic body | مشغّلون بزيّهم الكامل في مكان عملهم. |
| English body | Operators in full suits, at their station. |

**Typography spec:**

  1. Arabic headline line 1 «الإنتاج» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «على الخط» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «الإنتاج» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «مشغّلون بزيّهم الكامل في مكان عملهم.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «Production» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «Operators in full suits, at their station.» — Roboto Light, 26 px, white 80%, y=746.
  6. Chip «THE TEAMS · 3 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A012: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A011: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Operator in a full suit at the glove port (A011 or A012), cropped to the person and the work position; no readable label, no text. Dark green panel on the right.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الإنتاج» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «على الخط» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «الإنتاج» with kashida (tatweel) for rhythm.
3. Arabic supporting line «مشغّلون بزيّهم الكامل في مكان عملهم.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «Production» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «Operators in full suits, at their station.» — Roboto Light, 26 px, white 80%, y=746.
6. Chip «THE TEAMS · 3 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٦» in small Arabic-Indic digits and 3/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/6 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The packaging hall with women and men at the line (A013), wide, natural faces, graded to the emerald palette; caption area left clear below.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | التعبئة والتغليف |
| Arabic headline 2 | نساءٌ ورجال |
| Kashida word | التعبئة |
| English headline | Packaging |
| Arabic body | نساء ورجال جنبًا إلى جنب على الخط. |
| English body | Women and men, side by side at the line. |

**Typography spec:**

  1. Arabic headline line 1 «التعبئة والتغليف» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «نساءٌ ورجال» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «التعبئة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «نساء ورجال جنبًا إلى جنب على الخط.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Packaging» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Women and men, side by side at the line.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «THE TEAMS · 4 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The packaging hall with women and men at the line (A013), wide, natural faces, graded to the emerald palette; caption area left clear below.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «التعبئة والتغليف» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «نساءٌ ورجال» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «التعبئة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «نساء ورجال جنبًا إلى جنب على الخط.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Packaging» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Women and men, side by side at the line.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «THE TEAMS · 4 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٦» in small Arabic-Indic digits and 4/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/6 — idea
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Two rounded cream cards with friendly 3D characters in green work clothes: one with a toolbox and hard hat (engineering), one with a trolley and a clipboard (logistics). Illustrated, no text on the objects.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | الهندسة والإمداد |
| Arabic headline 2 | فِرق خلف الكواليس |
| Kashida word | الكواليس |
| English headline | Engineering and logistics |
| Arabic body | الفِرق التي تُبقي الموقع في حركته. |
| English body | The teams behind the scenes who keep the site moving. |

**Typography spec:**

  1. Arabic headline line 1 «الهندسة والإمداد» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «فِرق خلف الكواليس» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «الكواليس» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الفِرق التي تُبقي الموقع في حركته.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Engineering and logistics» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  5. English support line «The teams behind the scenes who keep the site moving.» — Roboto Light, 26 px, white 80%, y=406.
  6. Chip «THE TEAMS · 5 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Two rounded cream cards with friendly 3D characters in green work clothes: one with a toolbox and hard hat (engineering), one with a trolley and a clipboard (logistics). Illustrated, no text on the objects.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الهندسة والإمداد» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «فِرق خلف الكواليس» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «الكواليس» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الفِرق التي تُبقي الموقع في حركته.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Engineering and logistics» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
5. English support line «The teams behind the scenes who keep the site moving.» — Roboto Light, 26 px, white 80%, y=406.
6. Chip «THE TEAMS · 5 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٦» in small Arabic-Indic digits and 5/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 6/6 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, two-level Arabic headline, thin mint rule, one small line icon of a group of people. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | فريقًا بعد فريق |
| Arabic headline 2 | نعرّفكم بالناس |
| Kashida word | فريقًا |
| English headline | Team by team, we introduce the people |
| Arabic body | أيّ فريق تحبون أن تتعرّفوا عليه أكثر؟ اكتبوه لنا. |
| English body | Which team would you like to meet? Tell us. |

**Typography spec:**

  1. Arabic headline line 1 «فريقًا بعد فريق» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «نعرّفكم بالناس» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «فريقًا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «أيّ فريق تحبون أن تتعرّفوا عليه أكثر؟ اكتبوه لنا.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Team by team, we introduce the people» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Which team would you like to meet? Tell us.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Visible capability. Measurable impact.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, two-level Arabic headline, thin mint rule, one small line icon of a group of people. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «فريقًا بعد فريق» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «نعرّفكم بالناس» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «فريقًا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «أيّ فريق تحبون أن تتعرّفوا عليه أكثر؟ اكتبوه لنا.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Team by team, we introduce the people» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Which team would you like to meet? Tell us.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Visible capability. Measurable impact.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 6 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٦/٦» in small Arabic-Indic digits and 6/6 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### DEC-L03 — The year in review: what we showed you
- **Date:** 2026-12-07  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Year and community
- **Caption (AR):**

> عام 2026 كما رأيتموه: المكان من الأعلى، والناس عند عملهم، والمنصّات التي وقفنا عليها.
> شكرًا لكل من تابعنا وتفاعل معنا على مدار العام.
> ما اللقطة التي بقيت في ذاكرتكم؟

- **Caption (EN):**

> 2026 as you saw it: the place from above, the people at work, the stages we stood on.
> Thank you to everyone who followed and engaged with us through the year.
> Which moment stayed with you?

- **Hashtags:** #سدير_للأدوية #SudairPharma #حصاد_2026 #YearInReview

#### Slide 1/5 — hook
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Wide documentary photograph of the team standing in a single row at the booth (A048), graded teal-green, natural faces, ID badges softened. Clear area top-left for the logo.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG

| Element | String |
|---|---|
| Arabic headline 1 | عامنا 2026 |
| Arabic headline 2 | كما رأيتموه |
| Kashida word | عامنا |
| English headline | 2026, as you saw it |
| Arabic body | المكان، والناس، والمنصّات. |
| English body | The place, the people, the stages. |

**Typography spec:**

  1. Arabic headline line 1 «عامنا 2026» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «كما رأيتموه» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «عامنا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «المكان، والناس، والمنصّات.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «2026, as you saw it» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «The place, the people, the stages.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «THE YEAR · 1 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A048: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Wide documentary photograph of the team standing in a single row at the booth (A048), graded teal-green, natural faces, ID badges softened. Clear area top-left for the logo.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «عامنا 2026» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «كما رأيتموه» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «عامنا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «المكان، والناس، والمنصّات.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «2026, as you saw it» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «The place, the people, the stages.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «THE YEAR · 1 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Key-visual petal frame: three glowing petal windows over the real drone view of the whole site (A002). Dusk grade, no people.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | رأيتم المكان |
| Arabic headline 2 | من الأعلى |
| Kashida word | المكان |
| English headline | You saw the place |
| Arabic body | من الأعلى، ومن الطريق، ومن الداخل. |
| English body | From above, from the road, from inside. |

**Typography spec:**

  1. Arabic headline line 1 «رأيتم المكان» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «من الأعلى» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «المكان» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «من الأعلى، ومن الطريق، ومن الداخل.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «You saw the place» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «From above, from the road, from inside.» — Roboto Light, 34 px, white 80%, y=626.
  6. Chip «THE YEAR · 2 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Key-visual petal frame: three glowing petal windows over the real drone view of the whole site (A002). Dusk grade, no people.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «رأيتم المكان» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «من الأعلى» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «المكان» with kashida (tatweel) for rhythm.
3. Arabic supporting line «من الأعلى، ومن الطريق، ومن الداخل.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «You saw the place» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «From above, from the road, from inside.» — Roboto Light, 34 px, white 80%, y=626.
6. Chip «THE YEAR · 2 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab analyst at the bench (A007), three-quarter view, dark green panel on the right for text. No readable label on any container.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | رأيتم الناس |
| Arabic headline 2 | عند عملهم |
| Kashida word | الناس |
| English headline | You met the people |
| Arabic body | عند الطاولة، وعلى الخط، وفي قاعة التعبئة. |
| English body | At the bench, on the line, in the packaging hall. |

**Typography spec:**

  1. Arabic headline line 1 «رأيتم الناس» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «عند عملهم» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «الناس» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «عند الطاولة، وعلى الخط، وفي قاعة التعبئة.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «You met the people» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «At the bench, on the line, in the packaging hall.» — Roboto Light, 26 px, white 80%, y=746.
  6. Chip «THE YEAR · 3 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab analyst at the bench (A007), three-quarter view, dark green panel on the right for text. No readable label on any container.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «رأيتم الناس» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «عند عملهم» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «الناس» with kashida (tatweel) for rhythm.
3. Arabic supporting line «عند الطاولة، وعلى الخط، وفي قاعة التعبئة.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «You met the people» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «At the bench, on the line, in the packaging hall.» — Roboto Light, 26 px, white 80%, y=746.
6. Chip «THE YEAR · 3 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T5 Speaker or event · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The booth architecture with the SPC logo wall (A082), no people in frame, wide, graded to the emerald palette. A small label row reads: exhibitions and booths.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/مشاركة CPHI ME 2024/sudair-pharma-cphi-2025-booth.JPG

| Element | String |
|---|---|
| Arabic headline 1 | ورأيتمونا |
| Arabic headline 2 | في المعارض |
| Kashida word | المعارض |
| English headline | You saw us at the shows |
| Arabic body | منصّات وأجنحة شاركناها معكم في حينها. |
| English body | Stages and booths we shared with you at the time. |

**Typography spec:**

  1. Arabic headline line 1 «ورأيتمونا» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «في المعارض» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «المعارض» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «منصّات وأجنحة شاركناها معكم في حينها.» — Muna Regular, 40 px, white 90%, centred, y=380.
  4. English line «You saw us at the shows» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
  5. English support line «Stages and booths we shared with you at the time.» — Roboto Light, 28 px, white 80%, y=426.
  6. Chip «THE YEAR · 4 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A082: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/مشاركة CPHI ME 2024/sudair-pharma-cphi-2025-booth.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The booth architecture with the SPC logo wall (A082), no people in frame, wide, graded to the emerald palette. A small label row reads: exhibitions and booths.

TREATMENT T5, Speaker or event: Event card treatment: black-and-white head-and-shoulders portraits or one event photograph with a diagonal lime corner accent, emerald background with a faint large SPC logotype behind, calendar icon with date, location pin with city, a rounded outlined bar for the contact line.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ورأيتمونا» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «في المعارض» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «المعارض» with kashida (tatweel) for rhythm.
3. Arabic supporting line «منصّات وأجنحة شاركناها معكم في حينها.» — Muna Regular, 40 px, white 90%, centred, y=380.
4. English line «You saw us at the shows» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
5. English support line «Stages and booths we shared with you at the time.» — Roboto Light, 28 px, white 80%, y=426.
6. Chip «THE YEAR · 4 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, centred two-level Arabic headline, thin mint rule, one small line icon of a palm. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | شكرًا |
| Arabic headline 2 | لأنكم كنتم هناك |
| Kashida word | شكرًا |
| English headline | Thank you for being there |
| Arabic body | شكرًا لكل من تابعنا وشاركنا. صناعة تُرى، وأثر يُقاس. |
| English body | Thank you to everyone who followed and shared. Visible capability. Measurable impact. |

**Typography spec:**

  1. Arabic headline line 1 «شكرًا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «لأنكم كنتم هناك» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكرًا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «شكرًا لكل من تابعنا وشاركنا. صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Thank you for being there» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Thank you to everyone who followed and shared. Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Visible capability. Measurable impact.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, centred two-level Arabic headline, thin mint rule, one small line icon of a palm. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكرًا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «لأنكم كنتم هناك» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكرًا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «شكرًا لكل من تابعنا وشاركنا. صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Thank you for being there» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Thank you to everyone who followed and shared. Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Visible capability. Measurable impact.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### DEC-F04 — The year, in frames
- **Date:** 2026-12-08  |  **Channel:** Instagram + Facebook  |  **Format:** Carousel, 5 slides  |  **Pillar:** Year and community
- **Caption (AR):**

> عامنا في لقطات: المكان، والوجوه، والتفاصيل.
> مرّروا لتروا كيف رأينا عام 2026 معكم.
> أيّ لقطةٍ بقيت في ذاكرتكم؟

- **Caption (EN):**

> Our year, in frames: the place, the faces, the details.
> Swipe to see how we saw 2026 with you.
> Which frame stays with you?

- **Hashtags:** #سدير_للأدوية #SudairPharma #عام_2026 #YearInReview

#### Slide 1/5 — hook
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Deep emerald type card, hairline frame, thin mint rule, small white palm-burst icon; centred two-level headline.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | عامنا |
| Arabic headline 2 | في لقطات |
| Kashida word | عامنا |
| English headline | Our year, in frames. |
| Arabic body | 2026 كما رأيناه معكم. |
| English body | 2026, as we saw it with you. |

**Typography spec:**

  1. Arabic headline line 1 «عامنا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «في لقطات» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «عامنا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «2026 كما رأيناه معكم.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Our year, in frames.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «2026, as we saw it with you.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Deep emerald type card, hairline frame, thin mint rule, small white palm-burst icon; centred two-level headline.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «عامنا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «في لقطات» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «عامنا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «2026 كما رأيناه معكم.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Our year, in frames.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «2026, as we saw it with you.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Full-bleed real drone frame of the whole site in the desert (A002), teal-green grade, wide and calm.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | المكان |
| Arabic headline 2 | من الأعلى |
| Kashida word | المكان |
| English headline | The place. |
| Arabic body | مدينة سدير، حيث نعمل. |
| English body | Sudair City, where we work. |

**Typography spec:**

  1. Arabic headline line 1 «المكان» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «من الأعلى» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «المكان» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «مدينة سدير، حيث نعمل.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The place.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Sudair City, where we work.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Full-bleed real drone frame of the whole site in the desert (A002), teal-green grade, wide and calm.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «المكان» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «من الأعلى» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «المكان» with kashida (tatweel) for rhythm.
3. Arabic supporting line «مدينة سدير، حيث نعمل.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The place.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Sudair City, where we work.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real frame of the lab team standing together in the lab (A005), teal-green grade, natural faces.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الوجوه |
| Arabic headline 2 | خلف العمل |
| Kashida word | الوجوه |
| English headline | The faces. |
| Arabic body | فِرقٌ تلتقي كل صباح. |
| English body | Teams who meet every morning. |

**Typography spec:**

  1. Arabic headline line 1 «الوجوه» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «خلف العمل» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الوجوه» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «فِرقٌ تلتقي كل صباح.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The faces.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Teams who meet every morning.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A005: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real frame of the lab team standing together in the lab (A005), teal-green grade, natural faces.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الوجوه» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «خلف العمل» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الوجوه» with kashida (tatweel) for rhythm.
3. Arabic supporting line «فِرقٌ تلتقي كل صباح.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The faces.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Teams who meet every morning.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Close real frame of a gloved hand beside a row of glassware (A009), no readable label, soft emerald light.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4

| Element | String |
|---|---|
| Arabic headline 1 | التفاصيل |
| Arabic headline 2 | عن قرب |
| Kashida word | التفاصيل |
| English headline | The details. |
| Arabic body | يدٌ وزجاجٌ وضوء. |
| English body | A hand, glass and light. |

**Typography spec:**

  1. Arabic headline line 1 «التفاصيل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «عن قرب» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «التفاصيل» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يدٌ وزجاجٌ وضوء.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The details.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «A hand, glass and light.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A009: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Close real frame of a gloved hand beside a row of glassware (A009), no readable label, soft emerald light.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «التفاصيل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «عن قرب» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «التفاصيل» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يدٌ وزجاجٌ وضوء.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The details.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «A hand, glass and light.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Deep emerald type card with hairline frame, mint rule and the theme line; logo bottom-left.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | شكرًا |
| Arabic headline 2 | لأنكم رافقتمونا |
| Kashida word | شكرًا |
| English headline | Thank you for being with us. |
| Arabic body | صناعة تُرى، وأثر يُقاس. |
| English body | Visible capability. Measurable impact. |

**Typography spec:**

  1. Arabic headline line 1 «شكرًا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «لأنكم رافقتمونا» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكرًا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Thank you for being with us.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Tell us your favourite frame in the comments.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Deep emerald type card with hairline frame, mint rule and the theme line; logo bottom-left.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكرًا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «لأنكم رافقتمونا» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكرًا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Thank you for being with us.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Tell us your favourite frame in the comments.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### DEC-L04 — Events and partnerships of 2026: the stages we shared with you
- **Date:** 2026-12-09  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 6 slides  |  **Pillar:** Recognition and events
- **Caption (AR):**

> المنصّات التي وقفنا عليها هذا العام: معارض، وتوقيعات، وشراكات مع الجامعات.
> شكرًا لكل شريك وقف معنا على تلك المنصّات.
> تابعونا لنكمل القصة معكم.

- **Caption (EN):**

> The stages we stood on this year: exhibitions, signings and partnerships with universities.
> Thank you to every partner who stood with us on them.
> Follow along as the story continues.

- **Hashtags:** #سدير_للأدوية #SudairPharma #شراكات #Partnerships2026

#### Slide 1/6 — hook
**Treatment:** T5 Speaker or event · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Booth architecture with the SPC logo wall (A082), no people, wide; three small outlined pill labels under it with exhibition names only. Clear logo area top-left.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/مشاركة CPHI ME 2024/sudair-pharma-cphi-2025-booth.JPG

| Element | String |
|---|---|
| Arabic headline 1 | محطّات العام |
| Arabic headline 2 | ومَن شاركنا فيها |
| Kashida word | محطّات |
| English headline | Events and partnerships of 2026 |
| Arabic body | المنصّات التي شاركناها معكم. |
| English body | The stages we shared with you. |

**Typography spec:**

  1. Arabic headline line 1 «محطّات العام» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «ومَن شاركنا فيها» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «محطّات» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «المنصّات التي شاركناها معكم.» — Muna Regular, 40 px, white 90%, centred, y=380.
  4. English line «Events and partnerships of 2026» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
  5. English support line «The stages we shared with you.» — Roboto Light, 28 px, white 80%, y=426.
  6. Chip «EVENTS · 1 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A082: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/مشاركة CPHI ME 2024/sudair-pharma-cphi-2025-booth.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Booth architecture with the SPC logo wall (A082), no people, wide; three small outlined pill labels under it with exhibition names only. Clear logo area top-left.

TREATMENT T5, Speaker or event: Event card treatment: black-and-white head-and-shoulders portraits or one event photograph with a diagonal lime corner accent, emerald background with a faint large SPC logotype behind, calendar icon with date, location pin with city, a rounded outlined bar for the contact line.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «محطّات العام» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «ومَن شاركنا فيها» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «محطّات» with kashida (tatweel) for rhythm.
3. Arabic supporting line «المنصّات التي شاركناها معكم.» — Muna Regular, 40 px, white 90%, centred, y=380.
4. English line «Events and partnerships of 2026» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
5. English support line «The stages we shared with you.» — Roboto Light, 28 px, white 80%, y=426.
6. Chip «EVENTS · 1 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٦» in small Arabic-Indic digits and 1/6 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/6 — idea
**Treatment:** T5 Speaker or event · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Strategic agreement signing on stage at the Global Health Exhibition (A054), the host signage visible and smaller than the Sudair mark; crop so faces are not the focus, emerald frame.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-strategic-agreement-global-health-2025.JPG

| Element | String |
|---|---|
| Arabic headline 1 | معرض الصحة |
| Arabic headline 2 | العالمي |
| Kashida word | العالمي |
| English headline | Global Health Exhibition |
| Arabic body | توقيع اتفاقية على المنصّة، كما نُشر في حينه. |
| English body | An agreement signing on stage, as published at the time. |

**Typography spec:**

  1. Arabic headline line 1 «معرض الصحة» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «العالمي» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «العالمي» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «توقيع اتفاقية على المنصّة، كما نُشر في حينه.» — Muna Regular, 40 px, white 90%, centred, y=380.
  4. English line «Global Health Exhibition» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
  5. English support line «An agreement signing on stage, as published at the time.» — Roboto Light, 28 px, white 80%, y=426.
  6. Chip «EVENTS · 2 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A054: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-strategic-agreement-global-health-2025.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Strategic agreement signing on stage at the Global Health Exhibition (A054), the host signage visible and smaller than the Sudair mark; crop so faces are not the focus, emerald frame.

TREATMENT T5, Speaker or event: Event card treatment: black-and-white head-and-shoulders portraits or one event photograph with a diagonal lime corner accent, emerald background with a faint large SPC logotype behind, calendar icon with date, location pin with city, a rounded outlined bar for the contact line.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «معرض الصحة» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «العالمي» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «العالمي» with kashida (tatweel) for rhythm.
3. Arabic supporting line «توقيع اتفاقية على المنصّة، كما نُشر في حينه.» — Muna Regular, 40 px, white 90%, centred, y=380.
4. English line «Global Health Exhibition» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
5. English support line «An agreement signing on stage, as published at the time.» — Roboto Light, 28 px, white 80%, y=426.
6. Chip «EVENTS · 2 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٦» in small Arabic-Indic digits and 2/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/6 — idea
**Treatment:** T5 Speaker or event · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The agreement signing stage at CPHI Middle East (A097), wide, host signage smaller than the Sudair mark, emerald frame.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/مشاركة CPHI ME 2024/sudair-pharma-nupco-agreement-cphi-2025.JPG

| Element | String |
|---|---|
| Arabic headline 1 | معرض CPHI |
| Arabic headline 2 | الشرق الأوسط |
| Kashida word | معرض |
| English headline | CPHI Middle East |
| Arabic body | اتفاقيات ولقاءات في الجناح. |
| English body | Signings and conversations at the booth. |

**Typography spec:**

  1. Arabic headline line 1 «معرض CPHI» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «الشرق الأوسط» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «معرض» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «اتفاقيات ولقاءات في الجناح.» — Muna Regular, 40 px, white 90%, centred, y=380.
  4. English line «CPHI Middle East» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
  5. English support line «Signings and conversations at the booth.» — Roboto Light, 28 px, white 80%, y=426.
  6. Chip «EVENTS · 3 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A097: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/مشاركة CPHI ME 2024/sudair-pharma-nupco-agreement-cphi-2025.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The agreement signing stage at CPHI Middle East (A097), wide, host signage smaller than the Sudair mark, emerald frame.

TREATMENT T5, Speaker or event: Event card treatment: black-and-white head-and-shoulders portraits or one event photograph with a diagonal lime corner accent, emerald background with a faint large SPC logotype behind, calendar icon with date, location pin with city, a rounded outlined bar for the contact line.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «معرض CPHI» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «الشرق الأوسط» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «معرض» with kashida (tatweel) for rhythm.
3. Arabic supporting line «اتفاقيات ولقاءات في الجناح.» — Muna Regular, 40 px, white 90%, centred, y=380.
4. English line «CPHI Middle East» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
5. English support line «Signings and conversations at the booth.» — Roboto Light, 28 px, white 80%, y=426.
6. Chip «EVENTS · 3 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٦» in small Arabic-Indic digits and 3/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/6 — idea
**Treatment:** T5 Speaker or event · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The Sudair booth at the Saudi Made exhibition with the SPC logo and visitors (A109), wide, emerald frame.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/معرض صنع في السعودية/sudair-pharma-saudi-made-2025-booth.JPG

| Element | String |
|---|---|
| Arabic headline 1 | معرض صُنع |
| Arabic headline 2 | في السعودية |
| Kashida word | السعودية |
| English headline | Made in Saudi |
| Arabic body | جناحنا بين الصناعات السعودية. |
| English body | Our booth among Saudi-made industry. |

**Typography spec:**

  1. Arabic headline line 1 «معرض صُنع» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «في السعودية» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «السعودية» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «جناحنا بين الصناعات السعودية.» — Muna Regular, 40 px, white 90%, centred, y=380.
  4. English line «Made in Saudi» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
  5. English support line «Our booth among Saudi-made industry.» — Roboto Light, 28 px, white 80%, y=426.
  6. Chip «EVENTS · 4 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A109: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/معرض صنع في السعودية/sudair-pharma-saudi-made-2025-booth.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The Sudair booth at the Saudi Made exhibition with the SPC logo and visitors (A109), wide, emerald frame.

TREATMENT T5, Speaker or event: Event card treatment: black-and-white head-and-shoulders portraits or one event photograph with a diagonal lime corner accent, emerald background with a faint large SPC logotype behind, calendar icon with date, location pin with city, a rounded outlined bar for the contact line.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «معرض صُنع» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «في السعودية» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «السعودية» with kashida (tatweel) for rhythm.
3. Arabic supporting line «جناحنا بين الصناعات السعودية.» — Muna Regular, 40 px, white 90%, centred, y=380.
4. English line «Made in Saudi» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
5. English support line «Our booth among Saudi-made industry.» — Roboto Light, 28 px, white 80%, y=426.
6. Chip «EVENTS · 4 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٦» in small Arabic-Indic digits and 4/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/6 — idea
**Treatment:** T5 Speaker or event · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Memorandum signing with a university at the Saudi Made stage (A113), cropped to the table and the folders, emerald frame.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/معرض صنع في السعودية/sudair-pharma-taiba-university-mou-saudi-made-2025.JPG

| Element | String |
|---|---|
| Arabic headline 1 | شراكات |
| Arabic headline 2 | مع الجامعات |
| Kashida word | شراكات |
| English headline | Partnerships with universities |
| Arabic body | توقيع مذكرات تفاهم مع شركاء أكاديميين، كما نُشر. |
| English body | Memoranda signed with academic partners, as published. |

**Typography spec:**

  1. Arabic headline line 1 «شراكات» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «مع الجامعات» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «شراكات» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «توقيع مذكرات تفاهم مع شركاء أكاديميين، كما نُشر.» — Muna Regular, 40 px, white 90%, centred, y=380.
  4. English line «Partnerships with universities» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
  5. English support line «Memoranda signed with academic partners, as published.» — Roboto Light, 28 px, white 80%, y=426.
  6. Chip «EVENTS · 5 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A113: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/معرض صنع في السعودية/sudair-pharma-taiba-university-mou-saudi-made-2025.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Memorandum signing with a university at the Saudi Made stage (A113), cropped to the table and the folders, emerald frame.

TREATMENT T5, Speaker or event: Event card treatment: black-and-white head-and-shoulders portraits or one event photograph with a diagonal lime corner accent, emerald background with a faint large SPC logotype behind, calendar icon with date, location pin with city, a rounded outlined bar for the contact line.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شراكات» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «مع الجامعات» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «شراكات» with kashida (tatweel) for rhythm.
3. Arabic supporting line «توقيع مذكرات تفاهم مع شركاء أكاديميين، كما نُشر.» — Muna Regular, 40 px, white 90%, centred, y=380.
4. English line «Partnerships with universities» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
5. English support line «Memoranda signed with academic partners, as published.» — Roboto Light, 28 px, white 80%, y=426.
6. Chip «EVENTS · 5 OF 6» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٦» in small Arabic-Indic digits and 5/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 6/6 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, two-level Arabic headline, thin mint rule, one small line icon of two hands meeting. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | شكرًا لشركائنا |
| Arabic headline 2 | على الطريق المشترك |
| Kashida word | شركائنا |
| English headline | Thank you to our partners |
| Arabic body | شكرًا لكل من وقف معنا على هذه المنصّات. تابعونا لنكمل القصة. |
| English body | Thank you to everyone who stood with us on these stages. Follow along. |

**Typography spec:**

  1. Arabic headline line 1 «شكرًا لشركائنا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «على الطريق المشترك» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شركائنا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «شكرًا لكل من وقف معنا على هذه المنصّات. تابعونا لنكمل القصة.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Thank you to our partners» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Thank you to everyone who stood with us on these stages. Follow along.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, two-level Arabic headline, thin mint rule, one small line icon of two hands meeting. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكرًا لشركائنا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «على الطريق المشترك» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شركائنا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «شكرًا لكل من وقف معنا على هذه المنصّات. تابعونا لنكمل القصة.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Thank you to our partners» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Thank you to everyone who stood with us on these stages. Follow along.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 6 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٦/٦» in small Arabic-Indic digits and 6/6 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### DEC-L05 — Local industry in plain words
- **Date:** 2026-12-14  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Local manufacturing
- **Caption (AR):**

> صُنع هنا، في المملكة. ماذا يعني ذلك لنا؟
> الموقع هنا، والناس هنا، والعمل يُنجَز هنا.
> ماذا يعني لكم «صُنع في المملكة»؟

- **Caption (EN):**

> Made here, in the Kingdom. What does that mean to us?
> The place is here, the people are here, the work is done here.
> What does 'made in the Kingdom' mean to you?

- **Hashtags:** #سدير_للأدوية #SudairPharma #صنع_في_السعودية #MadeInSaudi

#### Slide 1/5 — hook
**Treatment:** T7 People hero · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Illustrated Saudi woman and man above the real drone view of the whole site (A002), night sky with teal gradient, mint rim light; headline area above the site photo. Clear 190 x 190 px area top-left.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | صُنع هنا |
| Arabic headline 2 | في المملكة |
| Kashida word | هنا |
| English headline | Made here, in the Kingdom |
| Arabic body | الصناعة المحلية، بكلمات بسيطة. |
| English body | Local industry, in plain words. |

**Typography spec:**

  1. Arabic headline line 1 «صُنع هنا» — AE_Sharjah-style heavy geometric kufi, 76 px, #FFFFFF, centred at y=1130.
  2. Arabic headline line 2 «في المملكة» — same family, 52 px, mint #8EF0B0, y=1215. Stretch the word «هنا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الصناعة المحلية، بكلمات بسيطة.» — Muna Regular, 40 px, white 90%, centred, y=1315.
  4. English line «Made here, in the Kingdom» — Friz Quadrata Bold / italic condensed sans, 28 px, uppercase, white 90%, tracking +40, y=1280.
  5. English support line «Local industry, in plain words.» — Roboto Light, 24 px, white 80%, y=1326.
  6. Chip «MADE HERE · 1 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1296.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Illustrated Saudi woman and man above the real drone view of the whole site (A002), night sky with teal gradient, mint rim light; headline area above the site photo. Clear 190 x 190 px area top-left.

TREATMENT T7, People hero: People-hero treatment: photoreal portrait of Saudi people (man in white thobe and red-white shemagh, woman in deep green hijab and abaya), arms crossed, proud and calm, looking up and to the right, cinematic light, teal night-sky gradient; below them a real photograph of the landmark or stage fills the lower third.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صُنع هنا» — AE_Sharjah-style heavy geometric kufi, 76 px, #FFFFFF, centred at y=1130.
2. Arabic headline line 2 «في المملكة» — same family, 52 px, mint #8EF0B0, y=1215. Stretch the word «هنا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الصناعة المحلية، بكلمات بسيطة.» — Muna Regular, 40 px, white 90%, centred, y=1315.
4. English line «Made here, in the Kingdom» — Friz Quadrata Bold / italic condensed sans, 28 px, uppercase, white 90%, tracking +40, y=1280.
5. English support line «Local industry, in plain words.» — Roboto Light, 24 px, white 80%, y=1326.
6. Chip «MADE HERE · 1 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1296.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Key-visual petal frame with the real drone view of the site (A002) in the central petal, dusk grade, no people.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | الموقع هنا |
| Arabic headline 2 | في سدير، نجد |
| Kashida word | الموقع |
| English headline | The place is here |
| Arabic body | مدينة سدير في منطقة نجد، في قلب المملكة. |
| English body | Sudair City is in the Najd region of the Kingdom. |

**Typography spec:**

  1. Arabic headline line 1 «الموقع هنا» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «في سدير، نجد» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «الموقع» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «مدينة سدير في منطقة نجد، في قلب المملكة.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «The place is here» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «Sudair City is in the Najd region of the Kingdom.» — Roboto Light, 34 px, white 80%, y=626.
  6. Chip «MADE HERE · 2 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Key-visual petal frame with the real drone view of the site (A002) in the central petal, dusk grade, no people.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الموقع هنا» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «في سدير، نجد» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «الموقع» with kashida (tatweel) for rhythm.
3. Arabic supporting line «مدينة سدير في منطقة نجد، في قلب المملكة.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «The place is here» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «Sudair City is in the Najd region of the Kingdom.» — Roboto Light, 34 px, white 80%, y=626.
6. Chip «MADE HERE · 2 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Women and men of the packaging hall at the line (A013), wide, natural faces, graded to the emerald palette.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الناس هنا |
| Arabic headline 2 | نساءٌ ورجال |
| Kashida word | الناس |
| English headline | The people are here |
| Arabic body | نساء ورجال يعملون في قاعة التعبئة. |
| English body | Women and men at work in the packaging hall. |

**Typography spec:**

  1. Arabic headline line 1 «الناس هنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «نساءٌ ورجال» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الناس» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «نساء ورجال يعملون في قاعة التعبئة.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The people are here» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Women and men at work in the packaging hall.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «MADE HERE · 3 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Women and men of the packaging hall at the line (A013), wide, natural faces, graded to the emerald palette.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الناس هنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «نساءٌ ورجال» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الناس» with kashida (tatweel) for rhythm.
3. Arabic supporting line «نساء ورجال يعملون في قاعة التعبئة.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The people are here» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Women and men at work in the packaging hall.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «MADE HERE · 3 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Close crop of a gloved hand beside a row of flasks (A009), no label legible, shallow depth, emerald grade.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4

| Element | String |
|---|---|
| Arabic headline 1 | والعمل يُنجَز هنا |
| Arabic headline 2 | بأيدي الفريق |
| Kashida word | العمل |
| English headline | The work is done here |
| Arabic body | يدٌ بقفّاز، وصفٌّ من الأدوات، ويومُ عمل. |
| English body | A gloved hand, a row of glassware, a day's work. |

**Typography spec:**

  1. Arabic headline line 1 «والعمل يُنجَز هنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «بأيدي الفريق» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «العمل» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يدٌ بقفّاز، وصفٌّ من الأدوات، ويومُ عمل.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The work is done here» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «A gloved hand, a row of glassware, a day's work.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «MADE HERE · 4 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A009: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Close crop of a gloved hand beside a row of flasks (A009), no label legible, shallow depth, emerald grade.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «والعمل يُنجَز هنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «بأيدي الفريق» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «العمل» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يدٌ بقفّاز، وصفٌّ من الأدوات، ويومُ عمل.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The work is done here» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «A gloved hand, a row of glassware, a day's work.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «MADE HERE · 4 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, two-level Arabic headline, thin mint rule, one small line icon of a palm. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | هذا ما نعنيه |
| Arabic headline 2 | بصناعة محلية |
| Kashida word | نعنيه |
| English headline | That is what local industry means to us |
| Arabic body | المكان هنا، والناس هنا، والعمل هنا. ماذا يعني لكم «صُنع في المملكة»؟ |
| English body | The place is here, the people are here, the work is here. What does 'made in the Kingdom' mean to you? |

**Typography spec:**

  1. Arabic headline line 1 «هذا ما نعنيه» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «بصناعة محلية» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «نعنيه» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «المكان هنا، والناس هنا، والعمل هنا. ماذا يعني لكم «صُنع في المملكة»؟» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «That is what local industry means to us» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «The place is here, the people are here, the work is here. What does 'made in the Kingdom' mean to you?» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR CITY · NAJD» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, two-level Arabic headline, thin mint rule, one small line icon of a palm. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «هذا ما نعنيه» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «بصناعة محلية» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «نعنيه» with kashida (tatweel) for rhythm.
3. Arabic supporting line «المكان هنا، والناس هنا، والعمل هنا. ماذا يعني لكم «صُنع في المملكة»؟» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «That is what local industry means to us» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «The place is here, the people are here, the work is here. What does 'made in the Kingdom' mean to you?» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR CITY · NAJD» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### DEC-L06 — The people side of a plant
- **Date:** 2026-12-16  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** People and careers
- **Caption (AR):**

> قبل الآلات، الناس. في المختبر، وعلى الخط، وفي قاعة التعبئة.
> نساء ورجال يعملون معًا في المكان نفسه.
> مَن تحبون أن نعرّفكم به من فريقنا؟

- **Caption (EN):**

> Before the machines, the people: in the lab, on the line and in the packaging hall.
> Women and men working together in the same place.
> Who from our team would you like to meet?

- **Hashtags:** #سدير_للأدوية #SudairPharma #ناس_سدير #PeopleOfSudair

#### Slide 1/5 — hook
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab analyst at the bench (A007), three-quarter view, soft key light from the left, dark green panel on the right. No readable label on any container.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | قبل الآلات |
| Arabic headline 2 | الناس |
| Kashida word | الآلات |
| English headline | Before the machines, the people |
| Arabic body | الجانب الإنساني في المصنع. |
| English body | The people side of a plant. |

**Typography spec:**

  1. Arabic headline line 1 «قبل الآلات» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «الناس» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «الآلات» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الجانب الإنساني في المصنع.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «Before the machines, the people» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «The people side of a plant.» — Roboto Light, 26 px, white 80%, y=746.
  6. Chip «THE PEOPLE · 1 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab analyst at the bench (A007), three-quarter view, soft key light from the left, dark green panel on the right. No readable label on any container.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «قبل الآلات» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «الناس» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «الآلات» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الجانب الإنساني في المصنع.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «Before the machines, the people» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «The people side of a plant.» — Roboto Light, 26 px, white 80%, y=746.
6. Chip «THE PEOPLE · 1 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab team standing together in the lab (A005), wide, natural faces, graded to the emerald palette.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4

| Element | String |
|---|---|
| Arabic headline 1 | فريق المختبر |
| Arabic headline 2 | معًا في مكانه |
| Kashida word | المختبر |
| English headline | The lab team, together |
| Arabic body | وجوهٌ تعمل عند الطاولة كل يوم. |
| English body | Faces at the bench, day after day. |

**Typography spec:**

  1. Arabic headline line 1 «فريق المختبر» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «معًا في مكانه» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «المختبر» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «وجوهٌ تعمل عند الطاولة كل يوم.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The lab team, together» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Faces at the bench, day after day.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «THE PEOPLE · 2 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A005: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab team standing together in the lab (A005), wide, natural faces, graded to the emerald palette.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «فريق المختبر» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «معًا في مكانه» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «المختبر» with kashida (tatweel) for rhythm.
3. Arabic supporting line «وجوهٌ تعمل عند الطاولة كل يوم.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The lab team, together» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Faces at the bench, day after day.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «THE PEOPLE · 2 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Operator in a full suit (A012), cropped to the person and the station; no label, no text. Dark green panel on the right.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4

| Element | String |
|---|---|
| Arabic headline 1 | على الخط |
| Arabic headline 2 | بهدوء وتركيز |
| Kashida word | الخط |
| English headline | On the line, calm and focused |
| Arabic body | مشغّل بزيّه الكامل في مكان عمله. |
| English body | An operator in a full suit, at their station. |

**Typography spec:**

  1. Arabic headline line 1 «على الخط» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «بهدوء وتركيز» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «الخط» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «مشغّل بزيّه الكامل في مكان عمله.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «On the line, calm and focused» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «An operator in a full suit, at their station.» — Roboto Light, 26 px, white 80%, y=746.
  6. Chip «THE PEOPLE · 3 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A012: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Operator in a full suit (A012), cropped to the person and the station; no label, no text. Dark green panel on the right.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «على الخط» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «بهدوء وتركيز» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «الخط» with kashida (tatweel) for rhythm.
3. Arabic supporting line «مشغّل بزيّه الكامل في مكان عمله.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «On the line, calm and focused» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «An operator in a full suit, at their station.» — Roboto Light, 26 px, white 80%, y=746.
6. Chip «THE PEOPLE · 3 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The packaging hall with women and men at the line (A013), wide, natural faces, emerald grade.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | قاعة التعبئة |
| Arabic headline 2 | نساءٌ ورجال |
| Kashida word | قاعة |
| English headline | The packaging hall |
| Arabic body | نساء ورجال جنبًا إلى جنب. |
| English body | Women and men, side by side. |

**Typography spec:**

  1. Arabic headline line 1 «قاعة التعبئة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «نساءٌ ورجال» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «قاعة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «نساء ورجال جنبًا إلى جنب.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The packaging hall» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Women and men, side by side.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «THE PEOPLE · 4 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The packaging hall with women and men at the line (A013), wide, natural faces, emerald grade.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «قاعة التعبئة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «نساءٌ ورجال» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «قاعة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «نساء ورجال جنبًا إلى جنب.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The packaging hall» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Women and men, side by side.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «THE PEOPLE · 4 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, two-level Arabic headline, thin mint rule, one small line icon of two people. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | وراء المصنع |
| Arabic headline 2 | وجوهٌ وأسماء |
| Kashida word | المصنع |
| English headline | Behind the plant, faces and names |
| Arabic body | مَن تحبون أن نعرّفكم به من فريقنا؟ اكتبوا لنا. |
| English body | Who from our team would you like to meet? Tell us. |

**Typography spec:**

  1. Arabic headline line 1 «وراء المصنع» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وجوهٌ وأسماء» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «المصنع» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «مَن تحبون أن نعرّفكم به من فريقنا؟ اكتبوا لنا.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Behind the plant, faces and names» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Who from our team would you like to meet? Tell us.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Visible capability. Measurable impact.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, two-level Arabic headline, thin mint rule, one small line icon of two people. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وراء المصنع» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وجوهٌ وأسماء» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «المصنع» with kashida (tatweel) for rhythm.
3. Arabic supporting line «مَن تحبون أن نعرّفكم به من فريقنا؟ اكتبوا لنا.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Behind the plant, faces and names» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Who from our team would you like to meet? Tell us.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Visible capability. Measurable impact.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### DEC-F08 — Where the work happens
- **Date:** 2026-12-17  |  **Channel:** Instagram + Facebook  |  **Format:** Carousel, 5 slides  |  **Pillar:** Meet the makers
- **Caption (AR):**

> أين يحدث العمل في مدينة سدير؟
> مرّروا لنمشي معًا: الواجهة، والممرّ، وطاولة العمل.
> أيّ مكانٍ تودّون أن نُريكم بعد؟

- **Caption (EN):**

> Where does the work happen at Sudair City?
> Swipe and walk with us: the facade, the corridor, the bench.
> Which place should we show next?

- **Hashtags:** #سدير_للأدوية #SudairPharma #مدينة_سدير #صناعة_سعودية

#### Slide 1/5 — hook
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Route of small nodes on a thin mint line over a faint crop of the whole-site drone frame (A002); emerald background, lattice at 6%.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | أين يحدث |
| Arabic headline 2 | العمل؟ |
| Kashida word | يحدث |
| English headline | Where the work happens. |
| Arabic body | جولة قصيرة في المكان. |
| English body | A short walk around the site. |

**Typography spec:**

  1. Arabic headline line 1 «أين يحدث» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «العمل؟» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «يحدث» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «جولة قصيرة في المكان.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Where the work happens.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «A short walk around the site.» — Roboto Light, 26 px, white 80%, y=386.
  6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1210.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Route of small nodes on a thin mint line over a faint crop of the whole-site drone frame (A002); emerald background, lattice at 6%.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «أين يحدث» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «العمل؟» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «يحدث» with kashida (tatweel) for rhythm.
3. Arabic supporting line «جولة قصيرة في المكان.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Where the work happens.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «A short walk around the site.» — Roboto Light, 26 px, white 80%, y=386.
6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1210.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Full-bleed real frame of the palm-lined facade at golden light (A001), teal grade, a small route node bottom-left.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | الواجهة |
| Arabic headline 2 | بين النخيل |
| Kashida word | الواجهة |
| English headline | The facade, among the palms. |
| Arabic body | من هنا يدخل الفريق كل صباح. |
| English body | Where the team comes in each morning. |

**Typography spec:**

  1. Arabic headline line 1 «الواجهة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «بين النخيل» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الواجهة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «من هنا يدخل الفريق كل صباح.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The facade, among the palms.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Where the team comes in each morning.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A001: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Full-bleed real frame of the palm-lined facade at golden light (A001), teal grade, a small route node bottom-left.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الواجهة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «بين النخيل» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الواجهة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «من هنا يدخل الفريق كل صباح.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The facade, among the palms.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Where the team comes in each morning.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Full-bleed real frame of the corridor in long perspective (A003), lights on, teal-green grade, route node bottom-left.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | الممرّ |
| Arabic headline 2 | يُضاء مع الصباح |
| Kashida word | الممرّ |
| English headline | The corridor, lit for the day. |
| Arabic body | طريقٌ يعبره الجميع. |
| English body | A path everyone walks. |

**Typography spec:**

  1. Arabic headline line 1 «الممرّ» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «يُضاء مع الصباح» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الممرّ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «طريقٌ يعبره الجميع.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The corridor, lit for the day.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «A path everyone walks.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A003: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Full-bleed real frame of the corridor in long perspective (A003), lights on, teal-green grade, route node bottom-left.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الممرّ» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «يُضاء مع الصباح» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الممرّ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «طريقٌ يعبره الجميع.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The corridor, lit for the day.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «A path everyone walks.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Close real frame of a gloved hand beside a row of glassware (A009), no readable label, soft emerald light, route node bottom-left.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4

| Element | String |
|---|---|
| Arabic headline 1 | طاولة العمل |
| Arabic headline 2 | عن قرب |
| Kashida word | طاولة |
| English headline | The bench, up close. |
| Arabic body | زجاجٌ وضوءٌ ويدٌ ثابتة. |
| English body | Glass, light and a steady hand. |

**Typography spec:**

  1. Arabic headline line 1 «طاولة العمل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «عن قرب» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «طاولة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «زجاجٌ وضوءٌ ويدٌ ثابتة.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The bench, up close.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Glass, light and a steady hand.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A009: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Close real frame of a gloved hand beside a row of glassware (A009), no readable label, soft emerald light, route node bottom-left.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «طاولة العمل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «عن قرب» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «طاولة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «زجاجٌ وضوءٌ ويدٌ ثابتة.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The bench, up close.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Glass, light and a steady hand.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Deep emerald type card with hairline frame, mint rule and the theme line; logo bottom-left.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | أيّ مكانٍ |
| Arabic headline 2 | تودّون رؤيته؟ |
| Kashida word | مكانٍ |
| English headline | Which place next? |
| Arabic body | صناعة تُرى، وأثر يُقاس. |
| English body | Visible capability. Measurable impact. |

**Typography spec:**

  1. Arabic headline line 1 «أيّ مكانٍ» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «تودّون رؤيته؟» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «مكانٍ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Which place next?» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Tell us in the comments which place to show next.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Deep emerald type card with hairline frame, mint rule and the theme line; logo bottom-left.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «أيّ مكانٍ» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «تودّون رؤيته؟» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «مكانٍ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Which place next?» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Tell us in the comments which place to show next.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### DEC-F09 — People of Sudair
- **Date:** 2026-12-20  |  **Channel:** Instagram + Facebook  |  **Format:** Carousel, 5 slides  |  **Pillar:** People and careers
- **Caption (AR):**

> قبل المكان، هناك الناس.
> وجوهٌ تصل في الصباح، وأيدٍ تعمل، وفِرقٌ تعرف بعضها.
> من تحبّون أن تتعرّفوا عليه في سدير؟ أخبرونا.

- **Caption (EN):**

> Before the place, there are the people.
> Faces arriving in the morning, hands at work, teams who know each other.
> Who would you like to meet at Sudair? Tell us.

- **Hashtags:** #سدير_للأدوية #SudairPharma #ناس_سدير #PeopleOfSudair

#### Slide 1/5 — hook
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Portrait panel: tight three-quarter crop of one colleague from the hall frame (A013), dark green panelled wall, right column clear for the headline.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | ناس سدير |
| Arabic headline 2 | قبل كل شيء |
| Kashida word | سدير |
| English headline | People of Sudair. |
| Arabic body | وجوهٌ وراء المكان. |
| English body | The faces behind the place. |

**Typography spec:**

  1. Arabic headline line 1 «ناس سدير» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «قبل كل شيء» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «سدير» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «وجوهٌ وراء المكان.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «People of Sudair.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «The faces behind the place.» — Roboto Light, 26 px, white 80%, y=746.
  6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Portrait panel: tight three-quarter crop of one colleague from the hall frame (A013), dark green panelled wall, right column clear for the headline.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ناس سدير» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «قبل كل شيء» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «سدير» with kashida (tatweel) for rhythm.
3. Arabic supporting line «وجوهٌ وراء المكان.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «People of Sudair.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «The faces behind the place.» — Roboto Light, 26 px, white 80%, y=746.
6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1110.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Full-bleed real frame of the lab team standing together in the lab (A005), teal-green grade, natural faces.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4

| Element | String |
|---|---|
| Arabic headline 1 | فريق المختبر |
| Arabic headline 2 | يقف معًا |
| Kashida word | معًا |
| English headline | The lab team, together. |
| Arabic body | زملاءٌ يعرفون بعضهم. |
| English body | Colleagues who know each other. |

**Typography spec:**

  1. Arabic headline line 1 «فريق المختبر» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «يقف معًا» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «معًا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «زملاءٌ يعرفون بعضهم.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The lab team, together.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Colleagues who know each other.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A005: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Full-bleed real frame of the lab team standing together in the lab (A005), teal-green grade, natural faces.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «فريق المختبر» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «يقف معًا» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «معًا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «زملاءٌ يعرفون بعضهم.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The lab team, together.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Colleagues who know each other.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real frame of an operator at a station (A011), seen through a glove port, soft emerald light, nothing readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4

| Element | String |
|---|---|
| Arabic headline 1 | كلٌّ في موقعه |
| Arabic headline 2 | وله دوره |
| Kashida word | موقعه |
| English headline | Each at their post. |
| Arabic body | لكل زميلٍ دوره. |
| English body | Everyone has a part. |

**Typography spec:**

  1. Arabic headline line 1 «كلٌّ في موقعه» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «وله دوره» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «موقعه» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «لكل زميلٍ دوره.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Each at their post.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Everyone has a part.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A011: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real frame of an operator at a station (A011), seen through a glove port, soft emerald light, nothing readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «كلٌّ في موقعه» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «وله دوره» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «موقعه» with kashida (tatweel) for rhythm.
3. Arabic supporting line «لكل زميلٍ دوره.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Each at their post.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Everyone has a part.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Real frame of a colleague in full work suit (A012), calm, teal-green grade, morning light.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4

| Element | String |
|---|---|
| Arabic headline 1 | بزيّ العمل |
| Arabic headline 2 | كل صباح |
| Kashida word | العمل |
| English headline | In work clothes, every morning. |
| Arabic body | صباحٌ جديد، ووجوهٌ مألوفة. |
| English body | A new morning, familiar faces. |

**Typography spec:**

  1. Arabic headline line 1 «بزيّ العمل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «كل صباح» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «العمل» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «صباحٌ جديد، ووجوهٌ مألوفة.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «In work clothes, every morning.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «A new morning, familiar faces.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A012: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Real frame of a colleague in full work suit (A012), calm, teal-green grade, morning light.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «بزيّ العمل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «كل صباح» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «العمل» with kashida (tatweel) for rhythm.
3. Arabic supporting line «صباحٌ جديد، ووجوهٌ مألوفة.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «In work clothes, every morning.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «A new morning, familiar faces.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Deep emerald type card with hairline frame, mint rule and the theme line; logo bottom-left.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | من تودّون |
| Arabic headline 2 | أن تعرفوه؟ |
| Kashida word | تودّون |
| English headline | Who would you like to meet? |
| Arabic body | صناعة تُرى، وأثر يُقاس. |
| English body | Visible capability. Measurable impact. |

**Typography spec:**

  1. Arabic headline line 1 «من تودّون» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «أن تعرفوه؟» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تودّون» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Who would you like to meet?» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Tell us in the comments.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Deep emerald type card with hairline frame, mint rule and the theme line; logo bottom-left.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «من تودّون» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «أن تعرفوه؟» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تودّون» with kashida (tatweel) for rhythm.
3. Arabic supporting line «صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Who would you like to meet?» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Tell us in the comments.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### DEC-L07 — Looking back with gratitude
- **Date:** 2026-12-28  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Year and community
- **Caption (AR):**

> مع اقتراب نهاية العام، نتوقف لنقول شكرًا.
> لفِرقنا في كل ورديّة، ولشركائنا على المنصّات، ولكل من تابعنا وكتب لنا.
> كل عام وأنتم بخير.

- **Caption (EN):**

> As the year closes, we stop to say thank you.
> To our teams on every shift, to our partners on the stages, and to everyone who followed and wrote to us.
> Happy New Year from all of us at Sudair Pharma.

- **Hashtags:** #سدير_للأدوية #SudairPharma #شكرا #ThankYou2026

#### Slide 1/5 — hook
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, 'Thank you' centred and large, thin mint rule, one small white line icon of a palm, hairline inset frame. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | شكرًا |
| Arabic headline 2 | على عامٍ معكم |
| Kashida word | شكرًا |
| English headline | Thank you, for a year with you |
| Arabic body | نظرة إلى الوراء، بامتنان. |
| English body | A look back, with gratitude. |

**Typography spec:**

  1. Arabic headline line 1 «شكرًا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «على عامٍ معكم» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكرًا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «نظرة إلى الوراء، بامتنان.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Thank you, for a year with you» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «A look back, with gratitude.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «THANK YOU · 1 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, 'Thank you' centred and large, thin mint rule, one small white line icon of a palm, hairline inset frame. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكرًا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «على عامٍ معكم» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكرًا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «نظرة إلى الوراء، بامتنان.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Thank you, for a year with you» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «A look back, with gratitude.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «THANK YOU · 1 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The wide team photograph at the booth (A048), team in a single row, teal-green sky grade, ID badges softened. Caption area left clear.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG

| Element | String |
|---|---|
| Arabic headline 1 | لفِرقنا |
| Arabic headline 2 | في كل ورديّة |
| Kashida word | لفِرقنا |
| English headline | To our teams, on every shift |
| Arabic body | للأيام والليالي التي قضيتموها في الموقع. |
| English body | For the days and the nights you gave to the site. |

**Typography spec:**

  1. Arabic headline line 1 «لفِرقنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «في كل ورديّة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «لفِرقنا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «للأيام والليالي التي قضيتموها في الموقع.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «To our teams, on every shift» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «For the days and the nights you gave to the site.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «THANK YOU · 2 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A048: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The wide team photograph at the booth (A048), team in a single row, teal-green sky grade, ID badges softened. Caption area left clear.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «لفِرقنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «في كل ورديّة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «لفِرقنا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «للأيام والليالي التي قضيتموها في الموقع.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «To our teams, on every shift» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «For the days and the nights you gave to the site.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «THANK YOU · 2 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T5 Speaker or event · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Signing line-up on stage (A016), wide, host signage smaller than the Sudair mark, emerald frame.

**Assets (root = `Sudair Assets`):**
  - News Photos-20261001T081151Z-1-001/News Photos/Copy of Agreements at GHE.JPG

| Element | String |
|---|---|
| Arabic headline 1 | لشركائنا |
| Arabic headline 2 | على المنصّات |
| Kashida word | لشركائنا |
| English headline | To our partners, on the stages |
| Arabic body | لمن وقّع معنا ووقف بجانبنا. |
| English body | To those who signed with us and stood beside us. |

**Typography spec:**

  1. Arabic headline line 1 «لشركائنا» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «على المنصّات» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «لشركائنا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «لمن وقّع معنا ووقف بجانبنا.» — Muna Regular, 40 px, white 90%, centred, y=380.
  4. English line «To our partners, on the stages» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
  5. English support line «To those who signed with us and stood beside us.» — Roboto Light, 28 px, white 80%, y=426.
  6. Chip «THANK YOU · 3 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A016: upload "Sudair Assets/News Photos-20261001T081151Z-1-001/News Photos/Copy of Agreements at GHE.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Signing line-up on stage (A016), wide, host signage smaller than the Sudair mark, emerald frame.

TREATMENT T5, Speaker or event: Event card treatment: black-and-white head-and-shoulders portraits or one event photograph with a diagonal lime corner accent, emerald background with a faint large SPC logotype behind, calendar icon with date, location pin with city, a rounded outlined bar for the contact line.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «لشركائنا» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «على المنصّات» — same family, 70 px, mint #8EF0B0, y=280. Stretch the word «لشركائنا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «لمن وقّع معنا ووقف بجانبنا.» — Muna Regular, 40 px, white 90%, centred, y=380.
4. English line «To our partners, on the stages» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=380.
5. English support line «To those who signed with us and stood beside us.» — Roboto Light, 28 px, white 80%, y=426.
6. Chip «THANK YOU · 3 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The Sudair booth at the Saudi Made exhibition with visitors (A109), wide, warm light, emerald grade.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/معرض صنع في السعودية/sudair-pharma-saudi-made-2025-booth.JPG

| Element | String |
|---|---|
| Arabic headline 1 | ولكل من زارنا |
| Arabic headline 2 | وتابعنا وكتب لنا |
| Kashida word | زارنا |
| English headline | To everyone who visited, followed and wrote |
| Arabic body | أنتم مَن جعل هذا العام مشتركًا. |
| English body | You made this a year we shared. |

**Typography spec:**

  1. Arabic headline line 1 «ولكل من زارنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «وتابعنا وكتب لنا» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «زارنا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «أنتم مَن جعل هذا العام مشتركًا.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «To everyone who visited, followed and wrote» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «You made this a year we shared.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «THANK YOU · 4 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A109: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/معرض صنع في السعودية/sudair-pharma-saudi-made-2025-booth.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The Sudair booth at the Saudi Made exhibition with visitors (A109), wide, warm light, emerald grade.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ولكل من زارنا» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «وتابعنا وكتب لنا» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «زارنا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «أنتم مَن جعل هذا العام مشتركًا.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «To everyone who visited, followed and wrote» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «You made this a year we shared.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «THANK YOU · 4 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, 'Happy New Year' in two levels, thin mint rule, one small line icon of a palm. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | كل عامٍ |
| Arabic headline 2 | وأنتم بخير |
| Kashida word | عامٍ |
| English headline | Happy New Year |
| Arabic body | كل عام وأنتم بخير. صناعة تُرى، وأثر يُقاس. |
| English body | Happy New Year from all of us at Sudair Pharma. Visible capability. Measurable impact. |

**Typography spec:**

  1. Arabic headline line 1 «كل عامٍ» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأنتم بخير» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «عامٍ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «كل عام وأنتم بخير. صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Happy New Year» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Happy New Year from all of us at Sudair Pharma. Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Visible capability. Measurable impact.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, 'Happy New Year' in two levels, thin mint rule, one small line icon of a palm. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «كل عامٍ» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأنتم بخير» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «عامٍ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «كل عام وأنتم بخير. صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Happy New Year» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Happy New Year from all of us at Sudair Pharma. Visible capability. Measurable impact.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Visible capability. Measurable impact.» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### DEC-L08 — What we carry into the new year: values and people
- **Date:** 2026-12-30  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** People and careers
- **Caption (AR):**

> ما الذي نحمله معنا إلى العام الجديد؟ قيمٌ وناس.
> الناس في المقدّمة، واحترام للعمل، وانتماء إلى هذا المكان.
> ما القيمة التي تحملونها أنتم؟

- **Caption (EN):**

> What do we carry into the new year? Values and people.
> People at the centre, respect for the work, and belonging to this place.
> Which value do you carry?

- **Hashtags:** #سدير_للأدوية #SudairPharma #قيمنا #NewYear2027

#### Slide 1/5 — hook
**Treatment:** T1 Glass object · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Semi-transparent glass palm-tree sculpture on a glossy emerald floor, centred, 55 percent of tile height, mint rim light, faint lattice; three icon chips below (people, work, place). Clear logo area top-left.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | ما نحمله |
| Arabic headline 2 | إلى العام الجديد |
| Kashida word | نحمله |
| English headline | What we carry into the new year |
| Arabic body | قيمٌ وناس. |
| English body | Values and people. |

**Typography spec:**

  1. Arabic headline line 1 «ما نحمله» — AE_Sharjah-style heavy geometric kufi, 128 px, #FFFFFF, centred at y=170.
  2. Arabic headline line 2 «إلى العام الجديد» — same family, 84 px, mint #8EF0B0, y=320. Stretch the word «نحمله» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «قيمٌ وناس.» — Muna Regular, 40 px, white 90%, centred, y=420.
  4. English line «What we carry into the new year» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=430.
  5. English support line «Values and people.» — Roboto Light, 28 px, white 80%, y=476.
  6. Chip «VALUES · 1 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Semi-transparent glass palm-tree sculpture on a glossy emerald floor, centred, 55 percent of tile height, mint rim light, faint lattice; three icon chips below (people, work, place). Clear logo area top-left.

TREATMENT T1, Glass object: Premium 3D render of the hero object, semi-transparent glass and brushed metal, soft studio light from the upper left, mint rim light, clean reflections on a glossy emerald floor, shallow depth of field. Emerald gradient background from #09A45B (top-left glow) to #04301F (bottom-right), faint rounded-diamond lattice at 8% opacity. Hero centred, 55% of tile height, 90 px free space around it.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ما نحمله» — AE_Sharjah-style heavy geometric kufi, 128 px, #FFFFFF, centred at y=170.
2. Arabic headline line 2 «إلى العام الجديد» — same family, 84 px, mint #8EF0B0, y=320. Stretch the word «نحمله» with kashida (tatweel) for rhythm.
3. Arabic supporting line «قيمٌ وناس.» — Muna Regular, 40 px, white 90%, centred, y=420.
4. English line «What we carry into the new year» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=430.
5. English support line «Values and people.» — Roboto Light, 28 px, white 80%, y=476.
6. Chip «VALUES · 1 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1130.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The wide team photograph at the booth (A048), team in a single row, teal-green sky grade, ID badges softened.

**Assets (root = `Sudair Assets`):**
  - OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG

| Element | String |
|---|---|
| Arabic headline 1 | الناس |
| Arabic headline 2 | في المقدّمة |
| Kashida word | الناس |
| English headline | People at the centre |
| Arabic body | النساء والرجال الذين يعملون هنا. |
| English body | The women and men who work here. |

**Typography spec:**

  1. Arabic headline line 1 «الناس» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «في المقدّمة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الناس» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «النساء والرجال الذين يعملون هنا.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «People at the centre» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «The women and men who work here.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «VALUES · 2 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A048: upload "Sudair Assets/OneDrive_2026-10-01/Gallery Photos/GHE25/sudair-pharma-global-health-2025-team.JPG". Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The wide team photograph at the booth (A048), team in a single row, teal-green sky grade, ID badges softened.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الناس» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «في المقدّمة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الناس» with kashida (tatweel) for rhythm.
3. Arabic supporting line «النساء والرجال الذين يعملون هنا.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «People at the centre» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «The women and men who work here.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «VALUES · 2 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Close crop of a gloved hand beside a row of flasks (A009), no label legible, shallow depth, emerald grade.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4

| Element | String |
|---|---|
| Arabic headline 1 | احترام العمل |
| Arabic headline 2 | الذي نقوم به |
| Kashida word | احترام |
| English headline | Respect for the work |
| Arabic body | يومُ عمل يُؤدّى بانتباه. |
| English body | A day's work, done with attention. |

**Typography spec:**

  1. Arabic headline line 1 «احترام العمل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «الذي نقوم به» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «احترام» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يومُ عمل يُؤدّى بانتباه.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Respect for the work» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «A day's work, done with attention.» — Roboto Light, 26 px, white 80%, y=466.
  6. Chip «VALUES · 3 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A009: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Close crop of a gloved hand beside a row of flasks (A009), no label legible, shallow depth, emerald grade.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «احترام العمل» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «الذي نقوم به» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «احترام» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يومُ عمل يُؤدّى بانتباه.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Respect for the work» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «A day's work, done with attention.» — Roboto Light, 26 px, white 80%, y=466.
6. Chip «VALUES · 3 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The palm-lined building and campus in golden light (A001) inside a petal window, dusk grade, no people.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | الانتماء |
| Arabic headline 2 | إلى هذا المكان |
| Kashida word | الانتماء |
| English headline | Belonging to this place |
| Arabic body | مدينة سدير، نجد، المملكة. |
| English body | Sudair City, Najd, the Kingdom. |

**Typography spec:**

  1. Arabic headline line 1 «الانتماء» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «إلى هذا المكان» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «الانتماء» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «مدينة سدير، نجد، المملكة.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «Belonging to this place» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «Sudair City, Najd, the Kingdom.» — Roboto Light, 34 px, white 80%, y=626.
  6. Chip «VALUES · 4 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A001: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The palm-lined building and campus in golden light (A001) inside a petal window, dusk grade, no people.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الانتماء» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «إلى هذا المكان» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «الانتماء» with kashida (tatweel) for rhythm.
3. Arabic supporting line «مدينة سدير، نجد، المملكة.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «Belonging to this place» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «Sudair City, Najd, the Kingdom.» — Roboto Light, 34 px, white 80%, y=626.
6. Chip «VALUES · 4 OF 5» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, two-level Arabic headline, thin mint rule, one small line icon of a palm. No photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | قيمٌ نحملها |
| Arabic headline 2 | وناسٌ نعتزّ بهم |
| Kashida word | نحملها |
| English headline | Values we hold, people we value |
| Arabic body | ما القيمة التي تحملونها معكم إلى العام الجديد؟ |
| English body | Which value do you carry into the new year? |

**Typography spec:**

  1. Arabic headline line 1 «قيمٌ نحملها» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وناسٌ نعتزّ بهم» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «نحملها» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «ما القيمة التي تحملونها معكم إلى العام الجديد؟» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Values we hold, people we value» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Which value do you carry into the new year?» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, two-level Arabic headline, thin mint rule, one small line icon of a palm. No photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «قيمٌ نحملها» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وناسٌ نعتزّ بهم» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «نحملها» with kashida (tatweel) for rhythm.
3. Arabic supporting line «ما القيمة التي تحملونها معكم إلى العام الجديد؟» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Values we hold, people we value» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Which value do you carry into the new year?» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «SUDAIR PHARMA» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---


## January 2027

### JAN-L01 — Seven steps, no secrets: steps 1 to 3 ⚠ CLAIM REVIEW
- **Date:** 2027-01-04  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 6 slides  |  **Pillar:** How it is made
- ⚠ **Client must verify:** Client must confirm that the line can be described as seven steps and that steps 1 to 3 (materials arrive and are logged, each ingredient is weighed, ingredients are combined in a clean room) match the real sequence at the Sudair City plant.
- **Caption (AR):**

> للخط الذي نعمل عليه سبع خطوات، من وصول المواد إلى خروج الدفعة.
> نبدأ هذا الأسبوع بالثلاث الأولى: الاستلام، والوزن، والتحضير.
> تابعونا لتعرفوا بقية الخطوات.

- **Caption (EN):**

> The line we work on has seven steps, from materials arriving to the batch leaving.
> This week we start with the first three: receive, weigh, prepare.
> Follow along for the rest.

- **Hashtags:** #سدير_للأدوية #SudairPharma #سبع_خطوات #SevenSteps #صناعة_سعودية

#### Slide 1/6 — hook
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The campus seen from the air at golden hour under three glowing petal windows; headline on the dark emerald left side. No people.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | سبع خطوات |
| Arabic headline 2 | بلا أسرار |
| Kashida word | خطوات |
| English headline | Seven steps. No secrets. |
| Arabic body | الخطوات من الأولى إلى الثالثة. |
| English body | Steps 1 to 3. |

**Typography spec:**

  1. Arabic headline line 1 «سبع خطوات» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «بلا أسرار» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «خطوات» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الخطوات من الأولى إلى الثالثة.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «Seven steps. No secrets.» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «Steps 1 to 3.» — Roboto Light, 34 px, white 80%, y=626.
  6. Chip «Part 1 of 3» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The campus seen from the air at golden hour under three glowing petal windows; headline on the dark emerald left side. No people.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «سبع خطوات» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «بلا أسرار» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «خطوات» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الخطوات من الأولى إلى الثالثة.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «Seven steps. No secrets.» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «Steps 1 to 3.» — Roboto Light, 34 px, white 80%, y=626.
6. Chip «Part 1 of 3» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1240.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٦» in small Arabic-Indic digits and 1/6 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/6 — idea
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Seven small rounded step cards joined by a thin mint line on emerald, numbers in circles and one-word labels; steps 1 to 3 lit in mint, 4 to 7 dimmed. No photograph needed.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | للخط سبع خطوات |
| Arabic headline 2 | نبدأ بالأولى |
| Kashida word | سبع |
| English headline | The line has seven steps. |
| Arabic body | استلام، وزن، تحضير، تعبئة، تغليف، إفراج، شحن. |
| English body | Receive. Weigh. Prepare. Fill. Pack. Release. Ship. |

**Typography spec:**

  1. Arabic headline line 1 «للخط سبع خطوات» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «نبدأ بالأولى» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «سبع» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «استلام، وزن، تحضير، تعبئة، تغليف، إفراج، شحن.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «The line has seven steps.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Receive. Weigh. Prepare. Fill. Pack. Release. Ship.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Seven small rounded step cards joined by a thin mint line on emerald, numbers in circles and one-word labels; steps 1 to 3 lit in mint, 4 to 7 dimmed. No photograph needed.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «للخط سبع خطوات» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «نبدأ بالأولى» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «سبع» with kashida (tatweel) for rhythm.
3. Arabic supporting line «استلام، وزن، تحضير، تعبئة، تغليف، إفراج، شحن.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «The line has seven steps.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Receive. Weigh. Prepare. Fill. Pack. Release. Ship.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٦» in small Arabic-Indic digits and 2/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/6 — step
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Step card 1 with a generated store of incoming materials on pallets and shelves, soft light, no readable labels, no brand marks.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | الخطوة الأولى |
| Arabic headline 2 | الاستلام |
| Kashida word | الاستلام |
| English headline | Step 1: Receive. |
| Arabic body | تصل المواد إلى المصنع وتُسجَّل قبل أي عمل. |
| English body | Materials arrive at the plant and are logged before any work begins. |

**Typography spec:**

  1. Arabic headline line 1 «الخطوة الأولى» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «الاستلام» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الاستلام» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تصل المواد إلى المصنع وتُسجَّل قبل أي عمل.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Step 1: Receive.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Materials arrive at the plant and are logged before any work begins.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Step card 1 with a generated store of incoming materials on pallets and shelves, soft light, no readable labels, no brand marks.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوة الأولى» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «الاستلام» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الاستلام» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تصل المواد إلى المصنع وتُسجَّل قبل أي عمل.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Step 1: Receive.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Materials arrive at the plant and are logged before any work begins.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٦» in small Arabic-Indic digits and 3/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/6 — step
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Step card 2 with a close crop of a gloved hand beside a row of glass flasks on a bench, no label legible.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الخطوة الثانية |
| Arabic headline 2 | الوزن |
| Kashida word | الوزن |
| English headline | Step 2: Weigh. |
| Arabic body | يُوزن كل مكوّن ويُقاس بحسب ما تحتاجه الدفعة. |
| English body | Each ingredient is weighed and measured out for the batch. |

**Typography spec:**

  1. Arabic headline line 1 «الخطوة الثانية» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «الوزن» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الوزن» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يُوزن كل مكوّن ويُقاس بحسب ما تحتاجه الدفعة.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Step 2: Weigh.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Each ingredient is weighed and measured out for the batch.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A009: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Step card 2 with a close crop of a gloved hand beside a row of glass flasks on a bench, no label legible.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوة الثانية» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «الوزن» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الوزن» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يُوزن كل مكوّن ويُقاس بحسب ما تحتاجه الدفعة.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Step 2: Weigh.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Each ingredient is weighed and measured out for the batch.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٦» in small Arabic-Indic digits and 4/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/6 — step
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Step card 3 with the clean-room corridor in cool light, empty, long perspective, no signage readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | الخطوة الثالثة |
| Arabic headline 2 | التحضير |
| Kashida word | التحضير |
| English headline | Step 3: Prepare. |
| Arabic body | تُجمع المكوّنات المقاسة داخل غرفة نظيفة. |
| English body | The measured ingredients are brought together inside a clean room. |

**Typography spec:**

  1. Arabic headline line 1 «الخطوة الثالثة» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «التحضير» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «التحضير» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تُجمع المكوّنات المقاسة داخل غرفة نظيفة.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Step 3: Prepare.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «The measured ingredients are brought together inside a clean room.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A003: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Step card 3 with the clean-room corridor in cool light, empty, long perspective, no signage readable.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوة الثالثة» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «التحضير» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «التحضير» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تُجمع المكوّنات المقاسة داخل غرفة نظيفة.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Step 3: Prepare.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «The measured ingredients are brought together inside a clean room.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٦» in small Arabic-Indic digits and 5/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 6/6 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | تُرى |
| English headline | Visible capability. Measurable impact. |
| Arabic body | الخطوات من الرابعة إلى السادسة تصلكم الأسبوع القادم. |
| English body | Steps 4 to 6 follow next week. |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الخطوات من الرابعة إلى السادسة تصلكم الأسبوع القادم.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Steps 4 to 6 follow next week.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الخطوات من الرابعة إلى السادسة تصلكم الأسبوع القادم.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Steps 4 to 6 follow next week.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 6 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٦/٦» in small Arabic-Indic digits and 6/6 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### JAN-L02 — What you will see here in 2027
- **Date:** 2027-01-06  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Year and community
- **Caption (AR):**

> عامٌ جديد، وصفحة تعرّفكم بمن يعمل في سدير للأدوية وبالمكان الذي نعمل فيه.
> وجوه الفريق، ومدينة سدير، والعمل كما يُرى من قرب.
> ما الذي تودّون رؤيته هنا؟ شاركونا في التعليقات.

- **Caption (EN):**

> A new year, and a page about the people who work at Sudair Pharma and the place we work in.
> The faces of the team, Sudair City, and the work as it looks up close.
> What would you like to see here? Tell us in the comments.

- **Hashtags:** #سدير_للأدوية #SudairPharma #عام_جديد #NewYear2027

#### Slide 1/5 — hook
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type-only card on deep emerald with a thin mint rule and one small white palm line icon; no photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | ما سترونه هنا |
| Arabic headline 2 | في 2027 |
| Kashida word | سترونه |
| English headline | What you will see here in 2027 |
| Arabic body | الناس، والمكان، والعمل. |
| English body | The people, the place, the work. |

**Typography spec:**

  1. Arabic headline line 1 «ما سترونه هنا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «في 2027» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «سترونه» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الناس، والمكان، والعمل.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «What you will see here in 2027» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «The people, the place, the work.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type-only card on deep emerald with a thin mint rule and one small white palm line icon; no photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ما سترونه هنا» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «في 2027» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «سترونه» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الناس، والمكان، والعمل.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «What you will see here in 2027» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «The people, the place, the work.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The packaging hall team, women and men, standing together beside the line, relaxed and proud, wide frame graded to the emerald palette; no readable label.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | وجوه الفريق |
| Arabic headline 2 | الناس عن قرب |
| Kashida word | الفريق |
| English headline | The faces of the team |
| Arabic body | من قاعة التغليف إلى المختبر، نعرّفكم بمن يعمل هنا. |
| English body | From the packaging hall to the lab, meet the people who work here. |

**Typography spec:**

  1. Arabic headline line 1 «وجوه الفريق» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «الناس عن قرب» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الفريق» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «من قاعة التغليف إلى المختبر، نعرّفكم بمن يعمل هنا.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The faces of the team» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «From the packaging hall to the lab, meet the people who work here.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The packaging hall team, women and men, standing together beside the line, relaxed and proud, wide frame graded to the emerald palette; no readable label.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وجوه الفريق» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «الناس عن قرب» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الفريق» with kashida (tatweel) for rhythm.
3. Arabic supporting line «من قاعة التغليف إلى المختبر، نعرّفكم بمن يعمل هنا.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The faces of the team» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «From the packaging hall to the lab, meet the people who work here.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Drone view of the whole Sudair City site in the desert in warm light, with a single petal-shaped window framing the campus; headline left on dark emerald.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | المكان |
| Arabic headline 2 | مدينة سدير |
| Kashida word | المكان |
| English headline | The place |
| Arabic body | مدينة سدير للصناعات الدوائية من الأعلى، ومن الداخل. |
| English body | Sudair City for Pharma Industry, from above and from inside. |

**Typography spec:**

  1. Arabic headline line 1 «المكان» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «مدينة سدير» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «المكان» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «مدينة سدير للصناعات الدوائية من الأعلى، ومن الداخل.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «The place» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «Sudair City for Pharma Industry, from above and from inside.» — Roboto Light, 34 px, white 80%, y=626.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Drone view of the whole Sudair City site in the desert in warm light, with a single petal-shaped window framing the campus; headline left on dark emerald.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «المكان» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «مدينة سدير» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «المكان» with kashida (tatweel) for rhythm.
3. Arabic supporting line «مدينة سدير للصناعات الدوائية من الأعلى، ومن الداخل.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «The place» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «Sudair City for Pharma Industry, from above and from inside.» — Roboto Light, 34 px, white 80%, y=626.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A lab analyst working at the bench, three-quarter view, calm and focused, soft key light from the left, dark green panel on the right for text; no readable label on any container.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | العمل |
| Arabic headline 2 | كما يُرى من قرب |
| Kashida word | قرب |
| English headline | The work |
| Arabic body | طاولات وخطوط وأيدٍ تعمل، بلا مصطلحات معقّدة. |
| English body | Benches, lines and hands at work, without the jargon. |

**Typography spec:**

  1. Arabic headline line 1 «العمل» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «كما يُرى من قرب» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «قرب» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «طاولات وخطوط وأيدٍ تعمل، بلا مصطلحات معقّدة.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «The work» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «Benches, lines and hands at work, without the jargon.» — Roboto Light, 26 px, white 80%, y=746.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A lab analyst working at the bench, three-quarter view, calm and focused, soft key light from the left, dark green panel on the right for text; no readable label on any container.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «العمل» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «كما يُرى من قرب» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «قرب» with kashida (tatweel) for rhythm.
3. Arabic supporting line «طاولات وخطوط وأيدٍ تعمل، بلا مصطلحات معقّدة.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «The work» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «Benches, lines and hands at work, without the jargon.» — Roboto Light, 26 px, white 80%, y=746.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | تُرى |
| English headline | Visible capability. Measurable impact. |
| Arabic body | ما الذي تودّون رؤيته هنا؟ أخبرونا في التعليقات. |
| English body | What would you like to see here? Tell us in the comments. |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «ما الذي تودّون رؤيته هنا؟ أخبرونا في التعليقات.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «What would you like to see here? Tell us in the comments.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
3. Arabic supporting line «ما الذي تودّون رؤيته هنا؟ أخبرونا في التعليقات.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «What would you like to see here? Tell us in the comments.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### JAN-L03 — How a medicine is made: steps 4 to 6 ⚠ CLAIM REVIEW
- **Date:** 2027-01-11  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 6 slides  |  **Pillar:** How it is made
- ⚠ **Client must verify:** Client must confirm that steps 4 to 6 (batch is filled into its containers with the operator working through glove ports, filled units are packed by the packaging hall team, the batch is released once its records are reviewed) match the real sequence and equipment at the plant.
- **Caption (AR):**

> الجزء الثاني من سبع خطوات بلا أسرار: التعبئة، والتغليف، والإفراج.
> خلف كل خطوة منها فريق يعمل بها.
> أي خطوة تودّون أن نتوسّع فيها؟

- **Caption (EN):**

> Part 2 of Seven steps, no secrets: fill, pack, release.
> Behind each step there is a team that works on it.
> Which step would you like us to look at more closely?

- **Hashtags:** #سدير_للأدوية #SudairPharma #سبع_خطوات #SevenSteps #صناعة_سعودية

#### Slide 1/6 — hook
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Three numbered step cards (4, 5, 6) in a vertical flow with real photo crops of the isolator, the packaging hall and a row of flasks, on emerald with a faint lattice.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4

| Element | String |
|---|---|
| Arabic headline 1 | كيف يُصنع الدواء؟ |
| Arabic headline 2 | الخطوات 4 إلى 6 |
| Kashida word | الدواء |
| English headline | How a medicine is made. |
| Arabic body | التعبئة، والتغليف، والإفراج. |
| English body | Fill, pack, release. |

**Typography spec:**

  1. Arabic headline line 1 «كيف يُصنع الدواء؟» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «الخطوات 4 إلى 6» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الدواء» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «التعبئة، والتغليف، والإفراج.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «How a medicine is made.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Fill, pack, release.» — Roboto Light, 26 px, white 80%, y=386.
  6. Chip «Part 2 of 3» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1210.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A011: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A008: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Three numbered step cards (4, 5, 6) in a vertical flow with real photo crops of the isolator, the packaging hall and a row of flasks, on emerald with a faint lattice.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «كيف يُصنع الدواء؟» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «الخطوات 4 إلى 6» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الدواء» with kashida (tatweel) for rhythm.
3. Arabic supporting line «التعبئة، والتغليف، والإفراج.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «How a medicine is made.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Fill, pack, release.» — Roboto Light, 26 px, white 80%, y=386.
6. Chip «Part 2 of 3» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1210.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٦» in small Arabic-Indic digits and 1/6 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/6 — step
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Step card 4 with the isolator glove port and the operator behind it, cool light, no label legible.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الخطوة الرابعة |
| Arabic headline 2 | التعبئة |
| Kashida word | التعبئة |
| English headline | Step 4: Fill. |
| Arabic body | تُعبّأ الدفعة المحضّرة في عبواتها، ويعمل المشغّل عبر فتحات القفازات. |
| English body | The prepared batch is filled into its containers. The operator works through glove ports. |

**Typography spec:**

  1. Arabic headline line 1 «الخطوة الرابعة» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «التعبئة» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «التعبئة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تُعبّأ الدفعة المحضّرة في عبواتها، ويعمل المشغّل عبر فتحات القفازات.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Step 4: Fill.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «The prepared batch is filled into its containers. The operator works through glove ports.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A011: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Step card 4 with the isolator glove port and the operator behind it, cool light, no label legible.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوة الرابعة» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «التعبئة» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «التعبئة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تُعبّأ الدفعة المحضّرة في عبواتها، ويعمل المشغّل عبر فتحات القفازات.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Step 4: Fill.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «The prepared batch is filled into its containers. The operator works through glove ports.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٦» in small Arabic-Indic digits and 2/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/6 — step
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Step card 5 with the packaging hall team, women and men, standing at the line, wide frame graded to the emerald palette; no label readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الخطوة الخامسة |
| Arabic headline 2 | التغليف |
| Kashida word | التغليف |
| English headline | Step 5: Pack. |
| Arabic body | يغلّف فريق القاعة الوحدات المعبّأة في عبواتها النهائية. |
| English body | The packaging hall team packs the filled units into their final cartons. |

**Typography spec:**

  1. Arabic headline line 1 «الخطوة الخامسة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «التغليف» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «التغليف» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يغلّف فريق القاعة الوحدات المعبّأة في عبواتها النهائية.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Step 5: Pack.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «The packaging hall team packs the filled units into their final cartons.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Step card 5 with the packaging hall team, women and men, standing at the line, wide frame graded to the emerald palette; no label readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوة الخامسة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «التغليف» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «التغليف» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يغلّف فريق القاعة الوحدات المعبّأة في عبواتها النهائية.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Step 5: Pack.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «The packaging hall team packs the filled units into their final cartons.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٦» in small Arabic-Indic digits and 3/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/6 — step
**Treatment:** T1 Glass object · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A single closed batch file with a mint tab resting beside a clear glass flask with no label, on a glossy emerald floor, soft studio light from the upper left, shallow depth of field.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الخطوة السادسة |
| Arabic headline 2 | الإفراج |
| Kashida word | الإفراج |
| English headline | Step 6: Release. |
| Arabic body | تُفرَج الدفعة بعد مراجعة سجلّاتها، ثم تغادر المصنع. |
| English body | A batch is released once its records have been reviewed. Then it leaves the plant. |

**Typography spec:**

  1. Arabic headline line 1 «الخطوة السادسة» — AE_Sharjah-style heavy geometric kufi, 128 px, #FFFFFF, centred at y=170.
  2. Arabic headline line 2 «الإفراج» — same family, 84 px, mint #8EF0B0, y=320. Stretch the word «الإفراج» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تُفرَج الدفعة بعد مراجعة سجلّاتها، ثم تغادر المصنع.» — Muna Regular, 40 px, white 90%, centred, y=420.
  4. English line «Step 6: Release.» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=430.
  5. English support line «A batch is released once its records have been reviewed. Then it leaves the plant.» — Roboto Light, 28 px, white 80%, y=476.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A008: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A single closed batch file with a mint tab resting beside a clear glass flask with no label, on a glossy emerald floor, soft studio light from the upper left, shallow depth of field.

TREATMENT T1, Glass object: Premium 3D render of the hero object, semi-transparent glass and brushed metal, soft studio light from the upper left, mint rim light, clean reflections on a glossy emerald floor, shallow depth of field. Emerald gradient background from #09A45B (top-left glow) to #04301F (bottom-right), faint rounded-diamond lattice at 8% opacity. Hero centred, 55% of tile height, 90 px free space around it.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوة السادسة» — AE_Sharjah-style heavy geometric kufi, 128 px, #FFFFFF, centred at y=170.
2. Arabic headline line 2 «الإفراج» — same family, 84 px, mint #8EF0B0, y=320. Stretch the word «الإفراج» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تُفرَج الدفعة بعد مراجعة سجلّاتها، ثم تغادر المصنع.» — Muna Regular, 40 px, white 90%, centred, y=420.
4. English line «Step 6: Release.» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=430.
5. English support line «A batch is released once its records have been reviewed. Then it leaves the plant.» — Roboto Light, 28 px, white 80%, y=476.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٦» in small Arabic-Indic digits and 4/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/6 — idea
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald with a thin mint rule and one small line icon of a route with three nodes; no photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | ست خطوات حتى الآن |
| Arabic headline 2 | والسابعة قادمة |
| Kashida word | خطوات |
| English headline | Six steps so far. |
| Arabic body | الخطوات من الأولى إلى الثالثة في منشور الأسبوع الماضي. |
| English body | Steps 1 to 3 are in last week's post. Step 7 comes later this month. |

**Typography spec:**

  1. Arabic headline line 1 «ست خطوات حتى الآن» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «والسابعة قادمة» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «خطوات» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الخطوات من الأولى إلى الثالثة في منشور الأسبوع الماضي.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Six steps so far.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Steps 1 to 3 are in last week's post. Step 7 comes later this month.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald with a thin mint rule and one small line icon of a route with three nodes; no photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ست خطوات حتى الآن» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «والسابعة قادمة» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «خطوات» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الخطوات من الأولى إلى الثالثة في منشور الأسبوع الماضي.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Six steps so far.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Steps 1 to 3 are in last week's post. Step 7 comes later this month.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٦» in small Arabic-Indic digits and 5/6 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 6/6 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | تُرى |
| English headline | Visible capability. Measurable impact. |
| Arabic body | هل فاجأتكم خطوة؟ أخبرونا أيّها في التعليقات. |
| English body | Did a step surprise you? Tell us which one in the comments. |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «هل فاجأتكم خطوة؟ أخبرونا أيّها في التعليقات.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Did a step surprise you? Tell us which one in the comments.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
3. Arabic supporting line «هل فاجأتكم خطوة؟ أخبرونا أيّها في التعليقات.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Did a step surprise you? Tell us which one in the comments.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 6 of 6. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٦/٦» in small Arabic-Indic digits and 6/6 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### JAN-F05 — Seven steps, no secrets ⚠ CLAIM REVIEW
- **Date:** 2027-01-12  |  **Channel:** Instagram + Facebook  |  **Format:** Carousel, 5 slides  |  **Pillar:** How it is made
- ⚠ **Client must verify:** Verify the seven-step route exactly as stated (1 materials tested before use, 2 weighed, dispensed and recorded, 3 made in a controlled room, 4 filled behind a barrier through glove ports, 5 packed and checked on the line, 6 released on the reviewed record, 7 leaves the plant) against the actual process, and that a written record exists at every step.
- **Caption (AR):**

> من وصول المادة إلى مغادرة التشغيلة: سبع خطوات بترتيبها.
> مرّروا لتروا كل خطوة، وفي كل واحدة سجلٌّ مكتوب.
> أي خطوة تودّون أن نشرحها أكثر؟

- **Caption (EN):**

> From a material arriving to a batch leaving: seven steps, in order.
> Swipe to see each one. Every step leaves a written record.
> Which step would you like us to explain further?

- **Hashtags:** #سدير_للأدوية #SudairPharma #سبع_خطوات #SevenSteps #كيف_يصنع_الدواء

#### Slide 1/5 — hook
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Seven numbered nodes joined by a thin mint line, the seventh glowing, over a faint crop of the clean-room corridor (A003).

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | سبع خطوات |
| Arabic headline 2 | بلا أسرار |
| Kashida word | سبع |
| English headline | Seven steps. No secrets. |
| Arabic body | هكذا يُصنع الدواء، بالترتيب. |
| English body | How a medicine is made, in order. |

**Typography spec:**

  1. Arabic headline line 1 «سبع خطوات» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «بلا أسرار» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «سبع» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «هكذا يُصنع الدواء، بالترتيب.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Seven steps. No secrets.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «How a medicine is made, in order.» — Roboto Light, 26 px, white 80%, y=386.
  6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1210.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A003: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Seven numbered nodes joined by a thin mint line, the seventh glowing, over a faint crop of the clean-room corridor (A003).

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «سبع خطوات» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «بلا أسرار» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «سبع» with kashida (tatweel) for rhythm.
3. Arabic supporting line «هكذا يُصنع الدواء، بالترتيب.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Seven steps. No secrets.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «How a medicine is made, in order.» — Roboto Light, 26 px, white 80%, y=386.
6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1210.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — step
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Three step cards joined by the mint line, numbered 1 to 3, each with a small real crop: flasks (A008), a gloved hand beside a flask row (A009), an operator in a clean-room suit (A012).

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الخطوات 1 إلى 3 |
| Arabic headline 2 | قبل الخط |
| Kashida word | الخطوات |
| English headline | Steps 1 to 3 |
| Arabic body | 1 تُفحص المواد قبل استخدامها · 2 تُوزن وتُسجَّل · 3 تُصنَّع في غرفة مضبوطة |
| English body | 1 Materials are tested before use · 2 Weighed, dispensed and recorded · 3 Made in a controlled room |

**Typography spec:**

  1. Arabic headline line 1 «الخطوات 1 إلى 3» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «قبل الخط» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الخطوات» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «1 تُفحص المواد قبل استخدامها · 2 تُوزن وتُسجَّل · 3 تُصنَّع في غرفة مضبوطة» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Steps 1 to 3» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «1 Materials are tested before use · 2 Weighed, dispensed and recorded · 3 Made in a controlled room» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A008: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A009: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A012: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Three step cards joined by the mint line, numbered 1 to 3, each with a small real crop: flasks (A008), a gloved hand beside a flask row (A009), an operator in a clean-room suit (A012).

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوات 1 إلى 3» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «قبل الخط» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الخطوات» with kashida (tatweel) for rhythm.
3. Arabic supporting line «1 تُفحص المواد قبل استخدامها · 2 تُوزن وتُسجَّل · 3 تُصنَّع في غرفة مضبوطة» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Steps 1 to 3» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «1 Materials are tested before use · 2 Weighed, dispensed and recorded · 3 Made in a controlled room» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — step
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Two step cards numbered 4 and 5 with real crops: an operator at an isolator glove port behind barrier glass (A011) and the packaging hall with women and men along the line (A013).

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الخطوتان 4 و5 |
| Arabic headline 2 | تعبئة وتغليف |
| Kashida word | تعبئة |
| English headline | Steps 4 and 5 |
| Arabic body | 4 تُعبّأ خلف حاجز، عبر فتحات القفازات · 5 تُغلَّف وتُفحص على الخط |
| English body | 4 Filled behind a barrier, through glove ports · 5 Packed and checked on the line |

**Typography spec:**

  1. Arabic headline line 1 «الخطوتان 4 و5» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «تعبئة وتغليف» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «تعبئة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «4 تُعبّأ خلف حاجز، عبر فتحات القفازات · 5 تُغلَّف وتُفحص على الخط» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Steps 4 and 5» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «4 Filled behind a barrier, through glove ports · 5 Packed and checked on the line» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A011: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Two step cards numbered 4 and 5 with real crops: an operator at an isolator glove port behind barrier glass (A011) and the packaging hall with women and men along the line (A013).

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوتان 4 و5» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «تعبئة وتغليف» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «تعبئة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «4 تُعبّأ خلف حاجز، عبر فتحات القفازات · 5 تُغلَّف وتُفحص على الخط» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Steps 4 and 5» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «4 Filled behind a barrier, through glove ports · 5 Packed and checked on the line» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — proof
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A 3D glass sealed record folder with a mint ribbon seal beside the real wide drone view of the whole site (A002) in teal-green grade; node 7 glowing at the lower edge.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | الخطوتان 6 و7 |
| Arabic headline 2 | من الإفراج إلى الخروج |
| Kashida word | الإفراج |
| English headline | Steps 6 and 7 |
| Arabic body | 6 تُفرج على سجلّها المراجَع · 7 تغادر المصنع |
| English body | 6 Released on its reviewed record · 7 Leaves the plant |

**Typography spec:**

  1. Arabic headline line 1 «الخطوتان 6 و7» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «من الإفراج إلى الخروج» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الإفراج» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «6 تُفرج على سجلّها المراجَع · 7 تغادر المصنع» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Steps 6 and 7» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «6 Released on its reviewed record · 7 Leaves the plant» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A 3D glass sealed record folder with a mint ribbon seal beside the real wide drone view of the whole site (A002) in teal-green grade; node 7 glowing at the lower edge.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوتان 6 و7» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «من الإفراج إلى الخروج» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الإفراج» with kashida (tatweel) for rhythm.
3. Arabic supporting line «6 تُفرج على سجلّها المراجَع · 7 تغادر المصنع» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Steps 6 and 7» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «6 Released on its reviewed record · 7 Leaves the plant» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, hairline frame, thin mint rule, the small white palm-burst symbol.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | صناعة |
| English headline | Visible capability. Measurable impact. |
| Arabic body | تابعونا لنفصّل لكم كل خطوة. |
| English body | Follow along. We will take each step apart. |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «صناعة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تابعونا لنفصّل لكم كل خطوة.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Follow along. We will take each step apart.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Seven steps, January 2027» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, hairline frame, thin mint rule, the small white palm-burst symbol.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «صناعة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تابعونا لنفصّل لكم كل خطوة.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Follow along. We will take each step apart.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Seven steps, January 2027» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### JAN-L04 — Release: the paperwork is the product ⚠ CLAIM REVIEW
- **Date:** 2027-01-13  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Quality and trust
- ⚠ **Client must verify:** Client must verify that release at Sudair follows a review of the batch record by a responsible person, and approve the statement that the documentation is part of the product, before this carousel is used.
- **Caption (AR):**

> قبل أن تغادر الدفعة المصنع، يكون لها ملف.
> في مرحلة الإفراج يُقرأ هذا الملف ويُراجَع، وبذلك يصبح التوثيق جزءًا من المنتج.
> أي خطوة تودّون أن نشرحها بعد ذلك؟

- **Caption (EN):**

> Before a batch leaves the plant, it has a file.
> At release that file is read and reviewed, so the paperwork is part of the product.
> Which step would you like us to explain next?

- **Hashtags:** #سدير_للأدوية #SudairPharma #الإفراج #BatchRelease

#### Slide 1/5 — hook
**Treatment:** T1 Glass object · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** One closed batch file with a mint ribbon tab beside a clear glass flask with no label, on a glossy emerald floor; headline in the clear space above.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | التوثيق جزء من المنتج |
| Arabic headline 2 | مرحلة الإفراج |
| Kashida word | التوثيق |
| English headline | The paperwork is the product. |
| Arabic body | الخطوة السادسة من الخط: الإفراج. |
| English body | Step 6 of the line: release. |

**Typography spec:**

  1. Arabic headline line 1 «التوثيق جزء من المنتج» — AE_Sharjah-style heavy geometric kufi, 128 px, #FFFFFF, centred at y=170.
  2. Arabic headline line 2 «مرحلة الإفراج» — same family, 84 px, mint #8EF0B0, y=320. Stretch the word «التوثيق» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الخطوة السادسة من الخط: الإفراج.» — Muna Regular, 40 px, white 90%, centred, y=420.
  4. English line «The paperwork is the product.» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=430.
  5. English support line «Step 6 of the line: release.» — Roboto Light, 28 px, white 80%, y=476.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): One closed batch file with a mint ribbon tab beside a clear glass flask with no label, on a glossy emerald floor; headline in the clear space above.

TREATMENT T1, Glass object: Premium 3D render of the hero object, semi-transparent glass and brushed metal, soft studio light from the upper left, mint rim light, clean reflections on a glossy emerald floor, shallow depth of field. Emerald gradient background from #09A45B (top-left glow) to #04301F (bottom-right), faint rounded-diamond lattice at 8% opacity. Hero centred, 55% of tile height, 90 px free space around it.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «التوثيق جزء من المنتج» — AE_Sharjah-style heavy geometric kufi, 128 px, #FFFFFF, centred at y=170.
2. Arabic headline line 2 «مرحلة الإفراج» — same family, 84 px, mint #8EF0B0, y=320. Stretch the word «التوثيق» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الخطوة السادسة من الخط: الإفراج.» — Muna Regular, 40 px, white 90%, centred, y=420.
4. English line «The paperwork is the product.» — Friz Quadrata Bold / italic condensed sans, 32 px, uppercase, white 90%, tracking +40, y=430.
5. English support line «Step 6 of the line: release.» — Roboto Light, 28 px, white 80%, y=476.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Three rounded cream cards with a lime edge, each with a friendly 3D character in green clothing: one writing in a file, one reading it, one placing it in a cabinet; no readable text on the files.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | لكل دفعة ملفّها |
| Arabic headline 2 | يُكتب أثناء العمل |
| Kashida word | ملفّها |
| English headline | Every batch has a file. |
| Arabic body | يُكتب أثناء العمل، ويُقرأ قبل الإفراج، ويُحفظ مع الدفعة. |
| English body | Written as the work happens. Read before release. Kept with the batch. |

**Typography spec:**

  1. Arabic headline line 1 «لكل دفعة ملفّها» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «يُكتب أثناء العمل» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «ملفّها» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يُكتب أثناء العمل، ويُقرأ قبل الإفراج، ويُحفظ مع الدفعة.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Every batch has a file.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  5. English support line «Written as the work happens. Read before release. Kept with the batch.» — Roboto Light, 26 px, white 80%, y=406.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Three rounded cream cards with a lime edge, each with a friendly 3D character in green clothing: one writing in a file, one reading it, one placing it in a cabinet; no readable text on the files.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «لكل دفعة ملفّها» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «يُكتب أثناء العمل» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «ملفّها» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يُكتب أثناء العمل، ويُقرأ قبل الإفراج، ويُحفظ مع الدفعة.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Every batch has a file.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
5. English support line «Written as the work happens. Read before release. Kept with the batch.» — Roboto Light, 26 px, white 80%, y=406.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — step
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald with a thin mint rule and one small white line icon of an open file; no photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | يُقرأ الملف |
| Arabic headline 2 | قبل الإفراج |
| Kashida word | الملف |
| English headline | The file is read. |
| Arabic body | يطّلع مسؤول مختص على سجلّ الدفعة من أوله إلى آخره. |
| English body | A responsible person reads the batch record from start to finish. |

**Typography spec:**

  1. Arabic headline line 1 «يُقرأ الملف» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «قبل الإفراج» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «الملف» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يطّلع مسؤول مختص على سجلّ الدفعة من أوله إلى آخره.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «The file is read.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «A responsible person reads the batch record from start to finish.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald with a thin mint rule and one small white line icon of an open file; no photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «يُقرأ الملف» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «قبل الإفراج» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «الملف» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يطّلع مسؤول مختص على سجلّ الدفعة من أوله إلى آخره.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «The file is read.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «A responsible person reads the batch record from start to finish.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Three step nodes joined by a thin mint line labelled Made, Documented, Released, with small real crops: a row of flasks, the clean-room corridor, the site from the air.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | الإفراج قرار |
| Arabic headline 2 | يُتخذ بعد المراجعة |
| Kashida word | قرار |
| English headline | Release is a decision. |
| Arabic body | تُصنَع الدفعة، ثم تُوثَّق، ثم تُفرَج. |
| English body | Made, then documented, then released. |

**Typography spec:**

  1. Arabic headline line 1 «الإفراج قرار» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «يُتخذ بعد المراجعة» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «قرار» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تُصنَع الدفعة، ثم تُوثَّق، ثم تُفرَج.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Release is a decision.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Made, then documented, then released.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A008: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A003: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Three step nodes joined by a thin mint line labelled Made, Documented, Released, with small real crops: a row of flasks, the clean-room corridor, the site from the air.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الإفراج قرار» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «يُتخذ بعد المراجعة» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «قرار» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تُصنَع الدفعة، ثم تُوثَّق، ثم تُفرَج.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Release is a decision.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Made, then documented, then released.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | تُرى |
| English headline | Visible capability. Measurable impact. |
| Arabic body | سلسلة «سبع خطوات بلا أسرار» تستمر على هذه الصفحة. |
| English body | The Seven steps, no secrets series continues on this page. |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «سلسلة «سبع خطوات بلا أسرار» تستمر على هذه الصفحة.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «The Seven steps, no secrets series continues on this page.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
3. Arabic supporting line «سلسلة «سبع خطوات بلا أسرار» تستمر على هذه الصفحة.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «The Seven steps, no secrets series continues on this page.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### JAN-L05 — Technology in manufacturing ⚠ CLAIM REVIEW
- **Date:** 2027-01-18  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Local manufacturing
- ⚠ **Client must verify:** Client must confirm that an isolator with glove ports, clean rooms with controlled air and surfaces, and automated lines with team-set-up equipment are in use at the plant, and that each plain-language description is accurate.
- **Caption (AR):**

> ثلاثة أشياء تراها على خط التصنيع، بكلمات بسيطة: وحدة العزل، والغرفة النظيفة، والخط الآلي.
> خلف كل واحدة منها فريق يعمل بها.
> ما التقنية التي تودّون معرفة المزيد عنها؟

- **Caption (EN):**

> Three things you can see on a manufacturing line, in plain words: the isolator, the clean room and the automated line.
> Behind each one there is a team that works with it.
> Which would you like to know more about?

- **Hashtags:** #سدير_للأدوية #SudairPharma #التصنيع_الدوائي #PharmaManufacturing #صناعة_سعودية

#### Slide 1/5 — hook
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Three rounded cream cards with a lime edge and friendly 3D green-clad characters beside a glove-port enclosure, a clean-room doorway and a machine line; headline clear at the top.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | التقنية في التصنيع |
| Arabic headline 2 | كما تُرى على الخط |
| Kashida word | التقنية |
| English headline | Technology in manufacturing. |
| Arabic body | ثلاث أدوات، وفريق يعمل بها. |
| English body | Three tools, and the team that works with them. |

**Typography spec:**

  1. Arabic headline line 1 «التقنية في التصنيع» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «كما تُرى على الخط» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «التقنية» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «ثلاث أدوات، وفريق يعمل بها.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Technology in manufacturing.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  5. English support line «Three tools, and the team that works with them.» — Roboto Light, 26 px, white 80%, y=406.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Three rounded cream cards with a lime edge and friendly 3D green-clad characters beside a glove-port enclosure, a clean-room doorway and a machine line; headline clear at the top.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «التقنية في التصنيع» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «كما تُرى على الخط» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «التقنية» with kashida (tatweel) for rhythm.
3. Arabic supporting line «ثلاث أدوات، وفريق يعمل بها.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Technology in manufacturing.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
5. English support line «Three tools, and the team that works with them.» — Roboto Light, 26 px, white 80%, y=406.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The isolator glove port with the operator behind it, three-quarter view, cool key light from the left, dark green panel on the right for text; no label legible.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4

| Element | String |
|---|---|
| Arabic headline 1 | وحدة العزل |
| Arabic headline 2 | عمل عبر القفازات |
| Kashida word | العزل |
| English headline | The isolator |
| Arabic body | حيّز مغلق بفتحات قفازات، يعمل المشغّل من خلالها. |
| English body | A sealed enclosure with glove ports. The operator works through the gloves. |

**Typography spec:**

  1. Arabic headline line 1 «وحدة العزل» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «عمل عبر القفازات» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «العزل» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «حيّز مغلق بفتحات قفازات، يعمل المشغّل من خلالها.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «The isolator» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «A sealed enclosure with glove ports. The operator works through the gloves.» — Roboto Light, 26 px, white 80%, y=746.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A011: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The isolator glove port with the operator behind it, three-quarter view, cool key light from the left, dark green panel on the right for text; no label legible.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وحدة العزل» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «عمل عبر القفازات» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «العزل» with kashida (tatweel) for rhythm.
3. Arabic supporting line «حيّز مغلق بفتحات قفازات، يعمل المشغّل من خلالها.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «The isolator» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «A sealed enclosure with glove ports. The operator works through the gloves.» — Roboto Light, 26 px, white 80%, y=746.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The empty clean-room corridor in cool light with a small crop of an operator in a full suit as an inset; long perspective, no signage readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الغرفة النظيفة |
| Arabic headline 2 | يُدخل إليها بزيّ كامل |
| Kashida word | النظيفة |
| English headline | The clean room |
| Arabic body | غرفة مصمّمة للتحكم في الهواء والأسطح، ويدخلها العاملون بزيّ كامل. |
| English body | A room built to control the air and the surfaces. People enter in a full suit. |

**Typography spec:**

  1. Arabic headline line 1 «الغرفة النظيفة» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «يُدخل إليها بزيّ كامل» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «النظيفة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «غرفة مصمّمة للتحكم في الهواء والأسطح، ويدخلها العاملون بزيّ كامل.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «The clean room» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «A room built to control the air and the surfaces. People enter in a full suit.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A003: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A012: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The empty clean-room corridor in cool light with a small crop of an operator in a full suit as an inset; long perspective, no signage readable.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الغرفة النظيفة» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «يُدخل إليها بزيّ كامل» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «النظيفة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «غرفة مصمّمة للتحكم في الهواء والأسطح، ويدخلها العاملون بزيّ كامل.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «The clean room» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «A room built to control the air and the surfaces. People enter in a full suit.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The packaging hall team, women and men, standing at the line, wide frame graded to the emerald palette; equipment visible, no label readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الخط الآلي |
| Arabic headline 2 | بأيدٍ تُشغّله |
| Kashida word | الآلي |
| English headline | The automated line |
| Arabic body | تكرّر الآلات الخطوات نفسها، ويضبطها الفريق ويراقبها. |
| English body | Machines repeat the same steps. The team sets them up and watches them. |

**Typography spec:**

  1. Arabic headline line 1 «الخط الآلي» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «بأيدٍ تُشغّله» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الآلي» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تكرّر الآلات الخطوات نفسها، ويضبطها الفريق ويراقبها.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «The automated line» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Machines repeat the same steps. The team sets them up and watches them.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The packaging hall team, women and men, standing at the line, wide frame graded to the emerald palette; equipment visible, no label readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخط الآلي» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «بأيدٍ تُشغّله» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الآلي» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تكرّر الآلات الخطوات نفسها، ويضبطها الفريق ويراقبها.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «The automated line» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Machines repeat the same steps. The team sets them up and watches them.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | تُرى |
| English headline | Visible capability. Measurable impact. |
| Arabic body | أي تقنية تودّون أن نعرضها بتفصيل أكبر؟ |
| English body | Which technology would you like us to show in more detail? |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «أي تقنية تودّون أن نعرضها بتفصيل أكبر؟» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Which technology would you like us to show in more detail?» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
3. Arabic supporting line «أي تقنية تودّون أن نعرضها بتفصيل أكبر؟» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Which technology would you like us to show in more detail?» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### JAN-L06 — People and machines, side by side
- **Date:** 2027-01-20  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** Meet the makers
- **Caption (AR):**

> خلف كل آلة في المصنع إنسان يعرفها.
> نشكر هذا الأسبوع فرق قاعة التغليف والغرفة النظيفة والمختبر.
> من تودّون أن نعرّفكم إليه؟

- **Caption (EN):**

> Behind every machine in the plant there is a person who knows it.
> This week we thank the packaging hall, clean room and lab teams.
> Who would you like us to introduce?

- **Hashtags:** #سدير_للأدوية #SudairPharma #فريق_سدير #MeetTheTeam

#### Slide 1/5 — hook
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The packaging hall team, women and men, standing together beside the line, wide frame graded to the emerald palette; no label readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | إنسان وآلة |
| Arabic headline 2 | جنبًا إلى جنب |
| Kashida word | جنبًا |
| English headline | People and machines, side by side. |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «إنسان وآلة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «جنبًا إلى جنب» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «جنبًا» with kashida (tatweel) for rhythm.
  3. English line «People and machines, side by side.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The packaging hall team, women and men, standing together beside the line, wide frame graded to the emerald palette; no label readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «إنسان وآلة» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «جنبًا إلى جنب» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «جنبًا» with kashida (tatweel) for rhythm.
3. English line «People and machines, side by side.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** An operator in a full clean-room suit, three-quarter view, calm look, cool key light from the left, dark green panel on the right for text.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4

| Element | String |
|---|---|
| Arabic headline 1 | في الغرفة النظيفة |
| Arabic headline 2 | مشغّل بزيّ كامل |
| Kashida word | النظيفة |
| English headline | In the clean room |
| Arabic body | لكل غرفة من يعرفها ويعمل فيها كل يوم. |
| English body | Every room has someone who knows it and works in it every day. |

**Typography spec:**

  1. Arabic headline line 1 «في الغرفة النظيفة» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «مشغّل بزيّ كامل» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «النظيفة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «لكل غرفة من يعرفها ويعمل فيها كل يوم.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «In the clean room» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «Every room has someone who knows it and works in it every day.» — Roboto Light, 26 px, white 80%, y=746.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A012: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8892.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): An operator in a full clean-room suit, three-quarter view, calm look, cool key light from the left, dark green panel on the right for text.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «في الغرفة النظيفة» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «مشغّل بزيّ كامل» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «النظيفة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «لكل غرفة من يعرفها ويعمل فيها كل يوم.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «In the clean room» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «Every room has someone who knows it and works in it every day.» — Roboto Light, 26 px, white 80%, y=746.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A lab analyst at the bench, focused, soft key light from the left, dark green panel on the right for text; no label legible on any container.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | على طاولة المختبر |
| Arabic headline 2 | محلّل عند عمله |
| Kashida word | طاولة |
| English headline | At the lab bench |
| Arabic body | محلّل في مختبر المصنع عند طاولة عمله. |
| English body | An analyst at the bench in the plant lab. |

**Typography spec:**

  1. Arabic headline line 1 «على طاولة المختبر» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «محلّل عند عمله» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «طاولة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «محلّل في مختبر المصنع عند طاولة عمله.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «At the lab bench» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «An analyst at the bench in the plant lab.» — Roboto Light, 26 px, white 80%, y=746.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A lab analyst at the bench, focused, soft key light from the left, dark green panel on the right for text; no label legible on any container.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «على طاولة المختبر» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «محلّل عند عمله» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «طاولة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «محلّل في مختبر المصنع عند طاولة عمله.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «At the lab bench» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «An analyst at the bench in the plant lab.» — Roboto Light, 26 px, white 80%, y=746.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald with a thin mint rule and one small white line icon of two hands; no photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | بجانب كل آلة |
| Arabic headline 2 | إنسان |
| Kashida word | بجانب |
| English headline | Beside every machine, a person. |
| Arabic body | الآلات جزء من المكان، والفريق هو من يعمل بها. |
| English body | The machines are part of the place. The team is who works with them. |

**Typography spec:**

  1. Arabic headline line 1 «بجانب كل آلة» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «إنسان» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «بجانب» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الآلات جزء من المكان، والفريق هو من يعمل بها.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Beside every machine, a person.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «The machines are part of the place. The team is who works with them.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald with a thin mint rule and one small white line icon of two hands; no photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «بجانب كل آلة» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «إنسان» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «بجانب» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الآلات جزء من المكان، والفريق هو من يعمل بها.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Beside every machine, a person.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «The machines are part of the place. The team is who works with them.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | تُرى |
| English headline | Visible capability. Measurable impact. |
| Arabic body | شكرًا لكل من يعمل في المصنع. من تودّون أن تتعرّفوا إليه من الفريق؟ |
| English body | Thank you to everyone who works in the plant. Who from the team would you like to meet? |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «شكرًا لكل من يعمل في المصنع. من تودّون أن تتعرّفوا إليه من الفريق؟» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Thank you to everyone who works in the plant. Who from the team would you like to meet?» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
3. Arabic supporting line «شكرًا لكل من يعمل في المصنع. من تودّون أن تتعرّفوا إليه من الفريق؟» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Thank you to everyone who works in the plant. Who from the team would you like to meet?» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### JAN-F09 — The unglamorous half of innovation ⚠ CLAIM REVIEW
- **Date:** 2027-01-21  |  **Channel:** Instagram + Facebook  |  **Format:** Carousel, 5 slides  |  **Pillar:** Quality and trust
- ⚠ **Client must verify:** Verify that new equipment at Sudair City is installed, run in a documented trial, recorded, and then serviced and calibrated on a schedule, exactly as the slides state.
- **Caption (AR):**

> الابتكار ليس جهازًا جديدًا فقط: هو تركيبٌ، ثم تجربة، ثم تسجيل، ثم صيانةٌ دورية.
> النصف الذي لا يلمع هو الذي يبقي العمل مستمرًّا.
> مرّروا لترى كل مرحلة.

- **Caption (EN):**

> Innovation is not only a new machine: it is installing, trying out, recording and then regular upkeep.
> The half that does not shine is the half that keeps the work going.
> Swipe to see each stage.

- **Hashtags:** #سدير_للأدوية #SudairPharma #التقنية #Technology #صناعة_سعودية

#### Slide 1/5 — hook
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A rounded cream card with a lime edge: a friendly 3D character in green clothing with a spanner beside a glass-and-metal machine part, on emerald with faint lattice.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | نصف الابتكار |
| Arabic headline 2 | لا يلمع |
| Kashida word | الابتكار |
| English headline | The unglamorous half of innovation. |
| Arabic body | شراء الجهاز هو الجزء السهل. |
| English body | Buying the machine is the easy part. |

**Typography spec:**

  1. Arabic headline line 1 «نصف الابتكار» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «لا يلمع» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «الابتكار» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «شراء الجهاز هو الجزء السهل.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «The unglamorous half of innovation.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  5. English support line «Buying the machine is the easy part.» — Roboto Light, 26 px, white 80%, y=406.
  6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): A rounded cream card with a lime edge: a friendly 3D character in green clothing with a spanner beside a glass-and-metal machine part, on emerald with faint lattice.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «نصف الابتكار» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «لا يلمع» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «الابتكار» with kashida (tatweel) for rhythm.
3. Arabic supporting line «شراء الجهاز هو الجزء السهل.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «The unglamorous half of innovation.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
5. English support line «Buying the machine is the easy part.» — Roboto Light, 26 px, white 80%, y=406.
6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1190.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — step
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A cream card: a 3D character at a control panel, a small real crop of the corridor (A003) at the card edge; label at the left.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | أولًا: يُركَّب |
| Arabic headline 2 | ثم يُجرَّب |
| Kashida word | يُجرَّب |
| English headline | Installed, then tried out. |
| Arabic body | يُركَّب الجهاز الجديد، ثم يُشغَّل تجربةً ليظهر أنه يعمل كما أُعدّ له. |
| English body | New equipment is installed, then run as a trial to show it works as it was set up to. |

**Typography spec:**

  1. Arabic headline line 1 «أولًا: يُركَّب» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «ثم يُجرَّب» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «يُجرَّب» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يُركَّب الجهاز الجديد، ثم يُشغَّل تجربةً ليظهر أنه يعمل كما أُعدّ له.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Installed, then tried out.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  5. English support line «New equipment is installed, then run as a trial to show it works as it was set up to.» — Roboto Light, 26 px, white 80%, y=406.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A003: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A cream card: a 3D character at a control panel, a small real crop of the corridor (A003) at the card edge; label at the left.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «أولًا: يُركَّب» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «ثم يُجرَّب» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «يُجرَّب» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يُركَّب الجهاز الجديد، ثم يُشغَّل تجربةً ليظهر أنه يعمل كما أُعدّ له.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Installed, then tried out.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
5. English support line «New equipment is installed, then run as a trial to show it works as it was set up to.» — Roboto Light, 26 px, white 80%, y=406.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — step
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A cream card: a 3D character writing in a logbook beside a flask row; a small real crop of the bench (A009) at the card edge.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4

| Element | String |
|---|---|
| Arabic headline 1 | ثم يُكتب |
| Arabic headline 2 | كل شيء |
| Kashida word | يُكتب |
| English headline | Then written down. |
| Arabic body | تُسجَّل كل تجربة، وكل ضبط، وكل نتيجة. |
| English body | Each trial, each setting and each result is recorded. |

**Typography spec:**

  1. Arabic headline line 1 «ثم يُكتب» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «كل شيء» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «يُكتب» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تُسجَّل كل تجربة، وكل ضبط، وكل نتيجة.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Then written down.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  5. English support line «Each trial, each setting and each result is recorded.» — Roboto Light, 26 px, white 80%, y=406.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A009: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A cream card: a 3D character writing in a logbook beside a flask row; a small real crop of the bench (A009) at the card edge.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ثم يُكتب» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «كل شيء» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «يُكتب» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تُسجَّل كل تجربة، وكل ضبط، وكل نتيجة.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Then written down.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
5. English support line «Each trial, each setting and each result is recorded.» — Roboto Light, 26 px, white 80%, y=406.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — step
**Treatment:** T4 Card explainer · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A cream card: a 3D character with a toolkit by a machine, a calendar icon on the card; a small real crop of the bench (A007) at the edge.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | ثم يُصان |
| Arabic headline 2 | بانتظام |
| Kashida word | يُصان |
| English headline | Then looked after. |
| Arabic body | يُصان الجهاز ويُضبط في مواعيد محددة. |
| English body | The equipment is serviced and calibrated on a schedule. |

**Typography spec:**

  1. Arabic headline line 1 «ثم يُصان» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «بانتظام» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «يُصان» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يُصان الجهاز ويُضبط في مواعيد محددة.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Then looked after.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
  5. English support line «The equipment is serviced and calibrated on a schedule.» — Roboto Light, 26 px, white 80%, y=406.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A cream card: a 3D character with a toolkit by a machine, a calendar icon on the card; a small real crop of the bench (A007) at the edge.

TREATMENT T4, Card explainer: Infographic of rounded cream cards with a lime-green right edge, each card holding a friendly 3D Pixar-style character in green clothing that illustrates the label, soft inner shadow, glossy finish, on an emerald gradient with faint lattice. Two-column grid with a full-width final card.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «ثم يُصان» — AE_Sharjah-style heavy geometric kufi, 92 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «بانتظام» — same family, 64 px, mint #8EF0B0, y=270. Stretch the word «يُصان» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يُصان الجهاز ويُضبط في مواعيد محددة.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Then looked after.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=360.
5. English support line «The equipment is serviced and calibrated on a schedule.» — Roboto Light, 26 px, white 80%, y=406.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald, hairline frame, thin mint rule, the small white palm-burst symbol.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | صناعة |
| English headline | Visible capability. Measurable impact. |
| Arabic body | خلف كل جهازٍ يلمع، عملٌ كثيرٌ لا يُرى. |
| English body | Behind every machine that shines, a lot of work that is not seen. |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «صناعة» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «خلف كل جهازٍ يلمع، عملٌ كثيرٌ لا يُرى.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Behind every machine that shines, a lot of work that is not seen.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «Technology season, January 2027» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald, hairline frame, thin mint rule, the small white palm-burst symbol.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «صناعة» with kashida (tatweel) for rhythm.
3. Arabic supporting line «خلف كل جهازٍ يلمع، عملٌ كثيرٌ لا يُرى.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Behind every machine that shines, a lot of work that is not seen.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «Technology season, January 2027» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### JAN-L07 — Seven steps, no secrets: the full line ⚠ CLAIM REVIEW
- **Date:** 2027-01-25  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 7 slides  |  **Pillar:** How it is made
- ⚠ **Client must verify:** Client must confirm the full seven-step sequence (receive, weigh, prepare, fill, pack, release, ship) and each plain-language step description against the plant's approved process before publication.
- **Caption (AR):**

> سبع خطوات، من وصول المواد إلى خروج الدفعة: الاستلام، الوزن، التحضير، التعبئة، التغليف، الإفراج، الشحن.
> هذا هو الخط كاملًا، وخلف كل خطوة فريق.
> أي خطوة تودّون أن نتوسّع فيها؟

- **Caption (EN):**

> Seven steps, from materials arriving to the batch leaving: receive, weigh, prepare, fill, pack, release, ship.
> That is the full line, and behind every step there is a team.
> Which step would you like us to look at more closely?

- **Hashtags:** #سدير_للأدوية #SudairPharma #سبع_خطوات #SevenSteps #صناعة_سعودية

#### Slide 1/7 — hook
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Seven numbered step cards in a vertical flow with small real photo crops, on emerald with a faint lattice; headline above.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الخطوات السبع |
| Arabic headline 2 | كاملةً |
| Kashida word | الخطوات |
| English headline | The seven steps, in full. |
| Arabic body | الاستلام، الوزن، التحضير، التعبئة، التغليف، الإفراج، الشحن. |
| English body | Receive, weigh, prepare, fill, pack, release, ship. |

**Typography spec:**

  1. Arabic headline line 1 «الخطوات السبع» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «كاملةً» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الخطوات» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «الاستلام، الوزن، التحضير، التعبئة، التغليف، الإفراج، الشحن.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «The seven steps, in full.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Receive, weigh, prepare, fill, pack, release, ship.» — Roboto Light, 26 px, white 80%, y=386.
  6. Chip «Part 3 of 3» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1210.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A009: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A003: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A011: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A008: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Seven numbered step cards in a vertical flow with small real photo crops, on emerald with a faint lattice; headline above.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوات السبع» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «كاملةً» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الخطوات» with kashida (tatweel) for rhythm.
3. Arabic supporting line «الاستلام، الوزن، التحضير، التعبئة، التغليف، الإفراج، الشحن.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «The seven steps, in full.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Receive, weigh, prepare, fill, pack, release, ship.» — Roboto Light, 26 px, white 80%, y=386.
6. Chip «Part 3 of 3» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1210.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 7. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٧» in small Arabic-Indic digits and 1/7 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/7 — step
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Two step cards, 1 and 2, with a generated store of incoming materials and a close crop of a gloved hand beside a row of flasks; no readable labels.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الاستلام والوزن |
| Arabic headline 2 | الخطوتان 1 و2 |
| Kashida word | الاستلام |
| English headline | Steps 1 and 2: Receive and weigh. |
| Arabic body | تصل المواد وتُسجَّل، ثم يُوزن كل مكوّن للدفعة. |
| English body | Materials arrive and are logged. Each ingredient is weighed for the batch. |

**Typography spec:**

  1. Arabic headline line 1 «الاستلام والوزن» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «الخطوتان 1 و2» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الاستلام» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تصل المواد وتُسجَّل، ثم يُوزن كل مكوّن للدفعة.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Steps 1 and 2: Receive and weigh.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Materials arrive and are logged. Each ingredient is weighed for the batch.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A009: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8842.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Two step cards, 1 and 2, with a generated store of incoming materials and a close crop of a gloved hand beside a row of flasks; no readable labels.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الاستلام والوزن» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «الخطوتان 1 و2» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «الاستلام» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تصل المواد وتُسجَّل، ثم يُوزن كل مكوّن للدفعة.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Steps 1 and 2: Receive and weigh.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Materials arrive and are logged. Each ingredient is weighed for the batch.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 7. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٧» in small Arabic-Indic digits and 2/7 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/7 — step
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Two step cards, 3 and 4, with the clean-room corridor and the isolator glove port with an operator behind it; no label legible.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4

| Element | String |
|---|---|
| Arabic headline 1 | التحضير والتعبئة |
| Arabic headline 2 | الخطوتان 3 و4 |
| Kashida word | التحضير |
| English headline | Steps 3 and 4: Prepare and fill. |
| Arabic body | تُجمع المكوّنات في غرفة نظيفة، ثم تُعبّأ الدفعة في عبواتها. |
| English body | Ingredients are combined in a clean room. The batch is then filled into its containers. |

**Typography spec:**

  1. Arabic headline line 1 «التحضير والتعبئة» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «الخطوتان 3 و4» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «التحضير» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تُجمع المكوّنات في غرفة نظيفة، ثم تُعبّأ الدفعة في عبواتها.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Steps 3 and 4: Prepare and fill.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Ingredients are combined in a clean room. The batch is then filled into its containers.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A003: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A011: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8871.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Two step cards, 3 and 4, with the clean-room corridor and the isolator glove port with an operator behind it; no label legible.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «التحضير والتعبئة» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «الخطوتان 3 و4» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «التحضير» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تُجمع المكوّنات في غرفة نظيفة، ثم تُعبّأ الدفعة في عبواتها.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Steps 3 and 4: Prepare and fill.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Ingredients are combined in a clean room. The batch is then filled into its containers.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 7. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٧» in small Arabic-Indic digits and 3/7 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/7 — step
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Two step cards, 5 and 6, with the packaging hall team at the line and a row of unlabelled flasks beside a closed batch file.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4

| Element | String |
|---|---|
| Arabic headline 1 | التغليف والإفراج |
| Arabic headline 2 | الخطوتان 5 و6 |
| Kashida word | التغليف |
| English headline | Steps 5 and 6: Pack and release. |
| Arabic body | تُغلَّف الوحدات، وتُفرَج الدفعة بعد مراجعة سجلّاتها. |
| English body | Units are packed. The batch is released after its records are reviewed. |

**Typography spec:**

  1. Arabic headline line 1 «التغليف والإفراج» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «الخطوتان 5 و6» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «التغليف» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تُغلَّف الوحدات، وتُفرَج الدفعة بعد مراجعة سجلّاتها.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «Steps 5 and 6: Pack and release.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Units are packed. The batch is released after its records are reviewed.» — Roboto Light, 26 px, white 80%, y=386.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A008: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8839.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Two step cards, 5 and 6, with the packaging hall team at the line and a row of unlabelled flasks beside a closed batch file.

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «التغليف والإفراج» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «الخطوتان 5 و6» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «التغليف» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تُغلَّف الوحدات، وتُفرَج الدفعة بعد مراجعة سجلّاتها.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «Steps 5 and 6: Pack and release.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Units are packed. The batch is released after its records are reviewed.» — Roboto Light, 26 px, white 80%, y=386.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 7. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٧» in small Arabic-Indic digits and 4/7 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/7 — step
**Treatment:** T6 Key-visual petal · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Drone view of the Sudair City site at golden hour with one petal-shaped glowing window; headline left on dark emerald. No people.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | الخطوة السابعة |
| Arabic headline 2 | الشحن |
| Kashida word | الشحن |
| English headline | Step 7: Ship. |
| Arabic body | تغادر الدفعة المفرَج عنها المصنع نحو وجهتها. |
| English body | A released batch leaves the plant for its destination. |

**Typography spec:**

  1. Arabic headline line 1 «الخطوة السابعة» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
  2. Arabic headline line 2 «الشحن» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «الشحن» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تغادر الدفعة المفرَج عنها المصنع نحو وجهتها.» — Muna Regular, 40 px, white 90%, centred, y=540.
  4. English line «Step 7: Ship.» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
  5. English support line «A released batch leaves the plant for its destination.» — Roboto Light, 34 px, white 80%, y=626.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Drone view of the Sudair City site at golden hour with one petal-shaped glowing window; headline left on dark emerald. No people.

TREATMENT T6, Key-visual petal: Main theme key visual treatment: dark emerald left side fading to a Saudi dusk landscape on the right, three tall petal-shaped glowing windows in a fan above a modern pharmaceutical campus with palms and warm walkway lights, the scenes of the message visible inside the petals, a father and child walking toward the building, soft mist, mint rim light on the petal edges.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخطوة السابعة» — AE_Sharjah-style heavy geometric kufi, 120 px, #FFFFFF, right-aligned inside the left column x 60 to 600 at y=280.
2. Arabic headline line 2 «الشحن» — same family, 84 px, mint #8EF0B0, y=440. Stretch the word «الشحن» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تغادر الدفعة المفرَج عنها المصنع نحو وجهتها.» — Muna Regular, 40 px, white 90%, centred, y=540.
4. English line «Step 7: Ship.» — Friz Quadrata Bold / italic condensed sans, 38 px, uppercase, white 90%, tracking +40, y=580.
5. English support line «A released batch leaves the plant for its destination.» — Roboto Light, 34 px, white 80%, y=626.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 7. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٧» in small Arabic-Indic digits and 5/7 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 6/7 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab team standing together in the lab, relaxed and proud, wide frame graded to the emerald palette; no label legible.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4

| Element | String |
|---|---|
| Arabic headline 1 | سبع خطوات |
| Arabic headline 2 | وأيادٍ كثيرة |
| Kashida word | أيادٍ |
| English headline | Seven steps, many hands. |
| Arabic body | وراء كل خطوة فريق يعمل بها كل يوم. |
| English body | Behind every step is a team that works on it every day. |

**Typography spec:**

  1. Arabic headline line 1 «سبع خطوات» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «وأيادٍ كثيرة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «أيادٍ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «وراء كل خطوة فريق يعمل بها كل يوم.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Seven steps, many hands.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Behind every step is a team that works on it every day.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A005: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8829.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab team standing together in the lab, relaxed and proud, wide frame graded to the emerald palette; no label legible.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «سبع خطوات» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «وأيادٍ كثيرة» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «أيادٍ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «وراء كل خطوة فريق يعمل بها كل يوم.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Seven steps, many hands.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Behind every step is a team that works on it every day.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 6 of 7. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٦/٧» in small Arabic-Indic digits and 6/7 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 7/7 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | تُرى |
| English headline | Visible capability. Measurable impact. |
| Arabic body | شكرًا لكل يدٍ عملت على الخط. أي خطوة فاجأتكم؟ |
| English body | Thank you to every pair of hands on the line. Which step surprised you? |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «شكرًا لكل يدٍ عملت على الخط. أي خطوة فاجأتكم؟» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Thank you to every pair of hands on the line. Which step surprised you?» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
3. Arabic supporting line «شكرًا لكل يدٍ عملت على الخط. أي خطوة فاجأتكم؟» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Thank you to every pair of hands on the line. Which step surprised you?» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 7 of 7. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٧/٧» in small Arabic-Indic digits and 7/7 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### JAN-L08 — Careers in manufacturing
- **Date:** 2027-01-27  |  **Channel:** LinkedIn + X  |  **Format:** Carousel, 5 slides  |  **Pillar:** People and careers
- **Caption (AR):**

> في المصنع مهن كثيرة، من قاعة التغليف إلى المختبر، ومن الصيانة إلى الإدارة.
> وفريق واحد يجمعها.
> تابعوا هذه الصفحة لأخبار المهن في سدير للأدوية.

- **Caption (EN):**

> A plant has many careers, from the packaging hall to the lab, from maintenance to administration.
> One team brings them together.
> Follow this page for career news from Sudair Pharma.

- **Hashtags:** #سدير_للأدوية #SudairPharma #مهن_الصناعة #CareersInManufacturing

#### Slide 1/5 — hook
**Treatment:** T7 People hero · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Generated Saudi woman in deep green hijab and abaya beside a Saudi man in white thobe and red-white shemagh above the real drone photograph of the site in the lower third; headline at the bottom.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | المصنع يقوم على الناس |
| Arabic headline 2 | مهن كثيرة |
| Kashida word | يقوم |
| English headline | A plant runs on people. |
| Arabic body | — |
| English body | — |

**Typography spec:**

  1. Arabic headline line 1 «المصنع يقوم على الناس» — AE_Sharjah-style heavy geometric kufi, 76 px, #FFFFFF, centred at y=1130.
  2. Arabic headline line 2 «مهن كثيرة» — same family, 52 px, mint #8EF0B0, y=1215. Stretch the word «يقوم» with kashida (tatweel) for rhythm.
  3. English line «A plant runs on people.» — Friz Quadrata Bold / italic condensed sans, 28 px, uppercase, white 90%, tracking +40, y=1280.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A002: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084636_0010_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Generated Saudi woman in deep green hijab and abaya beside a Saudi man in white thobe and red-white shemagh above the real drone photograph of the site in the lower third; headline at the bottom.

TREATMENT T7, People hero: People-hero treatment: photoreal portrait of Saudi people (man in white thobe and red-white shemagh, woman in deep green hijab and abaya), arms crossed, proud and calm, looking up and to the right, cinematic light, teal night-sky gradient; below them a real photograph of the landmark or stage fills the lower third.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «المصنع يقوم على الناس» — AE_Sharjah-style heavy geometric kufi, 76 px, #FFFFFF, centred at y=1130.
2. Arabic headline line 2 «مهن كثيرة» — same family, 52 px, mint #8EF0B0, y=1215. Stretch the word «يقوم» with kashida (tatweel) for rhythm.
3. English line «A plant runs on people.» — Friz Quadrata Bold / italic condensed sans, 28 px, uppercase, white 90%, tracking +40, y=1280.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The packaging hall team, women and men, standing together at the line, wide frame graded to the emerald palette; no label readable.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | في قاعة التغليف |
| Arabic headline 2 | على الخط |
| Kashida word | التغليف |
| English headline | In the packaging hall |
| Arabic body | فرق تشغّل الخط وتجهّز العبوات، رجالًا ونساءً. |
| English body | Teams run the line and pack the units, women and men together. |

**Typography spec:**

  1. Arabic headline line 1 «في قاعة التغليف» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «على الخط» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «التغليف» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «فرق تشغّل الخط وتجهّز العبوات، رجالًا ونساءً.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «In the packaging hall» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Teams run the line and pack the units, women and men together.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The packaging hall team, women and men, standing together at the line, wide frame graded to the emerald palette; no label readable.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «في قاعة التغليف» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «على الخط» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «التغليف» with kashida (tatweel) for rhythm.
3. Arabic supporting line «فرق تشغّل الخط وتجهّز العبوات، رجالًا ونساءً.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «In the packaging hall» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Teams run the line and pack the units, women and men together.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** A lab analyst at the bench, focused, soft key light from the left, dark green panel on the right for text; no label legible on any container.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | في المختبر |
| Arabic headline 2 | محلّلون وفنيّون |
| Kashida word | المختبر |
| English headline | In the lab |
| Arabic body | محلّلون وفنيّون عند طاولات عملهم. |
| English body | Analysts and technicians at their benches. |

**Typography spec:**

  1. Arabic headline line 1 «في المختبر» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «محلّلون وفنيّون» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «المختبر» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «محلّلون وفنيّون عند طاولات عملهم.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «In the lab» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «Analysts and technicians at their benches.» — Roboto Light, 26 px, white 80%, y=746.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): A lab analyst at the bench, focused, soft key light from the left, dark green panel on the right for text; no label legible on any container.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «في المختبر» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «محلّلون وفنيّون» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «المختبر» with kashida (tatweel) for rhythm.
3. Arabic supporting line «محلّلون وفنيّون عند طاولات عملهم.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «In the lab» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «Analysts and technicians at their benches.» — Roboto Light, 26 px, white 80%, y=746.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Type card on deep emerald with a thin mint rule and one small white line icon of a team; no photograph.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | وخلف المشهد |
| Arabic headline 2 | مهن لا تُرى |
| Kashida word | المشهد |
| English headline | And behind the scenes |
| Arabic body | مهندسون ومخطّطون وفرق الصيانة والإمداد والإدارة. |
| English body | Engineers, planners, and the maintenance, logistics and administration teams. |

**Typography spec:**

  1. Arabic headline line 1 «وخلف المشهد» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «مهن لا تُرى» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «المشهد» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «مهندسون ومخطّطون وفرق الصيانة والإمداد والإدارة.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «And behind the scenes» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Engineers, planners, and the maintenance, logistics and administration teams.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Type card on deep emerald with a thin mint rule and one small white line icon of a team; no photograph.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «وخلف المشهد» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «مهن لا تُرى» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «المشهد» with kashida (tatweel) for rhythm.
3. Arabic supporting line «مهندسون ومخطّطون وفرق الصيانة والإمداد والإدارة.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «And behind the scenes» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Engineers, planners, and the maintenance, logistics and administration teams.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | صناعة تُرى، |
| Arabic headline 2 | وأثر يُقاس. |
| Kashida word | تُرى |
| English headline | Visible capability. Measurable impact. |
| Arabic body | تابعوا هذه الصفحة لأخبار المهن في سدير للأدوية. |
| English body | Follow this page for career news from Sudair Pharma. |

**Typography spec:**

  1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «تابعوا هذه الصفحة لأخبار المهن في سدير للأدوية.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Follow this page for career news from Sudair Pharma.» — Roboto Light, 30 px, white 80%, y=826.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Typography only on deep emerald with a thin mint rule, one small palm line icon in white, hairline inset frame; no photograph. Logo placed in the layout tool.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «صناعة تُرى،» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «وأثر يُقاس.» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «تُرى» with kashida (tatweel) for rhythm.
3. Arabic supporting line «تابعوا هذه الصفحة لأخبار المهن في سدير للأدوية.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Follow this page for career news from Sudair Pharma.» — Roboto Light, 30 px, white 80%, y=826.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

### JAN-F12 — A week in the plant
- **Date:** 2027-01-28  |  **Channel:** Instagram + Facebook  |  **Format:** Carousel, 5 slides  |  **Pillar:** Meet the makers
- **Caption (AR):**

> أسبوعٌ كامل في المصنع، من الأحد إلى الخميس، بلقطاتٍ من أيامه.
> شكرًا لكل يدٍ عملت هذا الأسبوع.
> مرّروا لتروه، وقولوا لنا أي لقطةٍ أعجبتكم.

- **Caption (EN):**

> A full working week in the plant, Sunday to Thursday, in shots from its days.
> Thank you to every hand that worked this week.
> Swipe to see it, and tell us which shot you liked.

- **Hashtags:** #سدير_للأدوية #SudairPharma #أسبوع_في_المصنع #LifeAtSudair

#### Slide 1/5 — hook
**Treatment:** T9 Process flow · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Five day-nodes joined by a thin mint line, Sunday to Thursday, each with a small real crop (A001, A003, A007, A013).

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | أسبوعٌ |
| Arabic headline 2 | في المصنع |
| Kashida word | أسبوعٌ |
| English headline | A week in the plant. |
| Arabic body | من الأحد إلى الخميس، كما رأيناه. |
| English body | Sunday to Thursday, as we saw it. |

**Typography spec:**

  1. Arabic headline line 1 «أسبوعٌ» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
  2. Arabic headline line 2 «في المصنع» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «أسبوعٌ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «من الأحد إلى الخميس، كما رأيناه.» — Muna Regular, 40 px, white 90%, centred, y=370.
  4. English line «A week in the plant.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
  5. English support line «Sunday to Thursday, as we saw it.» — Roboto Light, 26 px, white 80%, y=386.
  6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1210.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A001: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A003: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121103516_0070_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.
INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Five day-nodes joined by a thin mint line, Sunday to Thursday, each with a small real crop (A001, A003, A007, A013).

TREATMENT T9, Process flow: Process-flow treatment: vertical flow of rounded step cards joined by a thin mint line with small glowing nodes; each card holds a number in a circle, a two-word label and a small real photo crop (clean room, flasks, packaging line), on emerald with lattice at 6%.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «أسبوعٌ» — AE_Sharjah-style heavy geometric kufi, 100 px, #FFFFFF, centred at y=140.
2. Arabic headline line 2 «في المصنع» — same family, 70 px, mint #8EF0B0, y=270. Stretch the word «أسبوعٌ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «من الأحد إلى الخميس، كما رأيناه.» — Muna Regular, 40 px, white 90%, centred, y=370.
4. English line «A week in the plant.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=340.
5. English support line «Sunday to Thursday, as we saw it.» — Roboto Light, 26 px, white 80%, y=386.
6. Chip «Swipe» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1210.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 1 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «١/٥» in small Arabic-Indic digits and 1/5 in small English, 22 px, white 70%. HOOK slide: add a small swipe-arrow chip at the bottom right.
```

</details>

---

#### Slide 2/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The real drone view of the palm-lined campus at dawn (A001), teal-green grade; a small 'Sunday' day label.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV

| Element | String |
|---|---|
| Arabic headline 1 | الأحد |
| Arabic headline 2 | يبدأ الأسبوع |
| Kashida word | الأحد |
| English headline | Sunday: the week begins. |
| Arabic body | ضوء الصباح على الموقع، والفريق في الطريق. |
| English body | The morning light on the site, and the team on its way. |

**Typography spec:**

  1. Arabic headline line 1 «الأحد» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «يبدأ الأسبوع» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الأحد» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «ضوء الصباح على الموقع، والفريق في الطريق.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Sunday: the week begins.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «The morning light on the site, and the team on its way.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A001: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/DJI_20260121084222_0001_D.MOV" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The real drone view of the palm-lined campus at dawn (A001), teal-green grade; a small 'Sunday' day label.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الأحد» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «يبدأ الأسبوع» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «الأحد» with kashida (tatweel) for rhythm.
3. Arabic supporting line «ضوء الصباح على الموقع، والفريق في الطريق.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Sunday: the week begins.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «The morning light on the site, and the team on its way.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 2 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٢/٥» in small Arabic-Indic digits and 2/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 3/5 — idea
**Treatment:** T3 Portrait panel · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** The lab analyst at the bench (A007), the equipment beside them in soft focus; a small 'Tuesday' day label.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الثلاثاء |
| Arabic headline 2 | على المقعد |
| Kashida word | المقعد |
| English headline | Tuesday: at the bench. |
| Arabic body | يدٌ هادئة، وعملٌ متواصل. |
| English body | A calm hand, and steady work. |

**Typography spec:**

  1. Arabic headline line 1 «الثلاثاء» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
  2. Arabic headline line 2 «على المقعد» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «المقعد» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «يدٌ هادئة، وعملٌ متواصل.» — Muna Regular, 40 px, white 90%, centred, y=620.
  4. English line «Tuesday: at the bench.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
  5. English support line «A calm hand, and steady work.» — Roboto Light, 26 px, white 80%, y=746.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A007: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/1/ALABBASY.8838.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): The lab analyst at the bench (A007), the equipment beside them in soft focus; a small 'Tuesday' day label.

TREATMENT T3, Portrait panel: Studio portrait treatment: three-quarter view, calm confident look, soft key light from the left, dark green panelled wall with a faint vertical line pattern, shallow depth of field. Left 55% of the tile is the person, right 45% is clear dark green for text.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الثلاثاء» — AE_Sharjah-style heavy geometric kufi, 96 px, #FFFFFF, right-aligned in the right column x 560 to 1020 at y=170.
2. Arabic headline line 2 «على المقعد» — same family, 72 px, mint #8EF0B0, y=520. Stretch the word «المقعد» with kashida (tatweel) for rhythm.
3. Arabic supporting line «يدٌ هادئة، وعملٌ متواصل.» — Muna Regular, 40 px, white 90%, centred, y=620.
4. English line «Tuesday: at the bench.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=700.
5. English support line «A calm hand, and steady work.» — Roboto Light, 26 px, white 80%, y=746.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 3 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٣/٥» in small Arabic-Indic digits and 3/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 4/5 — idea
**Treatment:** T2 Team landscape · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Women and men of the packaging hall along the line (A013), natural faces, emerald-teal grade; a small 'Thursday' day label.

**Assets (root = `Sudair Assets`):**
  - Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4

| Element | String |
|---|---|
| Arabic headline 1 | الخميس |
| Arabic headline 2 | إيقاعٌ واحد |
| Kashida word | إيقاعٌ |
| English headline | Thursday: one rhythm. |
| Arabic body | نساءٌ ورجال، وفريقٌ واحد حتى آخر الأسبوع. |
| English body | Women and men, one team to the end of the week. |

**Typography spec:**

  1. Arabic headline line 1 «الخميس» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
  2. Arabic headline line 2 «إيقاعٌ واحد» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «إيقاعٌ» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «نساءٌ ورجال، وفريقٌ واحد حتى آخر الأسبوع.» — Muna Regular, 40 px, white 90%, centred, y=400.
  4. English line «Thursday: one rhythm.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
  5. English support line «Women and men, one team to the end of the week.» — Roboto Light, 26 px, white 80%, y=466.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

INPUT IMAGE A013: upload "Sudair Assets/Collective footage-20261001T081156Z-1-008/Collective footage/Camera/2/jaradi20260121_8608.MP4" (clip: pull a sharp, well-exposed frame between 2 s and 10 s, or the frame named in the shot). Keep people, clothing, architecture and equipment exactly as photographed; only regrade colour to the Sudair emerald palette, extend the background and remove distracting signage.

HERO (message first): Women and men of the packaging hall along the line (A013), natural faces, emerald-teal grade; a small 'Thursday' day label.

TREATMENT T2, Team landscape: Wide documentary photograph treatment: the subject group in one row in a landscape, a dramatic teal-green sky with long cirrus clouds, golden-hour side light, graded to the Sudair emerald palette, natural faces, horizon at 60% of tile height.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «الخميس» — AE_Sharjah-style heavy geometric kufi, 130 px, #FFFFFF, centred at y=150.
2. Arabic headline line 2 «إيقاعٌ واحد» — same family, 88 px, mint #8EF0B0, y=300. Stretch the word «إيقاعٌ» with kashida (tatweel) for rhythm.
3. Arabic supporting line «نساءٌ ورجال، وفريقٌ واحد حتى آخر الأسبوع.» — Muna Regular, 40 px, white 90%, centred, y=400.
4. English line «Thursday: one rhythm.» — Friz Quadrata Bold / italic condensed sans, 30 px, uppercase, white 90%, tracking +40, y=420.
5. English support line «Women and men, one team to the end of the week.» — Roboto Light, 26 px, white 80%, y=466.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 4 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٤/٥» in small Arabic-Indic digits and 4/5 in small English, 22 px, white 70%.
```

</details>

---

#### Slide 5/5 — cta
**Treatment:** T8 Type card · **Canvas:** 1080 × 1350 px (4:5)

**Hero:** Thank-you type card on deep emerald, hairline frame, thin mint rule, the small white palm-burst symbol.

**Assets (root = `Sudair Assets`):**
  - — (GENERATED)

| Element | String |
|---|---|
| Arabic headline 1 | شكرًا لكل يدٍ |
| Arabic headline 2 | عملت هذا الأسبوع |
| Kashida word | شكرًا |
| English headline | Visible capability. Measurable impact. |
| Arabic body | صناعة تُرى، وأثر يُقاس. |
| English body | Thank you to every hand that worked this week. |

**Typography spec:**

  1. Arabic headline line 1 «شكرًا لكل يدٍ» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
  2. Arabic headline line 2 «عملت هذا الأسبوع» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكرًا» with kashida (tatweel) for rhythm.
  3. Arabic supporting line «صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
  4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
  5. English support line «Thank you to every hand that worked this week.» — Roboto Light, 30 px, white 80%, y=826.
  6. Chip «January 2027» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
  Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

<details><summary>Full slide image prompt</summary>

```
FORMAT: Social tile, 1080 × 1350 px (4:5), for Instagram, Facebook, LinkedIn and X; keep the key message inside the central square for the profile-grid crop.

BRAND: Sudair Pharma (SPC), a Saudi pharmaceutical manufacturer. Main theme: Visible capability. Measurable impact. Look of the team's posts: deep emerald gradient, one hero, heavy Arabic headline, premium and calm.

HERO (message first): Thank-you type card on deep emerald, hairline frame, thin mint rule, the small white palm-burst symbol.

TREATMENT T8, Type card: Type-led treatment: deep emerald gradient, thin mint rule, one small white line icon, a 24 px hairline inset frame, no photograph.

COLOUR: emerald gradient #09A45B to #04301F, mint accent #8EF0B0, white headline; one accent only; no neon.

LIGHT AND GRADE: soft directional key light, mint rim light, natural skin tones, teal-green shadows, gentle vignette; documentary realism for photographs, polished studio finish for 3D.

TEXT (render exactly):
1. Arabic headline line 1 «شكرًا لكل يدٍ» — AE_Sharjah-style heavy geometric kufi, 140 px, #FFFFFF, centred at y=400.
2. Arabic headline line 2 «عملت هذا الأسبوع» — same family, 90 px, mint #8EF0B0, y=580. Stretch the word «شكرًا» with kashida (tatweel) for rhythm.
3. Arabic supporting line «صناعة تُرى، وأثر يُقاس.» — Muna Regular, 40 px, white 90%, centred, y=680.
4. English line «Visible capability. Measurable impact.» — Friz Quadrata Bold / italic condensed sans, 34 px, uppercase, white 90%, tracking +40, y=780.
5. English support line «Thank you to every hand that worked this week.» — Roboto Light, 30 px, white 80%, y=826.
6. Chip «January 2027» — rounded pill, 1 px outline #85C66F, text 24 px white, centred at y=1000.
Keep all text inside x 60 to 1020 and y 150 to 1230 (grid-safe). Arabic reads right to left. Render every string exactly; do not add words.

LOGO AND FRAME: reserve a clean 190 × 190 px area at the top-left (x 40, y 40) for the logo; do not draw any logo or tagline. Add a 24 px hairline inset frame in white at 20% opacity.

NEGATIVE: misspelled or broken Arabic, extra words, fake logos, other company names, watermark, stock-photo handshake, pills, blister packs or labels, medical claims, distorted hands, uncanny faces, plastic skin, neon colours, text outside the safe zones, flags, religious symbols.

CAROUSEL CONTINUITY: slide 5 of 5. The emerald glow moves 15% along the carousel (top-left on slide 1, drifting to the right), the lattice continues across slides, the headline baseline stays at y=210. Slide counter top-right: «٥/٥» in small Arabic-Indic digits and 5/5 in small English, 22 px, white 70%. CTA slide: add the theme line «صناعة تُرى، وأثر يُقاس.» and a soft call to action; make the logo area larger (260 × 260 px) and add sudairpharma.com in 26 px.
```

</details>

---

