from . import db


class TransactionEvent(db.Model):
    __tablename__ = 'transaction_event'
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transaction.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event = db.Column(db.String(80), nullable=False)