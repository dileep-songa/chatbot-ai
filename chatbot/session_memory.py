"""Intent detection engine and response generation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence

from .nlp import NLPProcessor


@dataclass(frozen=True)
class IntentMatch:
    """Represents a detected intent with confidence."""

    intent: str
    confidence: float


class IntentEngine:
    """Rule-based intent detection that is easy to extend."""

    def __init__(self):
        self.processor = NLPProcessor()
        self.intent_patterns: Dict[str, set[str]] = {
            "greeting": {"hello", "hi", "hey", "good", "morning", "afternoon", "evening", "greetings"},
            "help": {"help", "support", "assist", "guide", "need"},
            "goodbye": {"bye", "goodbye", "see", "later", "farewell", "exit"},
            "features": {"feature", "features", "capabilities", "ability", "abilities", "what", "can", "do"},
            "pricing": {"price", "pricing", "cost", "plan", "quote", "budget"},
        }

    def detect(self, text: str) -> IntentMatch:
        cleaned = self.processor.preprocess(text)
        tokens = self.processor.tokenize(cleaned)

        if not tokens:
            return IntentMatch("unknown", 0.0)

        scores = {intent: 0 for intent in self.intent_patterns}
        for intent, keywords in self.intent_patterns.items():
            for token in tokens:
                if token in keywords:
                    scores[intent] += 1

        best_intent = max(scores.items(), key=lambda item: item[1], default=("general", 0))
        if best_intent[1] == 0:
            return IntentMatch("general", 0.1)

        confidence = min(best_intent[1] / max(len(tokens), 1), 1.0)
        return IntentMatch(best_intent[0], round(confidence, 2))


class ResponseManager:
    """Generate clean, consistent responses for intents."""

    def __init__(self):
        self.templates = {
            "greeting": "Hello! I'm here to help. How can I assist you today?",
            "help": "I can help with product information, support, and general questions.",
            "goodbye": "Goodbye! Come back anytime.",
            "features": "This assistant can help with product questions, support, and general conversation.",
            "pricing": "I can provide general pricing guidance. Please connect with a sales or support representative for a custom quote.",
            "general": "Thanks for your message. I can help with product information, support, and general questions.",
            "unknown": "I did not understand that. Please rephrase your message or ask for help.",
        }

    def generate(
        self,
        intent: str,
        user_message: str,
        history: Optional[Sequence[dict]] = None,
    ) -> str:
        intent_name = intent if intent in self.templates else "general"

        if intent_name == "general" and history:
            recent = history[-3:]
            if any(item.get("intent") == "goodbye" for item in recent):
                return "It was nice chatting with you. Feel free to ask for help anytime."

        return self.templates.get(intent_name, self.templates["general"])
