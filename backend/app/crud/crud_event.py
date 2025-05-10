from typing import List, Optional
from supabase import Client
from ..models.event import EventCreate, EventUpdate, Event, EventRegistrationCreate
from fastapi import HTTPException, status

class CRUDEvent:
    def __init__(self, db: Client):
        self.db = db

    async def get(self, id: int) -> Optional[Event]:
        res = self.db.table('events').select('*').eq('id', id).execute()
        return res.data[0] if res.data else None

    async def get_multi(self, skip: int = 0, limit: int = 100) -> List[Event]:
        res = self.db.table('events').select('*').range(skip, skip + limit).execute()
        return res.data

    async def create(self, event: EventCreate) -> Event:
        res = self.db.table('events').insert(event.dict()).execute()
        return res.data[0]

    async def update(self, id: int, event: EventUpdate) -> Event:
        data = event.dict(exclude_unset=True)
        res = self.db.table('events').update(data).eq('id', id).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Event not found")
        return res.data[0]

    async def delete(self, id: int) -> Event:
        res = self.db.table('events').delete().eq('id', id).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Event not found")
        return res.data[0]

    async def register(self, event_id: int, registration: EventRegistrationCreate) -> dict:
        data = registration.dict()
        data['event_id'] = event_id
        res = self.db.table('event_registrations').insert(data).execute()
        return res.data[0]

    async def unregister(self, event_id: int, member_id: int) -> dict:
        res = self.db.table('event_registrations')\
            .delete()\
            .eq('event_id', event_id)\
            .eq('member_id', member_id)\
            .execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Registration not found")
        return {"success": True}

    def get_crud_event(db: Client):
        return CRUDEvent(db)

event = CRUDEvent