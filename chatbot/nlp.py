"""Text preprocessing and intent detection utilities."""

from __future__ import annotations

import re
from typing import List


class NLPProcessor:
    """Normalize text and infer the likely user intent."""

    def preprocess(self, text: str) -> str:
        cleaned = (text or "").lower().strip()
        cleaned = re.sub(r"[^a-z0-9\s]", " ", cleaned)
        cleaned = re.sub(r"\s+", " ", cleaned)
        return cleaned.strip()

    def tokenize(self, text: str) -> List[str]:
        cleaned = self.preprocess(text)
        return [token for token in cleaned.split() if token]

    def extract_keywords(self, text: str) -> List[str]:
        return self.tokenize(text)

    def detect_intent(self, text: str) -> str:
        tokens = self.tokenize(text)
        if not tokens:
            return "unknown"

        greeting_terms = {"hello", "hi", "hey", "greetings", "good", "morning", "afternoon", "evening"}
        help_terms = {"help", "support", "assist", "guide", "need"}
        goodbye_terms = {"bye", "goodbye", "see", "later", "farewell", "exit"}
        feature_terms = {"feature", "features", "capabilities", "ability", "abilities", "what", "can", "do"}
        pricing_terms = {"price", "pricing", "cost", "plan", "quote", "budget"}

        if any(token in greeting_terms for token in tokens):
            return "greeting"
        if any(token in help_terms for token in tokens):
            return "help"
        if any(token in goodbye_terms for token in tokens):
            return "goodbye"
        if any(token in feature_terms for token in tokens):
            return "features"
        if any(token in pricing_terms for token in tokens):
            return "pricing"
        return "general"
