# Piece fields (JSON)

Every piece carries these fields. Formats: still, carousel, reel, story. Channels: IG+FB, LI+X.

| Field | Meaning |
|---|---|
| id, date, week, channel, format, pillar | Placement |
| title_en, title_ar, objective | Message in one sentence |
| treatment | T1..T10 or TP (file 03) |
| hero_en | What the picture must show (message first, then detail) |
| asset_ids, source, generated_elements | Real assets by ID (file 06), REAL / REAL+GENERATED / GENERATED, what must be generated |
| consent_needed, needs_fact | Approval flags |
| claim_level, claim_type, claim_detail | NONE by default. FLAG only in the last month, with type and what to verify |
| compliance_note | One line: what was avoided or must be approved |
| head_ar_1, head_ar_2, kashida_word, head_en, sub_en, chip | Text on image (two-level Arabic headline, English line, chip) |
| caption_ar, caption_en, hashtags | Caption |
| slides[] (carousel) | n, role (hook, idea, proof, step, cta), treatment, hero_en, asset_ids, head_*, body_*, small_en, flagged |
| shots[] (reel) | n, sec_start, sec_end, key_frame_en, asset_ids, camera_move, subject_motion, environment_motion, on_screen_ar/en, vo_ar/en, flagged |
| duration_s, concept, audio, vo_ar, vo_en, cover_hero_en (reel) | Reel-level |
| story_kind, sticker_text (story) | poll, question, countdown, quiz, behind, thanks, fact, announce |
