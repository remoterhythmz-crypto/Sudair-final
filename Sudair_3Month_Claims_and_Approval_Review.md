# Posts that carry a claim or need approval (highlighted for review)

Client rule: no post may need SFDA approval or hold a medical or scientific claim that needs referencing. Where a claim could not be avoided, the piece was moved to **January 2027**, the last month, and is listed here.

## Result

- Pieces in the 3 months: **96**
- Claim-free (claim level NONE): **81** (all of November and December, and the rest of January)
- Flagged for review (claim level FLAG): **15**, all in January 2027

Nothing in any piece names a product, drug, dose, indication, statistic, ranking or comparison. Flagged pieces are **descriptive company statements** (how the line runs, how a step is done, a technology) that the client's quality team should verify for accuracy before posting. No scientific reference is needed for any of them, and none should need SFDA approval because none promotes a product.

## How the audit was done

1. Authors wrote under a claim-free rule (no health, disease, prevention, treatment, safety, efficacy, quality-assurance, standards, statistics, comparisons, advice, products).
2. `_src/claim_audit.py` scans every text field (headline, caption, slide, shot, on-screen text, voice-over) for 60+ English and Arabic claim terms and for numbers.
3. November and December must show zero hits and claim level NONE; January pieces are either NONE or FLAG with a stated reason. Result: 96 pieces, 0 problems.
4. Reviewed false positives (kept): `treatment` in a photo grade (DEC-F06), the event name Global Health Exhibition and the Arabic word for events (DEC-L04), "first working week of 2027" (JAN-F02), and the job title "quality team" (JAN-F11, people only).

## Flagged pieces (January 2027)

### JAN-L01 · 2027-01-04 · LinkedIn + X · Seven steps, no secrets: steps 1 to 3

- **Type:** process description
- **Client to verify:** Client must confirm that the line can be described as seven steps and that steps 1 to 3 (materials arrive and are logged, each ingredient is weighed, ingredients are combined in a clean room) match the real sequence at the Sudair City plant.
- **Where:** slide 2, slide 3, slide 4, slide 5
- **Headline:** سبع خطوات / Seven steps. No secrets.
- **Caption (EN):** The line we work on has seven steps, from materials arriving to the batch leaving. This week we start with the first three: receive, weigh, prepare. Follow along for the rest.

### JAN-F04 · 2027-01-10 · Instagram + Facebook · Step 6: release

- **Type:** process description
- **Client to verify:** Verify that a batch is released only after the quality unit has reviewed its record and signed it off, exactly as practised at the Sudair City plant, and that 'step 6 of 7' matches the approved seven-step route.
- **Where:** whole piece
- **Headline:** الخطوة السادسة / Step 6: Release.
- **Caption (EN):** Step 6 on the line: release. A batch moves on only after its record has been reviewed and signed off by the quality unit. Follow the series, and tell us which step you want explained next.

### JAN-L03 · 2027-01-11 · LinkedIn + X · How a medicine is made: steps 4 to 6

- **Type:** process description
- **Client to verify:** Client must confirm that steps 4 to 6 (batch is filled into its containers with the operator working through glove ports, filled units are packed by the packaging hall team, the batch is released once its records are reviewed) match the real sequence and equipment at the plant.
- **Where:** slide 1, slide 2, slide 3, slide 4
- **Headline:** كيف يُصنع الدواء؟ / How a medicine is made.
- **Caption (EN):** Part 2 of Seven steps, no secrets: fill, pack, release. Behind each step there is a team that works on it. Which step would you like us to look at more closely?

### JAN-S04 · 2027-01-11 · Instagram + Facebook · Step of the day

- **Type:** process description
- **Client to verify:** Verify that filling takes place behind a barrier with the operator working through glove ports, as stated, and that the step number matches the approved seven-step route.
- **Where:** whole piece
- **Headline:** الخطوة 4 / Step 4: filled behind a barrier.
- **Caption (EN):** Step 4: the operator works through glove ports, behind a glass barrier.

### JAN-F05 · 2027-01-12 · Instagram + Facebook · Seven steps, no secrets

- **Type:** process description
- **Client to verify:** Verify the seven-step route exactly as stated (1 materials tested before use, 2 weighed, dispensed and recorded, 3 made in a controlled room, 4 filled behind a barrier through glove ports, 5 packed and checked on the line, 6 released on the reviewed record, 7 leaves the plant) against the actual process, and that a written record exists at every step.
- **Where:** slide 2, slide 3, slide 4
- **Headline:** سبع خطوات / Seven steps. No secrets.
- **Caption (EN):** From a material arriving to a batch leaving: seven steps, in order. Swipe to see each one. Every step leaves a written record. Which step would you like us to explain further?

### JAN-L04 · 2027-01-13 · LinkedIn + X · Release: the paperwork is the product

- **Type:** quality statement
- **Client to verify:** Client must verify that release at Sudair follows a review of the batch record by a responsible person, and approve the statement that the documentation is part of the product, before this carousel is used.
- **Where:** slide 1, slide 2, slide 3, slide 4
- **Headline:** التوثيق جزء من المنتج / The paperwork is the product.
- **Caption (EN):** Before a batch leaves the plant, it has a file. At release that file is read and reviewed, so the paperwork is part of the product. Which step would you like us to explain next?

### JAN-S05 · 2027-01-13 · Instagram + Facebook · Poll: which step surprised you?

- **Type:** process description
- **Client to verify:** The poll options name two steps of the seven-step line (weighing and release). Confirm the step names match the real plant process.
- **Where:** whole piece
- **Headline:** أي خطوة / Which step surprised you?
- **Caption (EN):** Which step surprised you most?

### JAN-F06 · 2027-01-14 · Instagram + Facebook · The whole line, in order

- **Type:** process description
- **Client to verify:** Verify that the order of steps narrated and shown (materials tested and weighed, made in a controlled room, filled behind a barrier, packed and checked on the line, released on the reviewed record, leaves the plant) matches the actual process, and that every location shown is the real Sudair City plant.
- **Where:** shot 2, shot 3, shot 4, shot 5, shot 6
- **Headline:** الخط كاملًا / The whole line, in order.
- **Caption (EN):** From a material arriving to a batch leaving: the whole line, in order. Every step you met in the series, now in one pass. Which shot made you stop?

### JAN-F07 · 2027-01-17 · Instagram + Facebook · Automated, not absent

- **Type:** technology description
- **Client to verify:** Verify that the line uses automated equipment that trained staff set up, operate and monitor, as stated, and that the photographed operator may be shown in this context.
- **Where:** whole piece
- **Headline:** الآلة تعمل / Automated, not absent.
- **Caption (EN):** Equipment on the line runs automatically, yet the team is present: setting it up, running it and watching it. Technology makes the work easier. People run it. What do you notice most in a modern plant?

### JAN-L05 · 2027-01-18 · LinkedIn + X · Technology in manufacturing

- **Type:** technology description
- **Client to verify:** Client must confirm that an isolator with glove ports, clean rooms with controlled air and surfaces, and automated lines with team-set-up equipment are in use at the plant, and that each plain-language description is accurate.
- **Where:** slide 2, slide 3, slide 4
- **Headline:** التقنية في التصنيع / Technology in manufacturing.
- **Caption (EN):** Three things you can see on a manufacturing line, in plain words: the isolator, the clean room and the automated line. Behind each one there is a team that works with it. Which would you like to know more about?

### JAN-F08 · 2027-01-19 · Instagram + Facebook · Technology on the line

- **Type:** technology description
- **Client to verify:** Verify the on-screen and spoken descriptions of the equipment shown (barrier enclosure operated through glove ports, packaging line, bench instruments) against what is actually installed, that no brand or model is identifiable, and that the staff shown consent.
- **Where:** shot 2, shot 3, shot 4, shot 5
- **Headline:** التقنية / Technology on the line.
- **Caption (EN):** Technology on the line, seen from the outside. A barrier, machines and instruments, and always people working beside them. Which piece of equipment should we show more of?

### JAN-S08 · 2027-01-20 · Instagram + Facebook · A validation run, up close

- **Type:** process description
- **Client to verify:** Verify that a validation run is a trial run of the equipment in which each step is recorded and then reviewed, and that this is how Sudair City describes and practises it.
- **Where:** whole piece
- **Headline:** تجربة تشغيل / A validation run, up close.
- **Caption (EN):** A validation run: the equipment is run as a trial and each step is recorded.

### JAN-F09 · 2027-01-21 · Instagram + Facebook · The unglamorous half of innovation

- **Type:** technology description
- **Client to verify:** Verify that new equipment at Sudair City is installed, run in a documented trial, recorded, and then serviced and calibrated on a schedule, exactly as the slides state.
- **Where:** slide 2, slide 3, slide 4
- **Headline:** نصف الابتكار / The unglamorous half of innovation.
- **Caption (EN):** Innovation is not only a new machine: it is installing, trying out, recording and then regular upkeep. The half that does not shine is the half that keeps the work going. Swipe to see each stage.

### JAN-F10 · 2027-01-24 · Instagram + Facebook · Quality control: how a batch is checked and released

- **Type:** quality statement
- **Client to verify:** Verify that each batch is checked by the quality team and released only after its record is reviewed, with no exception, and that the wording 'each batch' and 'checked' is acceptable to Quality and Regulatory before publication.
- **Where:** whole piece
- **Headline:** تُفحص التشغيلة / Checked. Then released.
- **Caption (EN):** Before a batch moves on, the quality team checks it, and it is released after its record is reviewed. This is what the work of quality looks like from the outside, no secrets. What more would you like to know about it?

### JAN-L07 · 2027-01-25 · LinkedIn + X · Seven steps, no secrets: the full line

- **Type:** process description
- **Client to verify:** Client must confirm the full seven-step sequence (receive, weigh, prepare, fill, pack, release, ship) and each plain-language step description against the plant's approved process before publication.
- **Where:** slide 1, slide 2, slide 3, slide 4, slide 5
- **Headline:** الخطوات السبع / The seven steps, in full.
- **Caption (EN):** Seven steps, from materials arriving to the batch leaving: receive, weigh, prepare, fill, pack, release, ship. That is the full line, and behind every step there is a team. Which step would you like us to look at more closely?

## What stays out of every month

- Product names, packs, labels, doses, indications.
- Health advice, screening, symptoms, prevention, treatment.
- Statistics, percentages, rankings, 'first', 'leading', 'best'.
- Regulator names and standards as proof (SFDA, MoH, GMP).
- Patient stories, and generated people captioned as staff.
