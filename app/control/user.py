from datetime import datetime, timedelta

import fastapi.security as _security
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config.settings import env
from app.database.data import Users as users

oath2schema = _security.OAuth2PasswordBearer("/api/v1/auth/token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_current_user(
    token: str = Depends(oath2schema),
) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password or JWT token has expired",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, env.JWT_SECRET, algorithms=["HS256"])
    except JWTError:
        raise credentials_exception

    return payload


async def create_token(user: dict) -> dict:
    exp_time = env.ACCESS_TOKEN_EXPIRE_MILLISECONDS
    user["exp"] = datetime.utcnow() + timedelta(milliseconds=exp_time)
    token = jwt.encode(user, env.JWT_SECRET)

    return dict(access_token=token, token_type="bearer")


async def authenticate_user(name: str, password: str):
    try:
        user = users.data[name]
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )
    if not pwd_context.verify(password, user["hashed_password"]):
        return False

    return users.data[name]
