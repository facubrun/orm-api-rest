from fastapi import APIRouter, Depends, FastAPI, HTTPException
from api import category
from sqlalchemy.orm import Session
from api.database.database import get_db
from api import CategorySchema

# enrutador donde se definen endpoints
router = APIRouter()

@router.get("/", response_model=list[CategorySchema])
async def read_categories(db: Session = Depends(get_db)):
    return category.get_categories(db)

@router.post("/")
async def create_category(db: Session = Depends(get_db)):
    return {"message": "Category created"}

@router.put("/{category_id}")
async def update_category(category_id: int, db: Session = Depends(get_db)):
    return {"message": f"Category with ID {category_id} updated"}

@router.delete("/")
async def delete_category(db: Session = Depends(get_db)):
    return {"message": f"Categories deleted"}

