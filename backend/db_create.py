from app import db
from models.user import User
from utils.database import get_or_create

def generate_data():
    user = get_or_create(
        User,
        email="admin@dyszka.pl",
        username="admin",
        password="a",
        active=1
    )


db.create_all()
generate_data()
