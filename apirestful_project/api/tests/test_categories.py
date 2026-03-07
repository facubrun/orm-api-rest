from fastapi.testclient import TestClient
from api import app

# generamos el test cliente
client = TestClient(app)

# test del endpoint GET /categories
def test_read_categories():
    response = client.get("/categories/")
    assert response.status_code == 200