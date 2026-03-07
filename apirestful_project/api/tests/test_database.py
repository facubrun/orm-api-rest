import pytest
from api import engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

# comprobacion de la conexion contra la bd
def test_database_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert len(result.fetchall()) == 1
    except SQLAlchemyError as e:
        pytest.fail(f"Error al conectar con la base de datos: {e}")