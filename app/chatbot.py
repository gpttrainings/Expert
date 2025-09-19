"""Simple rule-based chatbot logic."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Dict, List


@dataclass
class Message:
    """Represents a single chat message."""

    role: str
    content: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    def serialize(self) -> Dict[str, str]:
        """Serialize the message to a dictionary for API responses."""
        timestamp = self.timestamp.astimezone(UTC).isoformat().replace("+00:00", "Z")
        return {
            "role": self.role,
            "content": self.content,
            "timestamp": timestamp,
        }


class ChatBot:
    """A very small rule-based chatbot.

    The bot keeps track of a conversation history and produces canned
    responses based on simple heuristics.
    """

    def __init__(self) -> None:
        self._history: List[Message] = []

    def _build_response(self, user_message: str) -> str:
        """Return a canned response based on the user message."""
        normalized = user_message.lower().strip()

        if not normalized:
            return "Я не расслышал сообщение. Можешь повторить?"

        if "привет" in normalized or "здравств" in normalized:
            return "Привет! Чем я могу помочь?"

        if "пока" in normalized or "до свид" in normalized:
            return "До встречи! Если появятся вопросы, напиши снова."

        if "время" in normalized or "времени" in normalized or "час" in normalized:
            now = datetime.now(UTC).strftime("%H:%M UTC")
            return f"Сейчас {now}."

        if "помощ" in normalized:
            return "Я могу отвечать на простые вопросы и поддерживать беседу."

        # Default response when no rule applies
        return "Интересно! Расскажи подробнее."

    def ask(self, message: str) -> Message:
        """Store a user message and return the bot's response."""
        user_entry = Message(role="user", content=message)
        self._history.append(user_entry)

        reply_content = self._build_response(message)
        reply_entry = Message(role="assistant", content=reply_content)
        self._history.append(reply_entry)

        return reply_entry

    def history(self) -> List[Dict[str, str]]:
        """Return the conversation history as serializable dictionaries."""
        return [entry.serialize() for entry in self._history]


__all__ = ["ChatBot", "Message"]