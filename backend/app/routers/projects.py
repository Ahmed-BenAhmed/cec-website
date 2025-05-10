from fastapi import APIRouter, Depends, HTTPException
from typing import List
from supabase import Client

from ..models.project import Project, ProjectCreate, ProjectUpdate, ProjectMemberCreate
from ..crud import project as crud_project, CRUDProject
from ..dependencies import get_current_user, get_supabase

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)

@router.post("/", response_model=Project)
async def create_project(
    project: ProjectCreate,
    db: Client = Depends(get_supabase)
):
    return await crud_project.get_crud_project(db).create(project)

@router.get("/", response_model=List[Project])
async def read_projects(
    skip: int = 0,
    limit: int = 100,
    db: Client = Depends(get_supabase)
):
    # crud = CRUDProject(db)  # Create instance directly
    # return await crud.get_multi(skip, limit)
    return await crud_project.get_crud_project(db).get_multi(skip, limit)

@router.get("/{project_id}", response_model=Project)
async def read_project(
    project_id: int,
    db: Client = Depends(get_supabase)
):
    project = await crud_project.get_crud_project(db).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=Project)
async def update_project(
    project_id: int,
    project: ProjectUpdate,
    db: Client = Depends(get_supabase)
):
    return await crud_project.get_crud_project(db).update(project_id, project)

@router.delete("/{project_id}")
async def delete_project(
    project_id: int,
    db: Client = Depends(get_supabase)
):
    return await crud_project.get_crud_project(db).delete(project_id)

@router.post("/{project_id}/members", response_model=dict)
async def add_project_member(
    project_id: int,
    member: ProjectMemberCreate,
    db: Client = Depends(get_supabase)
):
    return await crud_project.get_crud_project(db).add_member(project_id, member)

@router.delete("/{project_id}/members/{member_id}")
async def remove_project_member(
    project_id: int,
    member_id: int,
    db: Client = Depends(get_supabase)
):
    return await crud_project.get_crud_project(db).remove_member(project_id, member_id)