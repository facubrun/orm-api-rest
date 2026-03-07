from fastapi.testclient import TestClient
import pytest
from api import engine, app
from sqlalchemy import text

# generamos el test cliente
client = TestClient(app)

# fixture para inicializar la base de datos antes de cada test
@pytest.fixture
def db_init():
    # borrar todos los datos de DB/Table Category
    try:
        with (engine.connect() as conn):
            #Ahora mismo no hay relaciones pero cuando haya se deberá tener en cuenta para realizar el TRUNCATE
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
            conn.execute(text("TRUNCATE TABLE categories"))
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
            conn.execute(text("INSERT INTO categories (name) VALUES (:name)"),[
                {"name": "music"},{"name": "technology"},{"name": "food"},{"name": "sports"},{"name": "art"}])
            conn.commit()
    except SQLAlchemyError as excinfo:
            pytest.fail(f"Se ha producido un error en la conexion o en la consulta: {excinfo}")
# test del endpoint GET /categories
def test_read_categories():
    response = client.get("/categories/")
    assert response.status_code == 200

# test del endpoint GET /categories/{category_id}
def test_read_second_category():
    response = client.get("/categories/2")
    assert response.status_code == 200
    assert response.json() == {"id": 2, "name": "technology"}

# test del endpoint POST /categories/
def test_create_category(db_init):
    response = client.post("/categories/", json={"name": "new category"})
    assert response.status_code == 200
    assert response.json() == {"id": 6, "name": "new category"}

# test del endpoint DELETE /categories/{category_id}
def test_delete_category(db_init):
    response = client.delete("/categories/5")
    assert response.status_code == 200
    assert len(response.json()) == 4