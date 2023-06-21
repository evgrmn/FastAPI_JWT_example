from fastapi import APIRouter, Depends, HTTPException

import app.control.user as _control
from app.database.data import Users as users
from app.schemas.user import Salary, User

router = APIRouter()


@router.get(
    "/all",
    response_model=list[User],
    status_code=200,
    summary="A list of Employees",
)
async def get_employees() -> list:
    """
    A list of Employees
    """

    return list(users.data.values())


@router.get(
    "/me",
    response_model=Salary,
    status_code=200,
    summary="Employee salary information",
)
async def employee(
    user: dict = Depends(_control.get_current_user),
) -> Salary:
    """
    Employee salary information
    """
    try:
        employee = users.data[user["username"]]
    except Exception:
        raise HTTPException(status_code=404, detail="Employee not found")

    return Salary.parse_obj(employee)
