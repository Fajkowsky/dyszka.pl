from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean, default=False)
    user_token = db.Column(db.String(120))