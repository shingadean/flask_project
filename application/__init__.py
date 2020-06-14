from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'any secret string'

db = MongoEngine()
db.init_app(app)
from application import routes