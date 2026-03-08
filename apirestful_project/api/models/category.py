from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING
from api.database.database import Base

if TYPE_CHECKING:
    from api.models.podcast import Podcast

# Modelo Category
class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]

    # relacion one to many con podcasts
    podcasts: Mapped[list["Podcast"]] = relationship(back_populates="category")