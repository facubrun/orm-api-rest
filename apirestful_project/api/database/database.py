from sqlalchemy import create_engine

# creacion del conector a la base de datos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost/wordcast"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)