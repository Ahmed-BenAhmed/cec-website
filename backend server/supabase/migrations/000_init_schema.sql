-- Create tables
CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    university_id TEXT,
    study_program TEXT,
    year_of_study INTEGER,
    bio TEXT,
    skills TEXT[],
    join_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    role TEXT DEFAULT 'member',
    profile_picture_url TEXT,
    status TEXT DEFAULT 'active',
    hashed_password TEXT NOT NULL
);

-- Create other tables similarly...