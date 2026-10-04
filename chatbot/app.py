"""Core ChatBot implementation."""

from __future__ import annotations

from collections import deque
from typing import Deque, List, Optional

from .intent_engine import IntentEngine, ResponseManager
from .session_memory import SessionMemory


class ChatBot:
    """A simple but professional conversational bot with intent routing and memory."""

    def __init__(self, max_history: int = 5, session_id: str = "default"):
        self.intent_engine = IntentEngine()
        self.response_manager = ResponseManager()
        self.memory = SessionMemory(max_history=max_history)
        self.max_history = max_history
        self.session_id = session_id
        self.history: Deque[dict] = deque(maxlen=max_history)

    def chat(self, user_message: str, session_id: Optional[str] = None) -> str:
        message = (user_message or "").strip()
        if not message:
            return "Please send a message so I can respond."

        intent_match = self.intent_engine.detect(message)
        intent_name = intent_match.intent
        response = self.response_manager.generate(intent_name, message, list(self.history))

        history_item = {
            "user": message,
            "intent": intent_name,
            "confidence": intent_match.confidence,
            "response": response,
        }
        self.history.append(history_item)

        active_session = session_id or self.session_id
        self.memory.add(active_session, message, intent_name, response)
        return response

    def recent_history(self) -> List[dict]:
        return list(self.history)

    def get_session_history(self, session_id: Optional[str] = None) -> List[dict]:
        return self.memory.get_recent(session_id or self.session_id)
