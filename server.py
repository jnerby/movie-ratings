"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
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
def get_movies():
    
    all_movies = crud.return_all_movies()
    
    return render_template('movies.html', all_movies=all_movies)

@app.route('/movies/<movie_id>')
def get_movie_details(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html',movie=movie)

@app.route('/users')
def get_users():

    users = crud.return_all_users()

    return render_template('users.html', users=users)

@app.route('/users/<user_id>')
def get_user_details(user_id):
    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user=user)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
