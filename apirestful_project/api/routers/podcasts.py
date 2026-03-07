from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from api import podcast_controller, get_db
from api import PodcastSchema, PodcastCreateSchema, PodcastUpdateSchema

# Enrutador donde se definen los endpoints
router = APIRouter()


@router.get("/", response_model=list[PodcastSchema])
async def read_podcast(db: Session = Depends(get_db)):
    podcasts = podcast_controller.get_podcasts(db)
    if podcasts == None:
        raise HTTPException(status_code=503, detail="DB Unavailable")
    return podcasts


@router.get("/{podcast_id}", response_model=PodcastSchema)
async def read_podcast(podcast_id: int, db: Session = Depends(get_db)):
    podcast = podcast_controller.get_podcast(db, podcast_id)
    if podcast == None:
        raise HTTPException(status_code=404, detail="Podcast not found")
    return podcast


@router.post("/", response_model=PodcastSchema)
async def write_podcast(podcast: PodcastCreateSchema, db: Session = Depends(get_db)):
    podcastResult = podcast_controller.write_podcast(db, podcast)
    return podcastResult


@router.put("/{podcast_id}", response_model=PodcastSchema)
async def update_podcast(podcast_id: int, podcast: PodcastUpdateSchema, db: Session = Depends(get_db)):
    podcastResult = podcast_controller.update_podcast(db, podcast_id, podcast)
    if podcastResult == None:
        raise HTTPException(status_code=404, detail="Podcast not found")
    return podcastResult


@router.delete("/{podcast_id}", response_model=list[PodcastSchema])
async def delete_podcast(podcast_id: int, db: Session = Depends(get_db)):
    podcasts = podcast_controller.delete_podcast(db, podcast_id)
    if podcasts == None:
        raise HTTPException(status_code=404, detail="Podcast not found")
    return podcasts