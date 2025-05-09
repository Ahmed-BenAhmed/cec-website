from typing import List, Optional
from supabase import Client
from models.blog import BlogPostCreate, BlogPostUpdate, BlogPost
from fastapi import HTTPException, status

class CRUDBlog:
    def __init__(self, db: Client):
        self.db = db

    async def get(self, id: int) -> Optional[BlogPost]:
        res = self.db.table('blog_posts').select('*').eq('id', id).execute()
        return res.data[0] if res.data else None

    async def get_multi(self, skip: int = 0, limit: int = 100) -> List[BlogPost]:
        res = self.db.table('blog_posts').select('*').range(skip, skip + limit).execute()
        return res.data

    async def create(self, blog_post: BlogPostCreate, author_id: int) -> BlogPost:
        data = blog_post.dict()
        data['author_id'] = author_id
        res = self.db.table('blog_posts').insert(data).execute()
        return res.data[0]

    async def update(self, id: int, blog_post: BlogPostUpdate) -> BlogPost:
        data = blog_post.dict(exclude_unset=True)
        res = self.db.table('blog_posts').update(data).eq('id', id).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Blog post not found")
        return res.data[0]

    async def delete(self, id: int) -> BlogPost:
        res = self.db.table('blog_posts').delete().eq('id', id).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Blog post not found")
        return res.data[0]

    async def increment_views(self, id: int) -> BlogPost:
        res = self.db.rpc('increment_blog_views', {'post_id': id}).execute()
        return res.data[0] if res.data else None

def get_crud_blog(db: Client) -> CRUDBlog:
    return CRUDBlog(db)

blog = CRUDBlog