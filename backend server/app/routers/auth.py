from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from supabase import Client
from jose import jwt
from datetime import timedelta, datetime
import os
from dotenv import load_dotenv

from ..models.schemas import Token, UserLogin
from ..crud import member as crud_member
from ..dependencies import get_supabase, SECRET_KEY, ALGORITHM

router = APIRouter(tags=["Authentication"])

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Client = Depends(get_supabase)
):
    user = await crud_member.get_crud_member(db).get_by_email(form_data.username)
    if not user or user["hashed_password"] != "hashed_" + form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
