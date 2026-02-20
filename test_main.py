import pytest
import asyncio
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "version" in response.json()

@pytest.mark.asyncio
async def test_api_docs_available():
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        response = await ac.get("/docs")
    # The docs endpoint should be available
    assert response.status_code in [200, 307]  # May redirect but should be accessible

# Additional tests would go here for auth, tasks, etc.