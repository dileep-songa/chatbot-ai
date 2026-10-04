"""Intent classification and response routing utilities."""

from __future__ import annotations

from typing import Callable, Dict


class IntentRouter:
    """Maps detected intents to response handlers."""

    def __init__(self):
        self.handlers: Dict[str, Callable[[str], str]] = {
            "greeting": self._handle_greeting,
            "help": self._handle_help,
            "goodbye": self._handle_goodbye,
            "features": self._handle_features,
            "pricing": self._handle_pricing,
            "general": self._handle_general,
            "unknown": self._handle_unknown,
        }

    def handle(self, intent: str, user_message: str) -> str:
        handler = self.handlers.get(intent, self._handle_general)
        return handler(user_message)

    def _handle_greeting(self, user_message: str) -> str:
        return "Hello! I'm here to help. How can I assist you today?"

    def _handle_help(self, user_message: str) -> str:
        return "I can help with product information, support, and general questions."

    def _handle_goodbye(self, user_message: str) -> str:
        return "Goodbye! Come back anytime."

    def _handle_features(self, user_message: str) -> str:
        return "This assistant can help with product questions, support, and general conversation."

    def _handle_pricing(self, user_message: str) -> str:
        return "I can provide general pricing guidance. Please connect with a sales or support representative for a custom quote."

    def _handle_general(self, user_message: str) -> str:
        return "Thanks for your message. I can help with product information, support, and general questions."

    def _handle_unknown(self, user_message: str) -> str:
        return "I did not understand that. Please rephrase your message or ask for help."
