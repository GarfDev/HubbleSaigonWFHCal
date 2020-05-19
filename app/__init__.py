# Libraries
from os import getenv
import flask_praetorian
import flask_cors
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# INITIALIZE_APPLICATION
load_dotenv()
app = Flask(getenv("APP_NAME"))
app.config.from_pyfile('app/config/development.py')
db = SQLAlchemy(app)
guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()
api = Api(app)
###
from app.modules.users.model import User
###
db.create_all()
guard.init_app(app, User)
cors.init_app(app)