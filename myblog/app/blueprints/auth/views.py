from flask import request, redirect, url_for, render_template, flash
from app.blueprints.auth.models import User
from flask_login import login_user, logout_user, current_user
from app.blueprints.auth import bp as auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_email = request.form['email']
        form_password = request.form['password']

        user = User.query.filter_by(email=form_email).first()
        if user is None:
            return redirect(url_for('login'))
        login_user(user)
        flash('User successfuly logged in', 'success')
        return redirect(url_for('main.home'))
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'Post'])
def register():
    if request.method == 'POST':
        res= request.form
        if res['confirm_password'] == res['password']:
            u = User(first_name=res['first_name'], last_name=res['last_name'], password=res['password'])
            u.save()
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('User logged out successfully', 'info')
    return redirect(url_for('auth.login'))

@auth_bp('/follow')
def follow():
    flash('Sucessfully following!')
    return redirect(url_for('main.explore'))
    # u = User.query.get(current_user.id)
    # u.follow


    