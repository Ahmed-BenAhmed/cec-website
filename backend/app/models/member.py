from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, HttpUrl
from .base import BaseSchemas

class MemberBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    university_id: str
    study_program: str
    year_of_study: int
    bio: Optional[str] = None
    skills: List[str] = []
    profile_picture_url: Optional[HttpUrl] = None

class MemberCreate(MemberBase):
    password: str

class MemberUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    study_program: Optional[str] = None
    year_of_study: Optional[int] = None
    bio: Optional[str] = None
    skills: Optional[List[str]] = None
    profile_picture_url: Optional[HttpUrl] = None
    status: Optional[str] = None

class Member(MemberBase, BaseSchemas):
    id: int
    join_date: datetime
    role: str
    status: str