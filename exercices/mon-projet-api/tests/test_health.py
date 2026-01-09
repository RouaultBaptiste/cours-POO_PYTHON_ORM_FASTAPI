def test_health_endpoint(client):
    """
    Test de l'endpoint /health.
    Vérifie que l'endpoint retourne le statut "ok".
    """
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
