-- 👤 Users
INSERT INTO pawsitting_user (id, username, password, first_name, last_name, email, address, is_superuser, is_staff, is_active, date_joined)
VALUES
(2, 'alice', '', 'Alice', 'Wong', 'alice@example.com', 'Bangkok', false, false, true, CURRENT_TIMESTAMP),
(3, 'bob', '', 'Bob', 'Smith', 'bob@example.com', 'Chiang Mai', false, false, true, CURRENT_TIMESTAMP),
(4, 'carol', '', 'Carol', 'Lee', 'carol@example.com', 'Phuket', false, false, true, CURRENT_TIMESTAMP),
(5, 'dave', '', 'Dave', 'Chan', 'dave@example.com', 'Khon Kaen', false, false, true, CURRENT_TIMESTAMP),
(6, 'eve', '', 'Eve', 'Nguyen', 'eve@example.com', 'Rayong', false, false, true, CURRENT_TIMESTAMP),
(7, 'frank', '', 'Frank', 'Kim', 'frank@example.com', 'Bangkok', false, false, true, CURRENT_TIMESTAMP),
(8, 'grace', '', 'Grace', 'Tan', 'grace@example.com', 'Chiang Rai', false, false, true, CURRENT_TIMESTAMP),
(9, 'heidi', '', 'Heidi', 'Lim', 'heidi@example.com', 'Nakhon Pathom', false, false, true, CURRENT_TIMESTAMP),
(10, 'ivan', '', 'Ivan', 'Tran', 'ivan@example.com', 'Udon Thani', false, false, true, CURRENT_TIMESTAMP),
(11, 'judy', '', 'Judy', 'Ho', 'judy@example.com', 'Surat Thani', false, false, true, CURRENT_TIMESTAMP);

-- 🐾 Services
INSERT INTO pawsitting_service (id, name, price, description)
VALUES
(2, 'Dog Walking', 300.00, '30-minute walk around the neighborhood'),
(3, 'Pet Sitting', 500.00, 'Full-day pet sitting at your home'),
(4, 'Grooming', 700.00, 'Bath and grooming service');

-- 📅 Bookings
INSERT INTO pawsitting_booking (id, customer_id, sitter_id, service_id, start_date, end_date, status)
VALUES
(1, 2, 3, 2, '2025-10-05', '2025-10-05', 'Pending'),
(2, 4, 5, 3, '2025-10-06', '2025-10-06', 'Confirm'),
(3, 6, 7, 4, '2025-10-07', '2025-10-07', 'Completed'),
(4, 8, 9, 2, '2025-10-08', '2025-10-08', 'Pending'),
(5, 10, 11, 3, '2025-10-09', '2025-10-09', 'Confirm'),
(6, 3, 2, 4, '2025-10-10', '2025-10-10', 'Completed'),
(7, 5, 4, 2, '2025-10-11', '2025-10-11', 'Pending'),
(8, 7, 6, 3, '2025-10-12', '2025-10-12', 'Confirm'),
(9, 9, 8, 4, '2025-10-13', '2025-10-13', 'Completed'),
(10, 11, 10, 2, '2025-10-14', '2025-10-14', 'Pending');