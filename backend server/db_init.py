import os
from dotenv import load_dotenv
from supabase import create_client
from faker import Faker
import random
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# Initialize Faker for fake data
fake = Faker()

# Connect to Supabase
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def init_members(count=10):
    """Initialize members table with sample data"""
    print("Initializing members...")
    for _ in range(count):
        member_data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "university_id": fake.uuid4()[:8],
            "study_program": random.choice(["Computer Science", "Engineering", "IT", "Data Science"]),
            "year_of_study": random.randint(1, 5),
            "bio": fake.text(),
            "skills": random.sample(["Python", "JavaScript", "Java", "C++", "React", "Node.js"], 3),
            "join_date": datetime.now().isoformat(),
            "role": random.choice(["member", "admin", "lead"]),
            "status": "active"
        }
        supabase.table("members").insert(member_data).execute()

def init_projects(count=5):
    """Initialize projects table with sample data"""
    print("Initializing projects...")
    statuses = ["planning", "in-progress", "completed"]
    tech_stack = ["Python", "JavaScript", "React", "Django", "Flask", "FastAPI", "Node.js"]
    
    for _ in range(count):
        project_data = {
            "title": fake.catch_phrase(),
            "description": fake.text(),
            "start_date": datetime.now().isoformat(),
            "end_date": (datetime.now() + timedelta(days=random.randint(30, 90))).isoformat(),
            "status": random.choice(statuses),
            "github_url": f"https://github.com/{fake.user_name()}/{fake.word()}",
            "tags": random.sample(tech_stack, 3),
            "cover_image_url": f"https://picsum.photos/800/400?random={random.randint(1,100)}"
        }
        res = supabase.table("projects").insert(project_data).execute()
        project_id = res.data[0]["id"]
        
        # Add random members to project
        members = supabase.table("members").select("id").execute().data
        for member in random.sample(members, min(3, len(members))):
            supabase.table("project_members").insert({
                "project_id": project_id,
                "member_id": member["id"],
                "role": random.choice(["lead", "developer", "designer"]),
                "contribution": fake.sentence()
            }).execute()

def init_events(count=6):
    """Initialize events table with sample data"""
    print("Initializing events...")
    event_types = ["Workshop", "Hackathon", "Seminar", "Meetup", "Competition"]
    
    for _ in range(count):
        event_date = datetime.now() + timedelta(days=random.randint(1, 30))
        event_data = {
            "title": f"{random.choice(event_types)}: {fake.catch_phrase()}",
            "description": fake.text(),
            "event_date": event_date.isoformat(),
            "start_time": (event_date + timedelta(hours=10)).isoformat(),
            "end_time": (event_date + timedelta(hours=14)).isoformat(),
            "location": fake.address(),
            "registration_required": random.choice([True, False]),
            "max_attendees": random.choice([None, 20, 50, 100]),
            "cover_image_url": f"https://picsum.photos/800/400?random={random.randint(100,200)}",
            "status": "upcoming"
        }
        res = supabase.table("events").insert(event_data).execute()
        event_id = res.data[0]["id"]
        
        # Add random registrations
        if event_data["registration_required"]:
            members = supabase.table("members").select("id").execute().data
            for member in random.sample(members, min(5, len(members))):
                supabase.table("event_registrations").insert({
                    "event_id": event_id,
                    "member_id": member["id"],
                    "registration_date": datetime.now().isoformat(),
                    "attendance_status": "registered"
                }).execute()

def init_blog_posts(count=8):
    """Initialize blog_posts table with sample data"""
    print("Initializing blog posts...")
    members = supabase.table("members").select("id").execute().data
    
    for _ in range(count):
        post_date = datetime.now() - timedelta(days=random.randint(1, 30))
        post_data = {
            "title": fake.sentence(),
            "content": "\n\n".join(fake.paragraphs(5)),
            "author_id": random.choice(members)["id"],
            "publish_date": post_date.isoformat(),
            "last_updated": post_date.isoformat(),
            "status": "published",
            "featured_image_url": f"https://picsum.photos/800/400?random={random.randint(200,300)}",
            "tags": random.sample(["technology", "programming", "webdev", "datascience"], 2),
            "views_count": random.randint(0, 500)
        }
        supabase.table("blog_posts").insert(post_data).execute()

if __name__ == "__main__":
    print("Starting database initialization...")
    init_members(15)
    init_projects(5)
    init_events(6)
    init_blog_posts(8)
    print("Database initialization complete!")