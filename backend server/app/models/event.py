from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, HttpUrl
from .base import BaseSchemas
from .member import Member

class EventBase(BaseModel):
    title: str
    description: str
    event_date: datetime
    start_time: datetime
    end_time: datetime
    location: str
    event_link: Optional[str] = None
    cover_image_url: Optional[str] = None
    registration_required: bool = False
    max_attendees: Optional[int] = None

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    event_date: Optional[datetime] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    location: Optional[str] = None
    event_link: Optional[str] = None
    cover_image_url: Optional[str] = None
    registration_required: Optional[bool] = None
    max_attendees: Optional[int] = None
    status: Optional[str] = None

class EventRegistration(BaseModel):
    id: int
    member: Member
    registration_date: datetime
    attendance_status: str

    class Config:
        from_attributes = True

class EventRegistrationCreate(BaseModel):
    member_id: int

class Event(EventBase, BaseSchemas):
    id: int
    status: str
    registrations: List[EventRegistration] = []