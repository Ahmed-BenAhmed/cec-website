from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from .routers import auth, members, projects, events, blog
load_dotenv()

app = FastAPI(
    title="CEC Club API",
    description="API for the Computer Engineering Club",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Supabase Client Setup
def get_supabase() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    return create_client(url, key)

# Include routers
app.include_router(auth.router)
app.include_router(members.router)
app.include_router(projects.router)
app.include_router(events.router)
app.include_router(blog.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to CEC Club API"}