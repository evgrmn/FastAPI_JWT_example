from __future__ import annotations

import httpx
import pytest
import pytest_asyncio

from main import app

pytestmark = pytest.mark.asyncio


@pytest_asyncio.fixture
async def client():
    cl = httpx.AsyncClient(app=app)
    yield cl
    await cl.aclose()


url = "http://test/api/v1/"
