
-- Insert projects data
INSERT INTO projects (title, description, cover_image_url, start_date, status, tags)
VALUES
    ('Weather App', 'A web application providing real-time weather updates and forecasts. Users can search for cities to view temperature, conditions, and hourly predictions.', 'public/images/projects/weather.jpg', NOW(), 'active', ARRAY['web', 'weather']),
    ('CityGuide+', 'A web application for discovering and navigating popular cities. Features city information and QR code integration for enhanced exploration.', 'public/images/projects/tourist.jpg', NOW(), 'active', ARRAY['web', 'tourism']),
    ('Palestine Chronicle', 'A news portal dedicated to events, history, and information related to Palestine. Offers categorized news for easy browsing.', 'public/images/projects/palestine.jpg', NOW(), 'active', ARRAY['web', 'news']),
    ('Stay.Healthy Platform', 'A web application promoting a balanced lifestyle by helping users track health metrics like BMI and BMR, and offering guidance on well-being.', 'public/images/projects/healthy.jpg', NOW(), 'active', ARRAY['web', 'health']),
    ('BookWise Hub', 'A web platform for personal development book enthusiasts. Allows users to discover books, manage reading lists, and access summaries to boost their potential.', 'public/images/projects/books.jpg', NOW(), 'active', ARRAY['web', 'books']);

-- Insert events data
INSERT INTO events (title, description, cover_image_url, event_date, start_time, end_time, location, event_link, registration_required, status)
VALUES
    ('Hackathons: Where It All Began', 'Exploring the origins and impact of hackathons with industry experts.', 'public/images/events/pod.jpg', '2024-12-27', '2024-12-27 14:00:00', '2024-12-27 16:00:00', 'Online', '#', FALSE, 'upcoming'),
    ('From Idea to Product', 'A workshop detailing the journey from a concept to a market-ready product.', 'public/images/events/id-to-pd.png', '2025-04-30', '2025-04-30 10:00:00', '2025-04-30 12:00:00', 'Google Meet', '#', FALSE, 'upcoming'),
    ('Geeksblabla On Campus', 'An engaging on-campus session in collaboration with Geeksblabla.', 'public/images/events/geeks.png', '2025-02-26', '2025-02-26 09:00:00', '2025-02-26 11:00:00', 'ENSA Berrechid', '#', FALSE, 'upcoming'),
    ('Unlock the Power of Data and AI', 'An introductory session to the fascinating worlds of Data and Artificial Intelligence.', 'public/images/events/ai-data.png', '2024-12-18', '2024-12-18 15:00:00', '2024-12-18 17:00:00', 'Room D7, ENSA', '#', FALSE, 'upcoming');
