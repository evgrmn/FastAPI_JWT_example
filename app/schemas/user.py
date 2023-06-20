from __future__ import annotations

from pydantic import BaseModel


class User(BaseModel):
    username: str
    full_name: str
    email: str


class Salary(BaseModel):
    salary: str
    salary_rise_date: str
