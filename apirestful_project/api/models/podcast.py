from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import TYPE_CHECKING, List
from api import Base, podcasts_authors

if TYPE_CHECKING:
    from api.models.category import Category

# Modelo Podcast
class Podcast(Base):
    __tablename__ = "podcasts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    url: Mapped[str]

    # relacion many to one con category
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="podcasts")

    #relacion many to many con authors
    authors: Mapped[List["Author"]] = relationship(secondary="podcasts_authors", back_populates="podcasts")