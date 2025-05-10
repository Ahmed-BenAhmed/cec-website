from typing import List, Optional
from supabase import Client
from ..models.project import ProjectCreate, ProjectUpdate, Project, ProjectMemberCreate
from fastapi import HTTPException, status


class CRUDProject:
    def __init__(self, db: Client):
        self.db = db

    async def get(self, id: int) -> Optional[Project]:
        res = self.db.table('projects').select('*').eq('id', id).execute()
        return res.data[0] if res.data else None

    async def get_multi(self, skip: int = 0, limit: int = 100) -> List[Project]:
        res = self.db.table('projects').select('*').range(skip, skip + limit).execute()
        return res.data

    async def create(self, project: ProjectCreate) -> Project:
        res = self.db.table('projects').insert(project.dict()).execute()
        return res.data[0]

    async def update(self, id: int, project: ProjectUpdate) -> Project:
        data = project.dict(exclude_unset=True)
        res = self.db.table('projects').update(data).eq('id', id).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Project not found")
        return res.data[0]

    async def delete(self, id: int) -> Project:
        res = self.db.table('projects').delete().eq('id', id).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Project not found")
        return res.data[0]

    async def add_member(self, project_id: int, member: ProjectMemberCreate) -> dict:
        data = member.dict()
        data['project_id'] = project_id
        res = self.db.table('project_members').insert(data).execute()
        return res.data[0]

    async def remove_member(self, project_id: int, member_id: int) -> dict:
        res = self.db.table('project_members') \
            .delete() \
            .eq('project_id', project_id) \
            .eq('member_id', member_id) \
            .execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Membership not found")
        return {"success": True}

    def get_crud_project(db: Client):
        return CRUDProject(db)


project = CRUDProject
