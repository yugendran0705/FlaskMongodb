from flask import Flask
from flask_bcrypt import Bcrypt
import os
from flask_mongoengine import MongoEngine
from flask_session import Session
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']="SECRET_KEY"
app.config['MONGODB_SETTINGS'] = {
    'db': os.getenv("MONGO_DB"),
    'host': os.getenv("MONGO_HOST"),
}
db = MongoEngine(app)
bcrypt=Bcrypt(app)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

from flaskpage.clients.routes import client
from flaskpage.developers.routes import developer

app.register_blueprint(client)
app.register_blueprint(developer)

from flaskpage import routes
