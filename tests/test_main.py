import pytest
from httpx import AsyncClient
import warnings
from trio import TrioDeprecationWarning
from app.main import app

warnings.filterwarnings(action='ignore', category=TrioDeprecationWarning)


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}
