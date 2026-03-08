from typing import Union, List, TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from api.schemas.podcast import Podcast as PodcastSchema

#Schemas de Podcasts
class AuthorBase(BaseModel):
    name: str
    nationality: str

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(BaseModel):
    name: Union[str, None] = None
    nationality: Union[str, None] = None

class AuthorPodcasts(AuthorBase):
    podcasts: List['PodcastSchema']

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True