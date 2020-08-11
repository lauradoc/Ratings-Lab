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


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user"""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)

    if user:
        flash('Email already exists. Please make an account with a different email')
        
    else:
        crud.create_user(email, password)
        flash('Your account was created successfully! You can now log in.')
    
    return redirect('/')


@app.route('/users/loggedin')
def logged_in():
    """Check to see if password matches and log user in"""

    email = request.args.get('email')
    password = request.args.get('password')
    user = crud.get_user_by_email(email)
    
    if password in user.password:
        flash('Logged in!')
        session['email'] = user.user_id

    else:
        flash('Log In failed. Try again.')

    return redirect('/')


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
