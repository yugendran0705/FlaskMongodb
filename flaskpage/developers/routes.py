from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flaskpage.developers.forms import DeveloperForm,LoginForm,UpdateAccountForm
from flaskpage import app, bcrypt
from flaskpage.developers.models import Developer
from datetime import datetime
from PIL import Image
import secrets
import os

developer = Blueprint('developer', __name__)


@developer.route('/developer', methods=['GET', 'POST'])
def developer_signup():
    if session.get("name"):
        return redirect(url_for('home')) 
    form=DeveloperForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        date_cre=datetime.utcnow()
        new_developer = Developer(name=form.name.data, 
                                  email=form.email.data, 
                                  username=form.username.data,
                                  phone_number=form.phone_number.data,
                                  domain=form.domain.data,
                                  github_link=form.github_link.data,
                                  linkedin_link=form.linkedin_link.data,
                                  experience=form.experience.data,
                                  password=hashed_password,
                                  date_created=date_cre).save()
        
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('developer.html',template_folder='templates', form=form)
        
@developer.route('/developer/login', methods=['GET', 'POST'])
def developer_login():
    if session.get("name"):
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        dev=Developer.objects(username=form.username.data).first()
        if dev:
            password_dev = dev['password']
            if password_dev and bcrypt.check_password_hash(password_dev, form.password.data):
                session['name'] = form.username.data
                session['type'] = 'developer'
                flash('You have been logged in!', 'success')
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
                return redirect(url_for('developer.developer_login'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            return redirect(url_for('developer.developer_login'))
    return render_template('login.html',template_folder='templates',form=form)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn,".jpg")
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@developer.route('/developer/accountdetails', methods=['GET', 'POST'])
def developer_accountdetails():
    form=UpdateAccountForm()
    user=Developer.objects(username=session.get("name")).first()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            user['image_file'] = picture_file
        user['name'] = form.name.data
        user['username'] = form.username.data
        user['email'] = form.email.data
        user['phone_number'] = form.phone_number.data
        user['domain'] = form.domain.data
        user['github_link'] = form.github_link.data
        user['linkedin_link'] = form.linkedin_link.data
        user['experience'] = form.experience.data
        Developer.objects(username=session.get("name")).update(name=user['name'],
                                                               username=user['username'],
                                                               email=user['email'],
                                                               phone_number=user['phone_number'],
                                                               domain=user['domain'],
                                                               github_link=user['github_link'],
                                                               linkedin_link=user['linkedin_link'],
                                                               experience=user['experience'],
                                                               image_file=user['image_file'])
        session['name'] = user['username']
        flash('Your account has been updated!', 'success')
        return redirect(url_for('developer.developer_accountdetails'))
    
    elif request.method == 'GET':
        form.name.data = user['name']
        form.username.data = user['username']
        form.email.data = user['email']
        form.phone_number.data = user['phone_number']
        form.domain.data = user['domain']
        form.github_link.data = user['github_link']
        form.linkedin_link.data = user['linkedin_link']
        form.experience.data = user['experience']
    image_file = url_for('static', filename='profile_pics/' + user['image_file'])
    return render_template('developer_accountdetails.html',
                            template_folder='templates',
                            name=user['name'],
                            username=user['username'],
                            email=user['email'],
                            image_file=image_file,
                            form=form)
