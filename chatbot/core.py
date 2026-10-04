"""Session-scoped memory for chatbot conversations."""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Deque, Dict, List, Optional


class SessionMemory:
    """Stores recent conversation turns and metadata per session."""

    def __init__(self, max_history: int = 10):
        self.max_history = max_history
        self._sessions: Dict[str, Deque[dict]] = defaultdict(lambda: deque(maxlen=max_history))

    def add(self, session_id: str, user_message: str, intent: str, response: str) -> dict:
        payload = {
            "session_id": session_id,
            "user_message": user_message,
            "intent": intent,
            "response": response,
        }
        self._sessions[session_id].append(payload)
        return payload

    def get_recent(self, session_id: str) -> List[dict]:
        return list(self._sessions.get(session_id, ()))

    def clear(self, session_id: Optional[str] = None) -> None:
        if session_id is None:
            self._sessions.clear()
        else:
            self._sessions.pop(session_id, None)
