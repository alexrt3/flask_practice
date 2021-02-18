from app import db
from flask import render_template, request, redirect, url_for
from app.blueprints.auth.models import User
from app.blueprints.blog.models import Post
from flask_login import login_user, current_user, logout_user, login_required
from .import bp as main_bp


@main_bp.route('/')
def home():
    context = {
        'user': current_user,
        'posts': Post.query.order_by(Post.date_created.desc()).all()
    }
    return render_template('home.html', **context)

@main_bp.route('/profile')
def profile():
    return render_template('profile.html')

@main_bp.route('/explore')
@login_required
def explore():
    context = {
        'users': [user for user in User.query.all() if current_user.id != user.id]
    }
    print(current_user)
    return render_template('explore.html', **context)

