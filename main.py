from __future__ import annotations

import fastapi as _fastapi

from app.config.description import description
from app.endpoints import auth, user

app = _fastapi.FastAPI(
    title="FastAPI Application",
    description=description,
)


app.include_router(
    auth.router,
    prefix="/api/v1/auth",
    tags=["Создание токена"],
)

app.include_router(
    user.router,
    prefix="/api/v1/user",
    tags=["Работники"],
)
