"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():

    return render_template('homepage.html')

@app.route('/movies')
def view_movies():
    """View all movies"""

    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user"""

    username = request.form['email']
    password = request.form['password']

    if username in users.email:
        redirect('homepage.html')
    else:
        username = username
        password = password

    return render_template('homepage.html', username=username, password=password)

@app.route('/users')
def view_users():

    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show user profile page"""

    user = crud.get_user_profile(user_id)

    return render_template('user_details.html', user=user)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
