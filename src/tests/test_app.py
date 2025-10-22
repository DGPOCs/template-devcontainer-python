"""Tests for the FastAPI welcome message endpoints."""
from fastapi.testclient import TestClient

from importlib import reload

from app.main import app
import app.settings as app_settings


client = TestClient(app)


def test_read_welcome_returns_default_message() -> None:
    response = client.get("/api/welcome")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Bienvenido a la plantilla de Dev Containers para Python"
    }


def test_update_welcome_modifies_message() -> None:
    new_message = {"message": "Hola desde pruebas"}

    post_response = client.post("/api/welcome", json=new_message)
    assert post_response.status_code == 200
    assert post_response.json() == new_message

    get_response = client.get("/api/welcome")
    assert get_response.status_code == 200
    assert get_response.json() == new_message


def test_devto_api_key_is_loaded_from_environment(monkeypatch) -> None:
    monkeypatch.setenv("DEVTO_API_KEY", "test-api-key")

    settings = reload(app_settings)

    assert settings.get_settings().devto_api_key == "test-api-key"
    settings.get_settings.cache_clear()
