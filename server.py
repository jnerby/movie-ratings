"""Server for movie ratings app."""
import re
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

@app.route('/users', methods=['POST'])
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')

    # check if user in db
    user = crud.get_user_by_email(email)
    if user != None:
        flash('Email already exists. Please try again')
    else:
        crud.create_user(email,password)
        flash('Registration successful!')

    return render_template('homepage.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user.password == password:
        flash('Logged in!')
        session['user_id'] = user.user_id
        return render_template('rate.html')
    
    else:
        flash('Incorrect password')
        return redirect('/')

@app.route('/rate', methods=['GET','POST'])
def rate_movie():
    
    if 'user_id' in session:
        user = crud.get_user_by_id(session['user_id'])
        movie = crud.get_movie_by_title(request.form.get('movie'))
        score = request.form.get('score')

        crud.create_rating(user, movie, score)
        flash('Rating added!')
        return redirect('/')
        
    else:
        return redirect('/')

@app.route('/users/<user_id>')
def get_user_details(user_id):
    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user=user)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
