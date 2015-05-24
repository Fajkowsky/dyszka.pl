from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean, default=False)
    user_token = db.Column(db.String(120))

    profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('user_category.id'))

    profile = db.relationship('UserProfile')
    category = db.relationship('UserCategory')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.create_password(kwargs['password'])

    def create_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    avatar = db.Column(db.String)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(120))


class UserCategory(db.Model):
    __tablename__ = 'user_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
