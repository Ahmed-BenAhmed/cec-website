from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, HttpUrl
from .base import BaseSchemas
from .member import Member

class ProjectBase(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: Optional[datetime] = None
    github_url: Optional[HttpUrl] = None
    demo_url: Optional[HttpUrl] = None
    cover_image_url: Optional[str] = None
    tags: List[str] = []

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = None
    github_url: Optional[HttpUrl] = None
    demo_url: Optional[HttpUrl] = None
    cover_image_url: Optional[str] = None
    tags: Optional[List[str]] = None

class ProjectMember(BaseModel):
    member: Member
    role: str
    contribution: Optional[str] = None

    class Config:
        from_attributes = True

class ProjectMemberCreate(BaseModel):
    member_id: int
    role: str
    contribution: Optional[str] = None

class Project(ProjectBase, BaseSchemas):
    id: int
    status: str
    members: List[ProjectMember] = []