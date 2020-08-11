"""CRUD operations. Utility functions for creating data"""

from model import db, User, Movie, Rating, connect_to_db


# Functions start here!

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """return all users"""

    return User.query.all()

def get_user_profile(user_id):
    """get user profile with passed id"""

    return User.query.filter_by(user_id = user_id).one()

def get_user_by_email(email):
    """takes in email and returns user if exists, otherwise returns none"""

    return User.query.filter_by(email = email).first()

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """return all movies"""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """return movie with passed movie_id"""

    return Movie.query.filter_by(movie_id = movie_id).one()


def create_rating(user, movie, score):
    """Create and return a new rating"""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)