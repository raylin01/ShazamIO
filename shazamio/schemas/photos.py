from typing import Optional

from pydantic.v1 import BaseModel
from pydantic.v1 import Field


class ImageModel(BaseModel):
    width: int
    url: str
    height: int
    text_color3: Optional[str] = Field(None, alias="textColor3")
    text_color2: Optional[str] = Field(None, alias="textColor2")
    text_color4: Optional[str] = Field(None, alias="textColor4")
    text_color1: Optional[str] = Field(None, alias="textColor1")
    bg_color: Optional[str] = Field(None, alias="bgColor")
    has_p3: bool = Field(..., alias="hasP3")
