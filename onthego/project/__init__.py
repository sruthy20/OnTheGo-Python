from flask import Flask
import flask_sqlalchemy
from  .models import db
from .. import onthegoconfig

def app_create():
    flask_app=Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI']=onthegoconfig.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()    # push the context with our newly created app
    db.init_app(flask_app)       # link our db to the Flask app 
    db.create_all()             # create tables if not already created
    return flask_app