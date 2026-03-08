from typing import List, Union
from pydantic import BaseModel

# Esquema para Categoría
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

# Esta clase necesita importar Podcast después
class CategoryPodcasts(CategoryBase):
    id: int
    podcasts: List["Podcast"] = []

    class Config:
        from_attributes = True  # Reemplaza orm_mode en Pydantic v2

# Import circular resuelto después de definir las clases
from api.schemas.podcast import Podcast
CategoryPodcasts.model_rebuild()