from pydantic import BaseModel


class PagingBase(BaseModel):
    total: int
    page: int
