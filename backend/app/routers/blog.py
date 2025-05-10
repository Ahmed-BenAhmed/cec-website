from fastapi import APIRouter, Depends, HTTPException
from typing import List
from supabase import Client

from ..models.blog import BlogPost, BlogPostCreate, BlogPostUpdate
from ..dependencies import get_current_user, get_supabase
from ..crud import blog as crud_blog

router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
)

@router.post("/", response_model=BlogPost)
async def create_blog_post(
    post: BlogPostCreate,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_user)
):
    return await crud_blog.get_crud_blog(db).create(post, current_user["id"])

@router.get("/", response_model=List[BlogPost])
async def read_blog_posts(
    skip: int = 0,
    limit: int = 100,
    db: Client = Depends(get_supabase)
):
    return await crud_blog.get_crud_blog(db).get_multi(skip, limit)

@router.get("/{post_id}", response_model=BlogPost)
async def read_blog_post(
    post_id: int,
    db: Client = Depends(get_supabase)
):
    post = await crud_blog.get_crud_blog(db).get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    
    # Increment view count
    await crud_blog.get_crud_blog(db).increment_views(post_id)
    return post

@router.put("/{post_id}", response_model=BlogPost)
async def update_blog_post(
    post_id: int,
    post: BlogPostUpdate,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_user)
):
    # Verify ownership before update
    existing_post = await crud_blog.get_crud_blog(db).get(post_id)
    if existing_post["author_id"] != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to update this post")
    
    return await crud_blog.get_crud_blog(db).update(post_id, post)

@router.delete("/{post_id}")
async def delete_blog_post(
    post_id: int,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_user)
):
    # Verify ownership before delete
    existing_post = await crud_blog.get_crud_blog(db).get(post_id)
    if existing_post["author_id"] != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    
    return await crud_blog.get_crud_blog(db).delete(post_id)