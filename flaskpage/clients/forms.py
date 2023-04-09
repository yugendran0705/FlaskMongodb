from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField,SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    username=StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()],)
    confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    ''' def validate_phone_number(self, phone_number):
        client =Client.objects(phone_number=phone_number).first()
        print(client)
        if client:
            raise ValidationError('That phone number is taken. Please choose a different one.')
            
    
    def validate_username(self, username):
        client =Client.objects(username=username).first()
        if client:
            raise ValidationError('That username is taken. Please choose a different one.')
        '''
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')  
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    name=StringField('Name', validators=[DataRequired(), Length(max=30)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    '''def validate_phone_number(self, phone_number):
        client=Client.objects(username=current_user.username).first()
        if phone_number.data != client['phone_number']:
            client=Client.objects(phone_number=phone_number).first()
            if client:
                raise ValidationError('That phone number is taken. Please choose a different one.')
        

    def validate_email(self, email):
        client=Client.objects(username=current_user.username).first()
        if email.data != client['email']:
            client=Client.objects(email=email).first()
            if client:
                raise ValidationError('That phone number is taken. Please choose a different one.')

    def validate_username(self, username):
        client=Client.objects(username=current_user.username).first()
        if username.data != client['username']:
            client=Client.objects(username=username).first()
            if client:
                raise ValidationError('That phone number is taken. Please choose a different one.')'''