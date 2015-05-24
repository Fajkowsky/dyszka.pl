from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config')

db = SQLAlchemy(app)
from models import *

api = Api(app)
from resources import main
api.add_resource(main.Main, '/')
