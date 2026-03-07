from sqlalchemy import select
from api.models.category import Category as CategoryModel
from api.schemas.category import CategoryCreate as CategoryCreateSchema
from sqlalchemy.exc import SQLAlchemyError, NoResultFound

def get_categories(db):
    # crear la consulta
    stmt = select(CategoryModel)
    # lista de categorias
    result = db.scalars(stmt)
    categories = result.all()
    return categories

def get_category(db, category_id: int):
    try:
        # crear la consulta
        categoryModel = db.execute(select(CategoryModel).where(CategoryModel.id == category_id)).scalars().first()
    except NoResultFound:
        categoryModel = None
    return categoryModel

def create_category(db, category: CategoryCreateSchema):
    # crear modelo orm a partir del schema
    categoryModel = CategoryModel(name=category.name)
    # insertamos en la bd
    db.add(categoryModel)
    db.commit()
    db.refresh(categoryModel)
    return categoryModel

def update_category(db, category_id: int, category: CategoryCreateSchema):
    try:
        # buscar categoria por id en la bd
        result = db.execute(select(CategoryModel).where(CategoryModel.id == category_id))
        categoryModel = result.scalar_one()
        # actualizar los campos de la categoria
        category_db.name = category.name
        # guardar los cambios en la bd
        db.commit()
        db.refresh(category_db)
    except NoResultFound:
        categoryModel = None
    return categoryModel

def delete_category(db, category_id: int):
    try:
        # buscar categoria por id en la bd
        category_db = db.get(CategoryModel, category_id)
        # eliminar la categoria de la bd
        db.delete(category_db)
        db.commit()
        categories = get_categories(db)
    except UnmappedInstanceError:
        categories = None
    # devolver la lista actualizada de categorias
    return categories