-- Insert sample members
INSERT INTO members (first_name, last_name, email, phone, university_id, study_program, year_of_study, bio, skills, role, hashed_password)
VALUES 
('John', 'Doe', 'john@cec.club', '123456789', 'STD001', 'Computer Science', 3, 'Tech enthusiast', ARRAY['Python', 'JavaScript'], 'admin', 'hashed_password'),
('Jane', 'Smith', 'jane@cec.club', '987654321', 'STD002', 'Engineering', 2, 'Web developer', ARRAY['React', 'Node.js'], 'lead', 'hashed_password');

-- Insert sample projects
INSERT INTO projects (title, description, start_date, status, tags)
VALUES
('Website Redesign', 'Redesign the club website', NOW(), 'in-progress', ARRAY['HTML', 'CSS', 'JavaScript']),
('AI Workshop', 'Organize AI workshop for members', NOW(), 'planning', ARRAY['Python', 'Machine Learning']);