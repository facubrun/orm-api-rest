from typing import List

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from api import Base

# Modelo Author
class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    nationality: Mapped[str]

    # relacion many to many con podcasts
    podcasts: Mapped[List["Podcast"]] = relationship(secondary="podcasts_authors", back_populates="authors")