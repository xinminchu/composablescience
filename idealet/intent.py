"""Rule-based citation-intent classifier (baseline v0.1, CiTO-aligned).

Coarse intent vocabulary, aligned with the hand-annotated demo edges
("reuses", "background") and CiTO properties:

  usesMethodIn  ~ cito:usesMethodIn
  extends       ~ cito:extends
  confirms      ~ cito:confirms
  critiques     ~ cito:critiques
  background    ~ cito:citesAsRelated   (default)

Deterministic cue-word rules over the citation context sentence.
This is a baseline: the roadmap calls for a 7-class CiTO model with
human-in-the-loop review. Every output records its method + confidence.
"""

import re

# (intent, cues, confidence) — checked in order; first match wins.
_RULES = [
    ("critiques",
     [r"\bhowever\b", r"\blimitation", r"\bfail", r"\bin contrast\b",
      r"\bunlike\b", r"\bshortcoming", r"\bdrawback", r"\bstruggle"],
     0.60),
    ("extends",
     [r"\bwe extend", r"\bextends\b", r"\bimprov", r"\bbuilds? upon\b",
      r"\bgeneraliz", r"\boutperform", r"\bsurpass", r"\bgoes beyond\b"],
     0.60),
    ("confirms",
     [r"\bconsistent with\b", r"\bin line with\b", r"\bconfirm",
      r"\bsupport(?:s|ed)?\b", r"\bagree", r"\bvalidat"],
     0.55),
    ("usesMethodIn",
     [r"\bwe use\b", r"\bwe adopt", r"\bwe employ", r"\bwe leverage\b",
      r"\bbased on\b", r"\bfollowing\b", r"\bbuilt on\b", r"\badopted\b",
      r"\bdirectly on\b"],
     0.60),
    ("background",
     [r"\bprior work\b", r"\brelated work\b", r"\bproposed\b",
      r"\bintroduced\b", r"\bpioneered\b"],
     0.50),
]

_COMPILED = [(intent, [re.compile(p, re.I) for p in cues], conf)
             for intent, cues, conf in _RULES]


def classify_intent(context):
    """Return (intent, confidence, matched_cue) for a citation context."""
    text = context or ""
    for intent, patterns, conf in _COMPILED:
        for pat in patterns:
            m = pat.search(text)
            if m:
                return intent, conf, m.group(0)
    return "background", 0.40, ""


def split_sentences(text):
    """Naive sentence splitter (stdlib-only baseline)."""
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])", text or "")
    return [p.strip() for p in parts if p.strip()]
