from fastapi import APIRouter, Depends, HTTPException
from typing import List
from supabase import Client

from ..models.event import Event, EventCreate, EventUpdate, EventRegistrationCreate
from ..crud import event as crud_event
from ..dependencies import get_current_user, get_supabase

router = APIRouter(
    prefix="/events",
    tags=["Events"],
    dependencies=[]
)

@router.post("/", response_model=Event)
async def create_event(
    event: EventCreate,
    db: Client = Depends(get_supabase)
):
    return await crud_event.get_crud_event(db).create(event)

@router.get("/", response_model=List[Event])
async def read_events(
    skip: int = 0,
    limit: int = 100,
    db: Client = Depends(get_supabase)
):
    return await crud_event.get_crud_event(db).get_multi(skip, limit)

@router.get("/{event_id}", response_model=Event)
async def read_event(
    event_id: int,
    db: Client = Depends(get_supabase)
):
    event = await crud_event.get_crud_event(db).get(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}", response_model=Event)
async def update_event(
    event_id: int,
    event: EventUpdate,
    db: Client = Depends(get_supabase)
):
    return await crud_event.get_crud_event(db).update(event_id, event)

@router.delete("/{event_id}")
async def delete_event(
    event_id: int,
    db: Client = Depends(get_supabase)
):
    return await crud_event.get_crud_event(db).delete(event_id)

@router.post("/{event_id}/register", response_model=dict)
async def register_for_event(
    event_id: int,
    registration: EventRegistrationCreate,
    db: Client = Depends(get_supabase)
):
    return await crud_event.get_crud_event(db).register(event_id, registration)

@router.delete("/{event_id}/unregister/{member_id}")
async def unregister_from_event(
    event_id: int,
    member_id: int,
    db: Client = Depends(get_supabase)
):
    return await crud_event.get_crud_event(db).unregister(event_id, member_id)