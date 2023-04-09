from flaskpage import db
from datetime import datetime
from flask_mongoengine import Document

class Client(db.Document):
    meta = {'collection': 'clients'}
    name=db.StringField(max_length=50)
    email=db.StringField(max_length=60)
    username=db.StringField(max_length=20)
    phone_number=db.StringField(max_length=20)
    password=db.StringField(max_length=100)
    date_created=db.DateTimeField(default=datetime.utcnow())
    image_file = db.StringField(max_length=40, default='default.jpg')

    def __repr__(self):
        d={"name":self.name,"email":self.email,"username":self.username,"phone_number":self.phone_number,"date_created":self.date_created,"image_file":self.image_file,"password":self.password}
        return str(d)

    def get_id(self):
        return (self.username)