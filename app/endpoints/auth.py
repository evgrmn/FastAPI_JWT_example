from fastapi import APIRouter, Depends, HTTPException, security

import app.control.user as _control
from app.schemas.token import Token

router = APIRouter()


@router.post(
    "/token",
    response_model=Token,
    status_code=200,
    summary="Generate token",
)
async def generate_token(
    form_data: security.OAuth2PasswordRequestForm = Depends(),
) -> dict:
    """
    Generate token
    """
    user = await _control.authenticate_user(
        name=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=401, detail="Incorrect login or password")

    return await _control.create_token(user=user)
