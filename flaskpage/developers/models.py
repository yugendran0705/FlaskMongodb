
from flaskpage import db
from datetime import datetime
from flask_mongoengine import Document

    
class Developer(db.Document):
    meta = {'collection': 'developers'}
    name=db.StringField(max_length=50)
    email=db.StringField(max_length=60)
    username=db.StringField(max_length=20)
    phone_number=db.StringField(max_length=20)
    domain=db.StringField(max_length=50)
    github_link=db.StringField(max_length=100)
    linkedin_link=db.StringField(max_length=100)
    experience=db.StringField(max_length=100)
    password=db.StringField(max_length=100)
    date_created=db.DateTimeField(default=datetime.utcnow())
    image_file = db.StringField(max_length=40,default='default.jpg')

    def __repr__(self):
        d={}
        d['name']=self.name
        d['email']=self.email
        d['username']=self.username
        d['phone_number']=self.phone_number
        d['password']=self.password
        d['domain']=self.domain
        d['github_link']=self.github_link
        d['linkedin_link']=self.linkedin_link
        d['experience']=self.experience
        d['date_created']=self.date_created
        d['image_file']=self.image_file
        return str(d)

    def get_id(self):
        return (self.username)
    
'''
class Post(Document):
    username=StringField(max_length=20,primary_key=True)
    title=StringField(max_length=100)
    date_posted=DateTimeField(default=datetime.utcnow)
    content=StringField(max_length=400)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
        '''