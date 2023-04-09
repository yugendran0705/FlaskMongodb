from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField,SelectField,PasswordField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskpage.developers.models import Developer
from flask_login import current_user,login_user,logout_user,login_required

class DeveloperForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    username=StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    phone_number = StringField('Phone Number',validators=[DataRequired()])
    domain = SelectField('Domain', choices=['Web Developer','Graphics Designer','Digital Marketing','Video Editing'], validators=[DataRequired()])
    github_link = StringField('Github Link', validators=[DataRequired()])
    linkedin_link = StringField('Linkedin Link', validators=[DataRequired()])
    experience = StringField('Experience', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired()])
    confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    '''def validate_phone_number(self, phone_number):
        dev = Developer.objects(phone_number=phone_number).first()
        if dev:
            raise ValidationError('That phone number is taken. Please choose a different one.')
            
    def validate_username(self, username):
        dev=Developer.objects(username=username).first()
        if dev:
            raise ValidationError('That username is taken. Please choose a different one.')'''

class UpdateAccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=30)])
    username = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    domain = SelectField('Domain', choices=['Web Developer','Graphics Designer','Digital Marketing','Video Editing'], validators=[DataRequired()])
    github_link = StringField('Github Link', validators=[DataRequired()])
    linkedin_link = StringField('Linkedin Link', validators=[DataRequired()])
    experience = StringField('Experience', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    '''def validate_phone_number(self, phone_number):
        dev=Developer.objects(username=current_user.username).first()
        if phone_number.data != dev['phone_number']:
            dev=Developer.objects(phone_number=phone_number.data).first()
            if dev:
                raise ValidationError('That phone number is taken. Please choose a different one.')
        

    def validate_email(self, email):
        dev=Developer.objects(username=current_user.username).first()
        if email.data != dev['email']:
            dev=Developer.objects(email=email).first()
            if dev:
                raise ValidationError('That phone number is taken. Please choose a different one.')
                
    def validate_username(self, username):
        dev=Developer.objects(username=current_user.username).first()
        if username.data != dev['username']:
            dev=Developer.objects(username=username).first()
            if dev:
                raise ValidationError('That phone number is taken. Please choose a different one.')'''
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')  
    submit = SubmitField('Login')