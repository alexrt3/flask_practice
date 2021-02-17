from app import db
from flask import render_template, request, redirect, url_for, current_app as app
from app.blueprints.auth.models import User
from app.models import Post
from flask_login import login_user, current_user, logout_user


@app.route('/')
def home():
    context = {
        'user': current_user,
        'posts': Post.query.order_by(Post.date_created.desc()).all()
    }
    return render_template('home.html', **context)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/explore')
def explore():
    context = {
        'users': User.query.all()
    }
    return render_template('explore.html', **context)

