from app import db
from utils.database import get_or_create
from fixtures import fixtures

def generate_data():
    for item in fixtures:
        for data in item['data']:
            get_or_create(item['model'], **data)

db.create_all()
generate_data()
