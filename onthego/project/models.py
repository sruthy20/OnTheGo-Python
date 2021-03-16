import flask_sqlalchemy
db=flask_sqlalchemy.SQLAlchemy()

class User(db.Model):
    __tablename__='User'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    password=db.Column(db.String(20))

class Admin(db.Model):
    __tablename__='Admin'
    AdminId=db.Column(db.Integer,primary_key=True)
    UserID=db.Column(db.Integer,db.ForeignKey(User.id))

