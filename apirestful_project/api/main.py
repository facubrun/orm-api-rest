from fastapi import FastAPI
from . import categories_router
from . import tags_metadata

# apirestful con fastapi
app = FastAPI(
    title="API RESTful para podcast con FastAPI",
    description="API RESTful utilizando FastAPI y SQLAlchemy",
    version="1.0.0",
    contact={
        "name": "Facundo Brun",
    },
    
    openapi_tags=tags_metadata
)

# importacion de rutas
app.include_router(categories_router, prefix="/categories", tags=["categories"])

@app.get("/")
async def root():
    return {"message": "Hello World"}