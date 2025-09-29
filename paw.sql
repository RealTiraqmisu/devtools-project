-- Users
INSERT INTO pawsitting_user (id, username, first_name, last_name, email, address)
VALUES 
(1, 'alice123', 'Alice', 'Wong', 'alice@example.com', '123 ถนนสุขุมวิท กรุงเทพฯ'),
(2, 'bob456', 'Bob', 'Smith', 'bob@example.com', '456 ถนนพระราม 9 กรุงเทพฯ'),
(3, 'carol789', 'Carol', 'Tanaka', 'carol@example.com', '789 ถนนลาดกระบัง กรุงเทพฯ');

-- Services
INSERT INTO pawsitting_service (id, name, price, description)
VALUES 
(1, 'Dog Walking', 300.00, 'บริการพาสุนัขเดินเล่นวันละ 1 ชั่วโมง'),
(2, 'Pet Sitting', 1200.00, 'ดูแลสัตว์เลี้ยงที่บ้านลูกค้าแบบค้างคืน');

-- Bookings
INSERT INTO pawsitting_booking (id, customer_id, sitter_id, service_id, start_date, end_date, status)
VALUES 
(1, 1, 2, 1, '2025-10-01', '2025-10-05', 'Pending'),
(2, 3, 2, 2, '2025-10-10', '2025-10-12', 'Confirm');

-- Sitter Profile
INSERT INTO pawsitting_sitterprofile (id, user_id, bio, is_verified, cert_image)
VALUES 
(1, 2, 'รักสัตว์มาก มีประสบการณ์ดูแลสุนัขและแมวมากกว่า 5 ปี', TRUE, 'image/certificate_bob.jpg');

-- Many-to-Many: SitterProfile ↔ Service
INSERT INTO pawsitting_sitterprofile_service (sitterprofile_id, service_id)
VALUES 
(1, 1),
(1, 2);

-- Review
INSERT INTO pawsitting_review (id, booking_id, rating, created_at)
VALUES 
(1, 2, 5, '2025-10-13 10:00:00');