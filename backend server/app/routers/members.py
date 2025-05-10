from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from supabase import Client

from ..models.member import Member, MemberCreate, MemberUpdate
from ..crud import member as crud_member
from ..dependencies import get_current_user, get_supabase

router = APIRouter(
    prefix="/members",
    tags=["Members"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/", response_model=Member)
async def create_member(
    member: MemberCreate,
    db: Client = Depends(get_supabase)
):
    return await crud_member.get_crud_member(db).create(member)

@router.get("/", response_model=List[Member])
async def read_members(
    skip: int = 0,
    limit: int = 100,
    db: Client = Depends(get_supabase)
):
    return await crud_member.get_crud_member(db).get_multi(skip, limit)

@router.get("/{member_id}", response_model=Member)
async def read_member(
    member_id: int,
    db: Client = Depends(get_supabase)
):
    member = await crud_member.get_crud_member(db).get(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@router.put("/{member_id}", response_model=Member)
async def update_member(
    member_id: int,
    member: MemberUpdate,
    db: Client = Depends(get_supabase)
):
    return await crud_member.get_crud_member(db).update(member_id, member)

@router.delete("/{member_id}")
async def delete_member(
    member_id: int,
    db: Client = Depends(get_supabase)
):
    return await crud_member.get_crud_member(db).delete(member_id)