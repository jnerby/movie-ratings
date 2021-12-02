"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def return_all_movies():
    """Return all movies from DB"""
    return Movie.query.all()

def return_all_users():
    """Return all users from DB"""
    return User.query.all()

def get_movie_by_id(movie_id):
    """Getting movie obj from id"""
    return Movie.query.get(movie_id)

def get_movie_by_title(title):
    """Getting movie obj from title"""
    return Movie.query.filter_by(title=title).first()

def get_user_by_id(user_id):
    """Getting user obj from id"""
    return User.query.get(user_id)

def create_rating(user, movie, score):
                        # instance of movie, instance of user
                        # movie 1, user1
    """Create and return a new movie."""
    rat = Rating(user=user, movie=movie, score=score)

    db.session.add(rat)
    db.session.commit()
    
    return rat

def get_user_by_email(email):
    """Getting user obj from id"""
    return User.query.filter_by(email=email).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)