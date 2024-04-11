from typing import List
from typing import Optional

from pydantic.v1 import BaseModel
from pydantic.v1 import Field


class AttributeName(BaseModel):
    title: str


class ArtistAttribute(BaseModel):
    genre_names: List[str] = Field([], alias="genreNames")
    name: str
    url: str
    artist_bio: Optional[str] = Field(None, alias="artistBio")
