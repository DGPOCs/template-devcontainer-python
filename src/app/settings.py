"""Application settings sourced from environment variables."""
from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv

# Load environment variables defined in a local .env file if present.
load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Configuration values for the application."""

    devto_api_key: str | None


@lru_cache()
def get_settings() -> Settings:
    """Return the cached application settings."""

    return Settings(devto_api_key=os.getenv("DEVTO_API_KEY"))


__all__ = ["Settings", "get_settings"]
