"""FastAPI application that exposes welcome message endpoints."""
from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field


class WelcomeMessage(BaseModel):
    """Schema for requests and responses involving the welcome message."""

    message: str = Field(..., description="Mensaje de bienvenida a mostrar")


app = FastAPI(title="Dev Containers Python Template")


class _WelcomeMessageStore:
    """In-memory store for the welcome message."""

    def __init__(self, initial_message: str) -> None:
        self._message = initial_message

    def get(self) -> WelcomeMessage:
        return WelcomeMessage(message=self._message)

    def set(self, new_message: WelcomeMessage) -> WelcomeMessage:
        self._message = new_message.message
        return self.get()


_message_store = _WelcomeMessageStore(
    "Bienvenido a la plantilla de Dev Containers para Python"
)


@app.get("/api/welcome", response_model=WelcomeMessage)
def read_welcome() -> WelcomeMessage:
    """Return the current welcome message."""

    return _message_store.get()


@app.post("/api/welcome", response_model=WelcomeMessage)
def update_welcome(payload: WelcomeMessage) -> WelcomeMessage:
    """Update the welcome message using the provided payload."""

    return _message_store.set(payload)


__all__ = ["app"]
