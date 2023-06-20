import time

import pytest

from app.config.settings import env
from app.database.data import Users as users

from .conftest import url
from .variables import Vars as var

pytestmark = pytest.mark.asyncio


async def test_api(client):
    """
    Проверям эндпоинт со списком всех работников
    """
    r = await client.get(f"{url}user/all")
    assert r.status_code == 200, "wrong response"


async def test_not_authenticated(client):
    """
    Проверям эндпоинт с информацией о работнике. Status_code должен быть 401
    (Unauthorized Error), т.к. работник не авторизован
    """
    r = await client.get(f"{url}user/me")
    assert r.status_code == 401, "wrong response"


async def test_wrong_auth(client):
    """
    Создаем токен для сотрудника с экпирацией через 0.5 секунды
    с неправильным паролем
    """
    env.ACCESS_TOKEN_EXPIRE_MILLISECONDS = 500
    r = await client.post(
        f"{url}auth/token",
        data={"username": var.username, "password": "wrong_pass"},
    )
    assert r.status_code == 401, "wrong response"


async def test_create_token(client):
    """
    Создаем токен для сотрудника с экпирацией через 0.5 секунды
    """
    env.ACCESS_TOKEN_EXPIRE_MILLISECONDS = 500
    r = await client.post(
        f"{url}auth/token",
        data={"username": var.username, "password": var.password},
    )
    var.token = r.json()["access_token"]
    assert r.status_code == 200, "wrong response"


async def test_user_authenticated(client):
    """
    Проверям эндпоинт с информацией о работнике после создания токена для него
    """
    r = await client.get(
        f"{url}user/me", headers={"Authorization": f"Bearer {var.token}"}
    )
    response_data = r.json()
    assert r.status_code == 200, "wrong response"
    assert (
        response_data["salary"] == users.data[var.username]["salary"]
    ), "wrong salary amount"
    assert (
        response_data["salary_rise_date"] == users.data[var.username][
            "salary_rise_date"
        ]
    ), "wrong salary rise date"


async def test_token_expired(client):
    """
    Проверям эндпоинт с информацией о работнике через 2 секунды после
    создания токена. Status_code должен быть 401 (Unauthorized Error),
    т.к. токен, который был создан в предыдущем тесте, уже с истекшим
    сроком действия
    """
    time.sleep(2)
    r = await client.get(
        f"{url}user/me", headers={"Authorization": f"Bearer {var.token}"}
    )
    assert r.status_code == 401, "wrong response"
