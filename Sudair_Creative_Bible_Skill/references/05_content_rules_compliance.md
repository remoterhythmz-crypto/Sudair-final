# 05 Content rules and compliance (read before writing any copy)

This is a creative guard-rail, not legal advice. The client's regulatory and legal teams decide.


## CLAIM-FREE RULE (client ruling, Oct 2026): no SFDA approval, no claim that needs referencing
- A **claim** is any statement about health, disease, prevention, screening, treatment, safety, efficacy, dosage or outcomes; any health advice ("ask your pharmacist", "check early"); any quality-assurance or compliance assertion ("every batch is tested", "meets the standard", "GMP", "certified", "safe"); any scientific or technical explanation; any statistic, ranking, comparison or superlative; any product name or readable label; any regulator reference; any forward-looking promise.
- **Default for all content: claim level NONE.** Allowed: people, portraits, teams, thanks, careers, the site and its architecture, local industry as a plain fact of place, tools seen from outside, events attended (exact, already published), recognition quoted exactly, solidarity greetings on awareness days **without information or advice**, invitations (questions, polls), looking back.
- **If a claim cannot be avoided, schedule it in the last month of the plan and mark it `claim_level: FLAG`** with `claim_type` (process description, quality statement, technology description, recognition) and `claim_detail` (what the client must verify). Keep it descriptive. Never write efficacy, safety, outcomes, statistics, comparisons or product names, even then.
- Flagged pieces are listed in a separate file (`Sudair_3Month_Claims_and_Approval_Review.md`) and wait for the client's quality or regulatory sign-off.
- No safety line is needed on claim-free posts: do not add "for public awareness only" (it implies health content).
- Audit: run `_src/claim_audit.py` (English and Arabic term list). Zero hits and level NONE are required for every non-flagged piece.

## Product and claims (SFDA-safe by design)
- Corporate, awareness and people content only. **No product names, no drug names, no pack shots, no dosage, no indications, no efficacy, safety or comparison claims, no price, no offer, no "ask your doctor for [product]".**
- Do not show a medicine pack, blister, vial label, or a readable label on any container. Flasks, glassware, machines and clean rooms are fine when no label is legible.
- Health information is general and non-instructional. No symptom checklists, self-diagnosis steps, screening ages, rates or statistics unless a source is approved by the client (mark `[NEEDS APPROVED FACT]`).
- Health-related captions are avoided altogether (see the claim-free rule). If a client-approved awareness caption is ever added, it ends with: AR «للتوعية العامة فقط، ولا تغني عن استشارة الطبيبة أو الطبيب.» / EN "For public awareness only. It does not replace advice from your doctor."
- Awareness-day posts are solidarity greetings and thanks to the people who care. They carry no information, advice, number or claim.
- No patient story, testimonial, before-and-after or disease imagery that is graphic or depressing.

## Capital markets
- Never mention shares, the IPO, valuation, targets or results. No forward-looking promises ("Looking ahead (no promises)" means values and people only).
- Use only facts the client has published (site, press, awards). Awards (Forbes ME Top Healthcare Leaders 2026, Made in Saudi Gold Tier 2025) are quoted exactly as supplied.

## People
- Real staff or leaders appear only with written consent. Executive portraits only with written approval from the person and the company.
- Generated people are fine as an illustration but are never captioned as staff, patients or named people.
- Saudi norms: modest dress; hijab, abaya, thobe and shemagh are used naturally; no body imagery; no flags (state flags are handled by the client); no religious symbols or verses used decoratively; no alcohol, no pork; no music with instruments in religious periods (Ramadan is outside this window).
- Gender: mixed teams are shown in work context. Women are shown as professionals first.

## Partners and third parties
- No other company logo or sign as the hero. Partner and event logos only in an event post with permission and always smaller than the Sudair logo.
- Photos that show a host's signage (Global Health Exhibition, CPHI) are used only as event recap, never as proof of endorsement.

## Language
- Arabic: native review before posting. No machine-translated lines. Use the feminine addressing form only when the audience is women (awareness months).
- Dialect is used only in awareness months to match the team's pink series; the rest is Modern Standard Arabic with a Saudi warmth.
- English: short, active, no hype words ("revolutionary", "best", "leading" unless supplied and approved).
- Hashtags: 3 to 5, bilingual. Fixed: #سدير_للأدوية #SudairPharma. Add one topical tag.

## Approval gate (every piece)
1. Message approved (one sentence).
2. Facts sourced or marked `[NEEDS APPROVED FACT]`.
3. People consent logged.
4. Arabic native review.
5. Client regulatory sign-off for any health-related caption.
6. Posting time chosen (Sun to Thu, 08:30 to 10:00 or 19:30 to 21:30 KSA; LinkedIn Tue to Thu mornings).
