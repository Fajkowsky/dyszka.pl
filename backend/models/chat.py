from app import db


class Chat(db.Model):
    __tablename__ = 'chat'
    id = db.Column(db.Integer, primary_key=True)
    first_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    second_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
