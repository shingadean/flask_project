import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
import email_validator


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(maxlength=510)
    last_name = db.StringField(maxlength=50)
    email = db.StringField(maxlength=50, unique=True)
    password = db.StringField()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)


class Course(db.Document):
    courseID = db.StringField(max_length=10, unique=True)
    title = db.StringField(maxlength=100)
    description = db.StringField(maxlenght=250)
    credits = db.IntField()
    term = db.StringField(maxlenght=25)


class Enrollment(db.Document):
    user_id = db.IntField()
    courseID = db.StringField(max_length=10)
