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

def create_rating(user, movie, score):
                        # instance of movie, instance of user
                        # movie 1, user1
    """Create and return a new movie."""
    rat = Rating(user=user, movie=movie, score=score)

    db.session.add(rat)
    db.session.commit()
    
    return rat

if __name__ == '__main__':
    from server import app
    connect_to_db(app)