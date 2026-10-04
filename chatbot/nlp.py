import re
from typing import List


class NLPProcessor:
    """Simple NLP preprocessing and keyword extraction."""

    def preprocess(self, text: str) -> str:
        cleaned = text.lower().strip()
        cleaned = re.sub(r"[^a-z0-9\s]", " ", cleaned)
        cleaned = re.sub(r"\s+", " ", cleaned)
        return cleaned.strip()

    def tokenize(self, text: str) -> List[str]:
        cleaned = self.preprocess(text)
        return [token for token in cleaned.split() if token]

    def extract_keywords(self, text: str) -> List[str]:
        tokens = self.tokenize(text)
        return tokens

    def detect_intent(self, text: str) -> str:
        tokens = self.tokenize(text)
        if not tokens:
            return "unknown"

        greeting_terms = {"hello", "hi", "hey", "greetings"}
        help_terms = {"help", "support", "assist", "guide"}
        goodbye_terms = {"bye", "goodbye", "see", "later"}
        feature_terms = {"feature", "features", "capabilities", "what", "can"}
        pricing_terms = {"price", "pricing", "cost", "plan"}

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
