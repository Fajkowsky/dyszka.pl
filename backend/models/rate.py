from . import db

user_type = (
    'seller',
    'buyer'
)


class Rate(db.Model):
    __tablename__ = 'rate'
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transaction.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    type = db.Column(db.Enum(*user_type))
    rate = db.Column(db.Integer)
    comment = db.Column(db.String)