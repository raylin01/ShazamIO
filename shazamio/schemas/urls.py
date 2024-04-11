from pydantic.v1 import BaseModel


class UrlDTO(BaseModel):
    url: str
