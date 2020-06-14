import flask
from application import db

class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(maxlength=510)
    last_name = db.StringField(maxlength=50)
    email = db.StringField(maxlength=50)
    password = db.StringField(maxlength=50)

class Course(db.Document):
    user_id = db.StringField( max_length=10, unique=True)
    title = db.StringField(maxlength=100)
    description = db.StringField(maxlenght=250)
    credits = db.IntField()
    term = db.StringField(maxlenght=25)

class Enrollment(db.Document):
    user_id = db.IntField()
    course_id = db.StringField( max_length=10 )
