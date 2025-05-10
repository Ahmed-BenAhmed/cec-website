from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, HttpUrl

class BaseSchemas(BaseModel):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True