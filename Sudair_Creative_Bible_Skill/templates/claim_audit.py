# -*- coding: utf-8 -*-
"""Claim audit: scans every text field of every piece for claim-type language.
Nov/Dec pieces must be claim_level NONE with no hits. Jan pieces may be FLAG."""
import json, os, re, sys, glob

H = os.path.dirname(os.path.abspath(__file__))
TEXT_KEYS = {"title_en", "title_ar", "objective", "hero_en", "head_ar_1", "head_ar_2", "head_en", "sub_en", "chip", "caption_ar", "caption_en", "hashtags",
             "body_ar", "body_en", "small_en", "sticker_text", "concept", "vo_ar", "vo_en", "on_screen_ar", "on_screen_en", "key_frame_en", "cover_hero_en"}

EN = [r"\bsafe\b", r"\bsafety\b", r"\bquality\b", r"\btested\b", r"\btesting\b", r"\bchecked\b", r"\bchecks?\b", r"\bcertif", r"\bstandards?\b", r"\bgmp\b", r"\bsfda\b",
      r"\bprevent", r"\btreat", r"\bcure", r"\bprotect", r"\btherap", r"\befficac", r"\beffective", r"\bdose", r"\bdosage", r"\bsymptom", r"\bdiagnos", r"\bscreening",
      r"\bbest\b", r"\bleading\b", r"\bfirst\b", r"\blargest\b", r"\bguarantee", r"\bproven\b", r"\bclinical", r"\bscience\b|\bscientific", r"\bcompliance|\bcompliant",
      r"\bask your\b", r"\bconsult\b", r"\bdoctor", r"\bphysician", r"\bpatients?\b", r"\bhealth benefit", r"\bheal", r"\bmedicine works|\bworks? for\b",
      r"\d+\s?%", r"\bpercent"]
AR = ["آمن", "أمان", "سلامة", "جودة", "فحص", "اختبار", "معتمد", "اعتماد", "معايير", "معيار", "وقاية", "علاج", "يحمي", "تحمي", "حماية", "فعال", "جرعة", "أعراض", "تشخيص",
      "أفضل", "رائد", "الأول", "ضمان", "استشر", "طبيب", "مريض", "مرضى", "شفاء", "الكشف المبكر", "ضبط"]

# reviewed false positives (id -> terms). Reason noted in the claims review file.
ALLOW = {
    "DEC-F06": {"treat"},          # "sky treatment" = photo grade
    "DEC-L04": {"فعال", "heal"},   # "events" in Arabic; "Global Health Exhibition" is an event's exact name
    "JAN-F02": {"الأول"},          # "the first working week of 2027" (a date, not a superlative)
    "JAN-F11": {"quality", "جودة"},# job-function name "quality team" (people only)
}

def walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in TEXT_KEYS and isinstance(v, str):
                yield path + "/" + k, v
            elif isinstance(v, (dict, list)):
                yield from walk(v, path + "/" + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, path + "[%d]" % i)

INTERNAL = ("/hero_en", "/key_frame_en", "/cover_hero_en", "/objective", "/concept", "/compliance_note", "/audio")
MONTHS = r"(?i)\b(jan|january|feb|nov|november|dec|december|of|week|view|part|view)\b|نوفمبر|ديسمبر|يناير|من"

def hits(piece):
    out = []
    for p, t in walk(piece):
        low = t.lower()
        internal = p.endswith(INTERNAL) or any(p.endswith(k) for k in INTERNAL)
        for rx in EN:
            if internal and (rx.startswith(r"\d") or "percent" in rx):
                continue
            m = re.search(rx, low)
            if m: out.append((p, m.group(0), t))
        for w in AR:
            if w in t: out.append((p, w, t))
        if internal:
            continue
        for m in re.finditer(r"(?<![\d/:-])\d{1,3}(?![\d/:-])", t):
            if re.search(MONTHS, t[max(0, m.start() - 18): m.end() + 18]):
                continue
            # numbers other than dates/time/slide counters: flag short standalone numbers
            if re.search(r"(?i)\b(step|steps|slide|shift|week|day|view|frame|photo|hour|hours|minute|second|s|am|pm)\b", t[max(0, m.start() - 12): m.end() + 12]):
                continue
            out.append((p, "number " + m.group(0), t))
    return out

def load_all():
    res = []
    for f in sorted(glob.glob(os.path.join(H, "content_*.json"))):
        res += json.load(open(f, encoding="utf-8"))
    return res

if __name__ == "__main__":
    P = load_all()
    bad = 0
    for p in P:
        month = p["id"].split("-")[0]
        h = [x for x in hits(p) if not any(a in x[1] for a in ALLOW.get(p["id"], ()))]
        lvl = p.get("claim_level", "?")
        if month != "JAN":
            if lvl != "NONE" or h:
                bad += 1
                print("%s level=%s hits=%d" % (p["id"], lvl, len(h)))
                for path, term, t in h[:6]:
                    print("   %s [%s] %s" % (path, term, t[:110].replace("\n", " ")))
        else:
            if lvl not in ("NONE", "FLAG"):
                print("%s missing claim_level" % p["id"]); bad += 1
            if lvl == "NONE" and h:
                bad += 1
                print("%s level=NONE but has hits: %s" % (p["id"], sorted(set(t for _, t, _ in h))[:8]))
    print("pieces", len(P), "problems", bad)
    sys.exit(1 if bad else 0)
