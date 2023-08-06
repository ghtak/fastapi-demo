from typing import Annotated

from fastapi import APIRouter, Depends, Cookie

router = APIRouter(prefix='/dependencies', tags=['dependencies'])


class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False


checker = FixedContentQueryChecker("bar")


@router.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    return {"fixed_content_in_query": fixed_content_included}


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


CommonsDep = Annotated[dict, Depends(common_parameters)]


@router.get("/items/")
async def read_items(commons: CommonsDep):
    return commons


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@router.get("/items2/")
async def read_items2(commons: Annotated[CommonQueryParams, Depends(
    # CommonQueryParams
)]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response


def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(
        q: Annotated[str, Depends(query_extractor)],
        last_query: Annotated[str | None, Cookie()] = None,
):
    if not q:
        return last_query
    return q


@router.get("/items3/")
async def read_query(
        query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]
):
    return {"q_or_cookie": query_or_default}
