import re
from itertools import chain
from typing import Dict, List

class IntentDetector:
    def __init__(self, gazetteer: Dict[str, Dict[str, List[str]]]):
        # 1) Collect names per kingdom (primary/aliases/rulers/places)
        self.k2names = {
            k: list(chain(
                d.get("primary_names", []),
                d.get("aliases", []),
                d.get("rulers", []),
                d.get("places", []),
            ))
            for k, d in gazetteer.items()
        }
        # 2) Precompile word-boundary patterns (case-insensitive)
        self.k2patterns = {
            k: [re.compile(rf"\b{re.escape(n)}\b", re.IGNORECASE) for n in names]
            for k, names in self.k2names.items()
        }

    def detect_intent(self, tokens: List[str], language: str = None, top_k: int = 3, threshold: int = 1):
        text = " ".join(tokens)
        scores = {}

        for k, pats in self.k2patterns.items():
            matched = set()
            s = 0
            for p in pats:
                m = p.search(text)
                if m:
                    key = m.group(0).lower()  # de-dup same phrase
                    if key not in matched:
                        matched.add(key)
                        s += 1
            if s >= threshold:
                scores[k] = s

        if not scores:
            return {"kingdoms": [], "confidence": 0.0, "all_scores": {}}

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        best = ranked[0][1]
        keep = [k for k, sc in ranked if sc >= 0.5 * best][:top_k]
        confidence = best / sum(scores.values())  # simple 0–1 confidence

        return {"kingdoms": keep, "confidence": round(confidence, 3), "all_scores": dict(ranked)}