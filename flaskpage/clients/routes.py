from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flaskpage.clients.forms import ClientForm,LoginForm,UpdateAccountForm
from flaskpage.clients.models import Client
from flaskpage import app, bcrypt
from datetime import datetime,time
from PIL import Image
import secrets
import os

client = Blueprint('client', __name__)


@client.route('/client', methods=['GET', 'POST'])
def client_signup():
    if session.get("name"):
        return redirect(url_for('home'))
    form=ClientForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        date_cre=datetime.utcnow()
        cli=Client(name=form.name.data, 
                            email=form.email.data,
                            username=form.username.data, 
                            phone_number=form.phone_number.data,
                            password=hashed_password,
                            date_created=date_cre).save()
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('client.html',template_folder='templates',form=form)

@client.route('/client/login', methods=['GET', 'POST'])
def client_login():
    if session.get("name"):
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        client=Client.objects(username=form.username.data).first()
        if client:
            password_client = client['password']
            if password_client and bcrypt.check_password_hash(password_client, form.password.data):
                session['name'] = form.username.data
                session['type'] = 'client'
                flash('You have been logged in!', 'success')
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
                return redirect(url_for('client.client_login'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            return redirect(url_for('client.client_login'))
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

@client.route('/client/accountdetails', methods=['GET', 'POST'])
def client_accountdetails():
    form=UpdateAccountForm()
    user=Client.objects(username=session.get("name")).first()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            user['image_file'] = picture_file
        user['username'] = form.username.data
        user['phone_number'] = form.phone_number.data
        user['name'] = form.name.data
        user['email'] = form.email.data
        Client.objects(username=session.get("name")).update(name=user['name'],
                                                            username=user['username'],
                                                            email=user['email'],
                                                            image_file=user['image_file'],
                                                            phone_number=user['phone_number'])
        session['name'] = user['username']
        flash('Your account has been updated!', 'success')
        return redirect(url_for('client.client_accountdetails'))
            
    elif request.method == 'GET':
        form.name.data = user['name']
        form.username.data = user['username']
        form.email.data = user['email']
        form.phone_number.data = user['phone_number']
    image_file = url_for('static', filename='profile_pics/' + user['image_file'])
    return render_template('client_accountdetails.html',
                           template_folder='templates',
                           name=user['name'],
                           username=user['username'],
                           email=user['email'],
                           image_file=image_file,
                           form=form)
