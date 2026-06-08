# Online Movie Ticket Booking System

A complete Flask and MySQL movie ticket booking web application with customer authentication, admin management, API-backed movie search, seat selection, and booking history.

## Features

- Responsive dark UI built with Bootstrap, custom CSS, and JavaScript
- Movie cards, search, genre filters, details pages, and poster-first layout
- Customer signup/login with hashed passwords and Flask-Login sessions
- Admin login with movie, theater, show, booking, and user management
- MySQL schema with primary keys, foreign keys, and unique seat locking
- Seat picker that prevents double booking through a database constraint
- Flash messages, validation, loading animation, and mobile-friendly pages
- Optional TMDb or OMDb integration through environment variables

## Backend

The Flask app uses an app factory in `app.py`, routes in `routes.py`, models in `models.py`, and environment configuration in `config.py`. SQLAlchemy is used with a MySQL connection string, which keeps database access parameterized and avoids SQL injection from raw string queries.

## Frontend

Templates live in `templates/`, CSS in `static/css/style.css`, and JavaScript in `static/js/`. The UI uses Bootstrap 5 plus custom styling for movie cards, hover states, dashboards, and the seat map.

## Database

SQL files are in `database/`:

- `schema.sql` creates the MySQL database and tables.
- `dummy_data.sql` inserts demo users, movies, theaters, shows, and one sample booking.

Main tables:

- `users`
- `admins`
- `movies`
- `theaters`
- `shows`
- `bookings`
- `booking_seats`

`booking_seats` has a unique constraint on `(show_id, seat_number)`, so the same seat cannot be booked twice for the same show.

## Authentication

Passwords are hashed with Werkzeug. Flask-Login stores sessions for both user and admin accounts. Customer routes and admin routes use separate decorators, so a logged-in admin cannot accidentally book tickets as a customer account.

Demo accounts:

- User: `user@moviebook.local` / `User@123`
- Admin: `admin@moviebook.local` / `Admin@123`

## Booking System

Customers choose a movie, select a show, pick available seats, and confirm booking. The backend validates seat existence, quantity, availability, and duplicate selections before writing the booking.

## Setup

1. Create and activate a virtual environment.

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create the MySQL database.

```bash
mysql -u root -p < database/schema.sql
mysql -u root -p < database/dummy_data.sql
```

4. Configure environment variables.

```bash
copy .env.example .env
```

Update `DATABASE_URL` in `.env` with your MySQL username and password.

5. Run the application.

```bash
flask --app app.py run --debug
```

Open `http://127.0.0.1:5000`.

## Alternative Demo Seeding

You can also let Flask create tables and seed demo records:

```bash
flask --app app.py init-db
flask --app app.py seed-demo
```

## OMDb API

The app runs with local dummy data by default. To fetch movie data dynamically, add one of these keys to `.env`:

```bash
OMDB_API_KEY=your_omdb_key
```

## Project Structure

```text
.
├── app.py
├── config.py
├── models.py
├── routes.py
├── requirements.txt
├── README.md
├── database/
│   ├── schema.sql
│   └── dummy_data.sql
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── main.js
│   │   └── booking.js
│   └── images/
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── signup.html
    ├── movie_details.html
    ├── booking.html
    ├── confirmation.html
    ├── dashboard.html
    └── admin/
```
