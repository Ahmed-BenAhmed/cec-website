CREATE TABLE IF NOT EXISTS members (
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


CREATE TABLE IF NOT EXISTS projects (
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

CREATE TABLE IF NOT EXISTS events (
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


CREATE TABLE IF NOT EXISTS project_members (
                                               project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
                                               member_id INTEGER REFERENCES members(id) ON DELETE CASCADE,
                                               role VARCHAR(50) NOT NULL,
                                               contribution TEXT,
                                               PRIMARY KEY (project_id, member_id)
);
CREATE TABLE IF NOT EXISTS events (
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


CREATE TABLE IF NOT EXISTS event_registrations (
                                                   id SERIAL PRIMARY KEY,
                                                   event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
                                                   member_id INTEGER REFERENCES members(id) ON DELETE CASCADE,
                                                   registration_date TIMESTAMP DEFAULT NOW(),
                                                   attendance_status VARCHAR(20) DEFAULT 'registered'
);

CREATE TABLE IF NOT EXISTS blog_posts (
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