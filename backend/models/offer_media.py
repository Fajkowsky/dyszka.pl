from app import db


class OfferMedia(db.Model):
    __tablename__ = 'offer_media'
    id = db.Column(db.Integer, primary_key=True)
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'))
    url = db.Column(db.String(), nullable=False)