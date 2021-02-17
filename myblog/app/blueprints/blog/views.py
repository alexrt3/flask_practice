from .import bp as blog_bp
from flask import request, flash, redirect, url_for
from app import db

@blog_bp.route('/post/create', methods=['POST'])
def create_post():
    if request.method == 'POST':
        try:
            data = request.form['status_update']
            p = Post(body=data)
            db.session.add(p)
            db.session.commit()
            flash('Post was created sucessfully', 'info')
        except:
            flash('Error: couldnt create the post. Try again.', 'danger')       
    return redirect(url_for('main.home'))
    