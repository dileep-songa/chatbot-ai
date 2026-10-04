from collections import deque

from .intents import IntentRouter
from .nlp import NLPProcessor


class ChatBot:
    """A simple AI chatbot with intent routing and conversation memory."""

    def __init__(self, max_history: int = 5):
        self.nlp = NLPProcessor()
        self.router = IntentRouter()
        self.max_history = max_history
        self.history = deque(maxlen=max_history)

    def chat(self, user_message: str) -> str:
        message = (user_message or "").strip()
        if not message:
            return "Please send a message so I can respond."

        normalized = self.nlp.preprocess(message)
        intent = self.nlp.detect_intent(normalized)
        self.history.append({"user": message, "intent": intent})
        return self.router.handle(intent, message)

    def recent_history(self):
        return list(self.history)
