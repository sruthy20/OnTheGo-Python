from .models import db

def logininsert(model,**kwargs):
    
    val=model(**kwargs)
    db.session.add(val)
    code_commit()


def signupinsert(model,**kwargs):
    val=model(**kwargs)
    db.session.add(val)
    code_commit()

def code_commit():
 db.session.commit()


