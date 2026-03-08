from sqlalchemy import Column, ForeignKey, Integer, Table, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Base declarativa para los modelos ORM
Base = declarative_base()

# tabla asociacion entre podcasts y authors
podcasts_authors = Table(
    'podcasts_authors',
    Base.metadata,
    Column('podcast_id', Integer, ForeignKey('podcasts.id'), primary_key=True),
    Column('author_id', Integer, ForeignKey('authors.id'), primary_key=True)
)

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