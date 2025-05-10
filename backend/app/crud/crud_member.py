from typing import Optional
from supabase import Client
from ..models.member import MemberCreate, MemberUpdate, Member
from fastapi import HTTPException, status

class CRUDMember:
    def __init__(self, db: Client):
        self.db = db

    async def get(self, id: int) -> Optional[Member]:
        res = self.db.table('members').select('*').eq('id', id).execute()
        return res.data[0] if res.data else None

    async def get_by_email(self, email: str) -> Optional[Member]:
        res = self.db.table('members').select('*').eq('email', email).execute()
        return res.data[0] if res.data else None

    async def create(self, member: MemberCreate) -> Member:
        # In a real app, hash the password before storing
        data = member.dict(exclude={'password'})
        data['hashed_password'] = "hashed_" + member.password  # Replace with real hashing
        
        res = self.db.table('members').insert(data).execute()
        return res.data[0]

    async def update(self, id: int, member: MemberUpdate) -> Member:
        data = member.dict(exclude_unset=True)
        if not data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No data to update"
            )
        
        res = self.db.table('members').update(data).eq('id', id).execute()
        if not res.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Member not found"
            )
        return res.data[0]

    async def delete(self, id: int) -> Member:
        res = self.db.table('members').delete().eq('id', id).execute()
        if not res.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Member not found"
            )
        return res.data[0]

def get_crud_member(db: Client) -> CRUDMember:
    return CRUDMember(db)

member = CRUDMember  # For dependency injection