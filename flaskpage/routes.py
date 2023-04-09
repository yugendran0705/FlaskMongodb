from flask import render_template, flash, redirect, url_for,session
from flask_login import current_user, login_user, logout_user, login_required
from flaskpage import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():  
    return render_template('home.html',template_folder='templates')


@app.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    return render_template('aboutus.html',template_folder='templates')

@app.route('/logout')
def logout():
    session.pop('name',None)
    flash('Logged out Successfully','success')
    return redirect(url_for('home'))

@app.route('/login')
def login():
    if session.get("name"):
        return redirect(url_for('home'))
    return render_template('loginstart.html',template_folder='templates')
