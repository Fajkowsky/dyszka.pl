import os
BASE_DIR = os.path.realpath(os.path.join('..', os.path.dirname(__file__)))
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/develop.db'.format(BASE_DIR)
DEBUG = True