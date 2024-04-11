from typing import Generic
from typing import Optional
from typing import TypeVar

from pydantic.v1 import BaseModel
from pydantic.v1.generics import GenericModel


T = TypeVar("T", bound=BaseModel)


class BaseIdTypeHref(BaseModel):
    id: str
    type: str
    href: str


class BaseDataModel(GenericModel, BaseModel, Generic[T]):
    attributes: T


class BaseHrefNextData(GenericModel, Generic[T]):
    href: str
    next: Optional[str] = None
    data: T
