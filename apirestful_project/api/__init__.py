from api.database.database import engine, SessionLocal, get_db

# documentacion
from api.configdoc import tags_metadata

# modelos db
from api.models.category import Category as CategoryModel

# schemas pydantic
from api.schemas.category import Category as CategorySchema
from api.schemas.category import CategoryCreate as CategoryCreateSchema
from api.schemas.podcast import Podcast as PodcastSchema
from api.schemas.podcast import PodcastCreate as PodcastCreateSchema
from api.schemas.podcast import PodcastUpdate as PodcastUpdateSchema
from api.schemas.author import Author as AuthorSchema
from api.schemas.author import AuthorCreate as AuthorCreateSchema
from api.schemas.author import AuthorUpdate as AuthorUpdateSchema

# controladores
from api.controllers import category as category_controller
from api.controllers import podcast as podcast_controller
from api.controllers import author as author_controller

# rutas
from api.routers.categories import router as categories_router 
from api.routers.podcasts import router as podcasts_router
from api.routers.authors import router as authors_router

# app 
from api.main import app