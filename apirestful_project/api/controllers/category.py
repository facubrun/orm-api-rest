from sqlalchemy import select
from api import CategoryModel

def get_categories(db):
    # crear la consulta
    stmt = select(CategoryModel)
    # lista de categorias
    result = db.scalars(stmt)
    categories = result.all()
    return categories