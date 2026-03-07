from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# creacion del conector a la base de datos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost/wordcast"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


# genero la sesion
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        # se devuelve la sesion de la bd
        yield db
    finally:
        # se cierra la sesion de la bd
        db.close()