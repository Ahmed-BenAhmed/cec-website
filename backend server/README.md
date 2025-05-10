Here are the `requirements.txt` and `README.md` files for your project:

### `requirements.txt`
```text
fastapi==0.109.1
uvicorn==0.27.0
supabase==2.3.1
python-dotenv==1.0.0
python-jose[cryptography]==3.3.0
passlib==1.7.4
pydantic==2.6.1
httpx==0.26.0
```

pip install passlib httpx python-jose[cryptography]

### `README.md`
```markdown
# CEC Club Backend API

This is the backend API for the Computer Engineering Club (CEC) built with FastAPI and Supabase.

## Features

- Member management
- Project tracking
- Event organization
- Blog system
- JWT Authentication
- Supabase integration

## Prerequisites

- Python 3.9+
- Supabase account
- PostgreSQL database

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cec-club-backend.git
cd cec-club-backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your credentials:
```ini
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
JWT_SECRET_KEY=your_secure_jwt_secret
```

## Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at:
- `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`
- Redoc docs: `http://localhost:8000/redoc`

## Database Setup

1. Create tables in Supabase using the following schema:
```sql
-- Members table
CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    university_id VARCHAR(50) NOT NULL,
    study_program VARCHAR(255) NOT NULL,
    year_of_study INTEGER NOT NULL,
    bio TEXT,
    skills TEXT[] DEFAULT ARRAY[]::TEXT[],
    profile_picture_url VARCHAR(255),
    join_date TIMESTAMP DEFAULT NOW(),
    role VARCHAR(50) DEFAULT 'member',
    status VARCHAR(20) DEFAULT 'active',
    hashed_password VARCHAR(255) NOT NULL
);

-- Projects table
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,
    status VARCHAR(20) DEFAULT 'planning',
    github_url VARCHAR(255),
    demo_url VARCHAR(255),
    cover_image_url VARCHAR(255),
    tags TEXT[] DEFAULT ARRAY[]::TEXT[]
);

-- Project members junction table
CREATE TABLE project_members (
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    member_id INTEGER REFERENCES members(id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL,
    contribution TEXT,
    PRIMARY KEY (project_id, member_id)
);

-- Events table
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    event_date TIMESTAMP NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    location VARCHAR(255) NOT NULL,
    event_link VARCHAR(255),
    cover_image_url VARCHAR(255),
    registration_required BOOLEAN DEFAULT FALSE,
    max_attendees INTEGER,
    status VARCHAR(20) DEFAULT 'upcoming'
);

-- Event registrations table
CREATE TABLE event_registrations (
    id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
    member_id INTEGER REFERENCES members(id) ON DELETE CASCADE,
    registration_date TIMESTAMP DEFAULT NOW(),
    attendance_status VARCHAR(20) DEFAULT 'registered'
);

-- Blog posts table
CREATE TABLE blog_posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER REFERENCES members(id) ON DELETE CASCADE,
    publish_date TIMESTAMP DEFAULT NOW(),
    last_updated TIMESTAMP DEFAULT NOW(),
    status VARCHAR(20) DEFAULT 'draft',
    featured_image_url VARCHAR(255),
    tags TEXT[] DEFAULT ARRAY[]::TEXT[],
    views_count INTEGER DEFAULT 0
);
```

## API Endpoints

| Endpoint Group | Description |
|----------------|-------------|
| `/auth` | Authentication endpoints |
| `/members` | Member management |
| `/projects` | Project management |
| `/events` | Event management |
| `/blog` | Blog system |



### BACKEND ENTITIES

Core Entities
1. Members
   member_id (PK)

first_name

last_name

email (unique)

phone

university_id

study_program

year_of_study

join_date

role (member, admin, etc.)

bio

skills (array)

profile_picture_url

status (active, alumni)

2. Projects
   project_id (PK)

title

description

start_date

end_date (nullable)

status (planning, in-progress, completed, archived)

github_url (nullable)

demo_url (nullable)

cover_image_url

tags (array of tech stacks)

3. Project Members (Junction table)
   project_id (FK)

member_id (FK)

role (lead, developer, designer, etc.)

contribution

4. Events
event_id (PK)

title

description

event_date

start_time

end_time

location (physical/virtual)

event_link (for virtual events)

cover_image_url

registration_required (boolean)

max_attendees (nullable)

status (upcoming, ongoing, completed, canceled)

5. Event Registrations
   registration_id (PK)

event_id (FK)

member_id (FK)

registration_date

attendance_status (registered, attended, no-show)

6. Blog Posts
   post_id (PK)

title

content

author_id (FK to Members)

publish_date

last_updated

status (draft, published, archived)

featured_image_url

tags (array)

views_count

9. Contact Messages
   message_id (PK)

sender_name

sender_email

subject

message

received_date

status (new, in-progress, resolved)

responded_by (FK to Members, nullable)

response_date (nullable)