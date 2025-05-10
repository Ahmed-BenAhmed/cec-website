from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, HttpUrl
from .base import BaseSchemas
from .member import Member

class BlogPostBase(BaseModel):
    title: str
    content: str
    featured_image_url: Optional[HttpUrl] = None
    tags: List[str] = []

class BlogPostCreate(BlogPostBase):
    pass

class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    featured_image_url: Optional[HttpUrl] = None
    tags: Optional[List[str]] = None
    status: Optional[str] = None

class BlogPost(BlogPostBase, BaseSchemas):
    id: int
    author: Member
    publish_date: datetime
    last_updated: datetime
    status: str
    views_count: int