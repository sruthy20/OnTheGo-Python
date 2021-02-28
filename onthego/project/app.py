from flask.wrappers import Response
from . import app_create
from . import sqlqueries
from .models import User,Admin,db
from flask import request
import json

app=app_create()

@app.route("/")   ## Decorator method for routing
def landing():
    return 'Welcome to OnTheGo application'

@app.route("/login",methods=['POST']) 

def login():
    data=request.get_json()
    name=data['name']
    password=data['password']

    sqlqueries.logininsert(User,name=name,password=password)
    return json.dumps("Added"), 200

@app.route("/signup",methods=['POST'])    
def UserSignIn():
    data=request.get_json()
    name=data['name']
    email=data['email']
    password=data['password']
    #user=User(name=name,email=email,password=password)
    sqlqueries.signupinsert(User,name=name,email=email,password=password)
    
    return json.dumps("User signe up completed, email is sent"), 200
    
    

@app.route("/login/admin",methods=['POST']) 

def login_admin():
    data=request.get_json()
    name=data['name']
    password=data['password']

    user=Admin(name=name,password=password)
    sqlqueries.logininsert(Admin,user)
    Response.status_code=200
    return Response



if __name__=='__main__':
    app.run