from fastapi import APIRouter, Depends, HTTPException
from api import category_controller
from sqlalchemy.orm import Session
from api.database.database import get_db
from api import CategoryCreateSchema, CategorySchema

# enrutador donde se definen endpoints
router = APIRouter()

@router.get("/", response_model=list[CategorySchema])
async def read_categories(db: Session = Depends(get_db)):
    return category_controller.get_categories(db)

@router.get("/{category_id}", response_model=CategorySchema)
async def read_category(category_id: int, db: Session = Depends(get_db)):
    category = category_controller.get_category(db, category_id)
    if category == None:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
    return category

@router.post("/", response_model=CategorySchema)
async def create_category(category: CategoryCreateSchema, db: Session = Depends(get_db)):
    return category_controller.create_category(db, category)

@router.put("/{category_id}", response_model=CategorySchema)
async def update_category(category_id: int, category: CategoryCreateSchema, db: Session = Depends(get_db)):
    category = category_controller.update_category(db, category_id, category)
    if category == None:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
    return category

@router.delete("/{category_id}", response_model=list[CategorySchema])
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    categories = category_controller.delete_category(db, category_id)
    if categories == None:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
    return categories

