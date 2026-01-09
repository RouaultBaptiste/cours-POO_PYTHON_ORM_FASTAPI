import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    """
    Fixture pytest qui crée un client de test pour l'application FastAPI.
    """
    return TestClient(app)

@pytest.fixture
def test_app():
    """
    Fixture pytest qui retourne l'instance de l'application FastAPI.
    """
    return app