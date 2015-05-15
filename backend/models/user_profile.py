from . import db


class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    description = db.Column(db.Text)
    avatar = db.Column(db.Strig)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(120))

    user = db.relationship('User', backref='user_profile')