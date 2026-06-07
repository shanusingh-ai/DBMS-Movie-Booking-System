# python -m flask --app app.py run --debug

from datetime import date, time, timedelta

from flask import Flask
from flask_login import LoginManager
from flask_wtf import CSRFProtect

from config import Config
from models import Admin, Booking, Movie, Show, Theater, User, db
from routes import register_routes


login_manager = LoginManager()
csrf = CSRFProtect()


def create_app():
    """Create and configure the Flask application."""

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = "login"
    login_manager.login_message_category = "warning"

    @login_manager.user_loader
    def load_user(user_id):
        """Load either a customer or admin from the Flask-Login session id."""

        try:
            auth_type, raw_id = user_id.split(":", 1)
            model = Admin if auth_type == "admin" else User
            return db.session.get(model, int(raw_id))
        except (ValueError, TypeError):
            return None

    @app.template_filter("currency")
    def currency(value):
        return f"Rs. {float(value):,.2f}"

    @app.template_filter("show_date")
    def show_date(value):
        return value.strftime("%d %b %Y") if value else ""

    @app.template_filter("show_time")
    def show_time(value):
        return value.strftime("%I:%M %p") if value else ""

    register_routes(app)
    register_cli(app)
    return app


def register_cli(app):
    """Useful developer commands for database setup and demo data."""

    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        print("Database tables created.")

    @app.cli.command("seed-demo")
    def seed_demo():
        db.create_all()

        if not Admin.query.filter_by(email="admin@moviebook.local").first():
            admin = Admin(name="Admin", email="admin@moviebook.local")
            admin.set_password("Admin@123")
            db.session.add(admin)

        if not User.query.filter_by(email="user@moviebook.local").first():
            user = User(name="Demo User", email="user@moviebook.local", phone="9876543210")
            user.set_password("User@123")
            db.session.add(user)

        movies = [
            Movie(
                title="The Dark Knight",
                genre="Action, Crime, Drama",
                release_year="2008",
                language="English",
                duration="152 min",
                rating=9.0,
                plot="Batman faces a criminal mastermind whose chaos tests Gotham and its heroes.",
                poster_url="https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
                tmdb_id=155,
            ),
            Movie(
                title="Inception",
                genre="Action, Sci-Fi, Thriller",
                release_year="2010",
                language="English",
                duration="148 min",
                rating=8.8,
                plot="A skilled thief enters dreams to steal secrets and attempts one impossible job.",
                poster_url="https://image.tmdb.org/t/p/w500/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg",
                tmdb_id=27205,
            ),
            Movie(
                title="Interstellar",
                genre="Adventure, Drama, Sci-Fi",
                release_year="2014",
                language="English",
                duration="169 min",
                rating=8.7,
                plot="Explorers travel through a wormhole to find humanity a future among the stars.",
                poster_url="https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
                tmdb_id=157336,
            ),
            Movie(
                title="Jawan",
                genre="Action, Thriller",
                release_year="2023",
                language="Hindi",
                duration="169 min",
                rating=7.0,
                plot="A vigilante's mission grows into a fight against corruption and injustice.",
                poster_url="https://image.tmdb.org/t/p/w500/jFt1gS4BGHlK8xt76Y81Alp4dbt.jpg",
                tmdb_id=872906,
            ),
        ]

        for movie in movies:
            existing = Movie.query.filter_by(title=movie.title).first()
            if not existing:
                db.session.add(movie)

        theaters = [
            Theater(
                name="CinePulse Central",
                city="Hyderabad",
                address="Road No. 12, Banjara Hills",
            ),
            Theater(
                name="Vista IMAX",
                city="Hyderabad",
                address="Hi-Tech City Main Road",
            ),
            Theater(
                name="Metro Grand Screens",
                city="Mumbai",
                address="Lower Parel, Mumbai",
            ),
        ]

        for theater in theaters:
            if not Theater.query.filter_by(name=theater.name, city=theater.city).first():
                db.session.add(theater)

        db.session.commit()

        if Show.query.count() == 0:
            all_movies = Movie.query.limit(4).all()
            all_theaters = Theater.query.limit(3).all()
            times = ["10:30", "14:15", "18:45", "22:00"]
            for day_offset in range(1, 5):
                for movie_index, movie in enumerate(all_movies):
                    theater = all_theaters[movie_index % len(all_theaters)]
                    hour, minute = map(int, times[(movie_index + day_offset) % len(times)].split(":"))
                    show = Show(
                        movie_id=movie.id,
                        theater_id=theater.id,
                        show_date=date.today() + timedelta(days=day_offset),
                        show_time=time(hour, minute),
                        price=180 + (movie_index * 25),
                    )
                    db.session.add(show)

        db.session.commit()
        print("Demo data inserted.")


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)