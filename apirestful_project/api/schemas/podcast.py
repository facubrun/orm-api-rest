from typing import Union, List, TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from api.schemas.author import Author as AuthorSchema

#Schemas de Podcasts
class PodcastBase(BaseModel):
    title: str
    description: str
    url: str
    category_id: int

class PodcastCreate(PodcastBase):
    pass

class PodcastUpdate(BaseModel):
    title: Union[str, None] = None
    description: Union[str, None] = None
    url: Union[str, None] = None

class Podcast(PodcastBase):
    id: int

class PodcastAuthors(Podcast):
    authors: List['AuthorSchema']

    class Config:
        from_attributes = True