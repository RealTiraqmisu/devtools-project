-- Insert Users
INSERT INTO pawsitting_user (id, username, first_name, last_name, email)
VALUES 
(1, 'alice123', 'Alice', 'Wong', 'alice@example.com'),
(2, 'bob456', 'Bob', 'Smith', 'bob@example.com'),
(3, 'carol789', 'Carol', 'Tanaka', 'carol@example.com');

-- Insert Services
INSERT INTO pawsitting_service (id, name, description)
VALUES 
(1, 'Dog Walking', 'Daily dog walking service'),
(2, 'Pet Sitting', 'Overnight pet sitting at your home');

-- Insert Bookings
INSERT INTO pawsitting_booking (id, customer_id, sitter_id, service_id, start_date, end_date, status)
VALUES 
(1, 1, 2, 1, '2025-10-01', '2025-10-05', 'Pending'),
(2, 3, 2, 2, '2025-10-10', '2025-10-12', 'Confirm');

-- Insert Sitter Profiles
INSERT INTO pawsitting_sitterprofile (id, user_id, bio, price, is_verified)
VALUES 
(1, 2, 'Experienced pet sitter with 5 years of experience.', 500.00, TRUE);

-- Insert Many-to-Many relationships for SitterProfile and Service
INSERT INTO pawsitting_sitterprofile_service (sitterprofile_id, service_id)
VALUES 
(1, 1),
(1, 2);

-- Insert Reviews
INSERT INTO pawsitting_review (id, booking_id, rating, created_at)
VALUES 
(1, 2, 5, '2025-10-13 10:00:00');