USE movie_booking_system;

INSERT INTO admins (id, name, email, password_hash, created_at) VALUES
(1, 'Admin', 'admin@moviebook.local', 'pbkdf2:sha256:1000000$adminseed$e9f06bad4f182faa804cf05de18d0b9f29a58be93d8c69e60f7428bcec1c5b18', NOW())
ON DUPLICATE KEY UPDATE name = VALUES(name);

INSERT INTO users (id, name, email, phone, password_hash, active, created_at) VALUES
(1, 'Demo User', 'user@moviebook.local', '9876543210', 'pbkdf2:sha256:1000000$userseed$64cdbd288fef550580c30a0c49ce65fdfcd2780fb5a264303a26536e61f68e7a', 1, NOW())
ON DUPLICATE KEY UPDATE name = VALUES(name), phone = VALUES(phone), active = VALUES(active);

INSERT INTO movies (id, tmdb_id, imdb_id, title, genre, release_year, language, duration, rating, plot, poster_url, created_at) VALUES
(1, 155, NULL, 'The Dark Knight', 'Action, Crime, Drama', '2008', 'English', '152 min', 9.0, 'Batman faces a criminal mastermind whose chaos tests Gotham and its heroes.', 'https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg', NOW()),
(2, 27205, NULL, 'Inception', 'Action, Sci-Fi, Thriller', '2010', 'English', '148 min', 8.8, 'A skilled thief enters dreams to steal secrets and attempts one impossible job.', 'https://image.tmdb.org/t/p/w500/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg', NOW()),
(3, 157336, NULL, 'Interstellar', 'Adventure, Drama, Sci-Fi', '2014', 'English', '169 min', 8.7, 'Explorers travel through a wormhole to find humanity a future among the stars.', 'https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg', NOW()),
(4, 872906, NULL, 'Jawan', 'Action, Thriller', '2023', 'Hindi', '169 min', 7.0, 'A vigilante mission grows into a fight against corruption and injustice.', 'https://image.tmdb.org/t/p/w500/jFt1gS4BGHlK8xt76Y81Alp4dbt.jpg', NOW())
ON DUPLICATE KEY UPDATE title = VALUES(title), genre = VALUES(genre), rating = VALUES(rating);

INSERT INTO theaters (id, name, city, address, rows_data, seats_per_row, created_at) VALUES
(1, 'CinePulse Central', 'Hyderabad', 'Road No. 12, Banjara Hills', 'A,B,C,D,E,F,G,H', 10, NOW()),
(2, 'Vista IMAX', 'Hyderabad', 'Hi-Tech City Main Road', 'A,B,C,D,E,F,G,H', 10, NOW()),
(3, 'Metro Grand Screens', 'Mumbai', 'Lower Parel, Mumbai', 'A,B,C,D,E,F,G,H', 10, NOW())
ON DUPLICATE KEY UPDATE name = VALUES(name), city = VALUES(city), address = VALUES(address);

INSERT INTO shows (id, movie_id, theater_id, show_date, show_time, price, status, created_at) VALUES
(1, 1, 1, DATE_ADD(CURDATE(), INTERVAL 1 DAY), '10:30:00', 220.00, 'Scheduled', NOW()),
(2, 2, 1, DATE_ADD(CURDATE(), INTERVAL 1 DAY), '18:45:00', 240.00, 'Scheduled', NOW()),
(3, 3, 2, DATE_ADD(CURDATE(), INTERVAL 2 DAY), '14:15:00', 260.00, 'Scheduled', NOW()),
(4, 4, 3, DATE_ADD(CURDATE(), INTERVAL 2 DAY), '20:00:00', 200.00, 'Scheduled', NOW()),
(5, 1, 2, DATE_ADD(CURDATE(), INTERVAL 3 DAY), '22:00:00', 280.00, 'Scheduled', NOW())
ON DUPLICATE KEY UPDATE price = VALUES(price), status = VALUES(status);

INSERT INTO bookings (id, booking_code, user_id, show_id, seat_count, total_amount, status, booked_at) VALUES
(1, 'MBDEMO1001', 1, 1, 2, 440.00, 'Confirmed', NOW())
ON DUPLICATE KEY UPDATE status = VALUES(status);

INSERT INTO booking_seats (booking_id, show_id, seat_number, price, created_at) VALUES
(1, 1, 'C5', 220.00, NOW()),
(1, 1, 'C6', 220.00, NOW())
ON DUPLICATE KEY UPDATE price = VALUES(price);