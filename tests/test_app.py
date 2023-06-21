import time

import pytest

from app.config.settings import env
from app.database.data import Users as users

from .conftest import url
from .variables import Vars as var

pytestmark = pytest.mark.asyncio


async def test_api(client):
    """
    Check the endpoint with a list of all employees
    """
    r = await client.get(f"{url}user/all")
    assert r.status_code == 200, "wrong response"


async def test_not_authenticated(client):
    """
    Checking the endpoint with information about the employee. Status_code 
    should be 401 (Unauthorized Error), because employee is not authorized
    """
    r = await client.get(f"{url}user/me")
    assert r.status_code == 401, "wrong response"


async def test_wrong_auth(client):
    """
    Create a token for an employee with 0.5 second expiration with 
    wrong password
    """
    env.ACCESS_TOKEN_EXPIRE_MILLISECONDS = 500
    r = await client.post(
        f"{url}auth/token",
        data={"username": var.username, "password": "wrong_pass"},
    )
    assert r.status_code == 401, "wrong response"


async def test_create_token(client):
    """
    Create a token for an employee with an expiration time of 0.5 seconds
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
    Checking the endpoint with information about the employee
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
    Checking the endpoint with information about the employee 2 seconds 
    after the creation of the token. Status_code should be 401 
    (Unauthorized Error) because the token that was created in the 
    previous test is already expired
    """
    time.sleep(2)
    r = await client.get(
        f"{url}user/me", headers={"Authorization": f"Bearer {var.token}"}
    )
    assert r.status_code == 401, "wrong response"
