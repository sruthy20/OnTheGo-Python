from . import app_create
from .models import User,Admin,db
import requests
import json

app=app_create()

@app.route("/")   ## Decorator method for routing
def landing():
    return 'Welcome to OnTheGo application'

@app.route("/login",methods=['POST']) 

def login():
    data=requests.get_json()
    name=data['name']
    password=data['password']

    user=User(name=name,password=password)
    
    db.session.add(user)
    db.session.commit()

@app.route("/signup",methods=['POST'])    
def UserSignIn():
    data=requests.get_json()
    name=data['name']
    email=data['email']
    password=data['password']
    user=User(name=name,email=email,password=password)
    
    db.session.add(user)
    db.session.commit()
    return json.dumps('Added')




if __name__=='__main__':
    app.run