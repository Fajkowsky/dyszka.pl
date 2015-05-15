from . import db


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(40), nullable=False)
    short_desc = db.Column(db.Strin(100))
    long_desc = db.Column(db.Text)