"""FastAPI server exposing a simple chatbot."""

from __future__ import annotations

from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .chatbot import ChatBot

app = FastAPI(title="Simple ChatBot API", version="0.1.0")
_bot_sessions: Dict[str, ChatBot] = {}


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


class ChatResponse(BaseModel):
    reply: str
    history: list[dict[str, str]]


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Receive a user message and return the bot's reply."""
    session_id = request.session_id.strip() or "default"

    if len(session_id) > 64:
        raise HTTPException(status_code=400, detail="session_id слишком длинный")

    bot = _bot_sessions.setdefault(session_id, ChatBot())
    reply_message = bot.ask(request.message)

    return ChatResponse(reply=reply_message.content, history=bot.history())


@app.get("/health")
def health() -> dict[str, str]:
    """Simple health-check endpoint."""
    return {"status": "ok"}