from .models import User, db, File


def add_user(user:User)->None:
    db.session.add(user)
    db.session.commit()

def delete_user(user:User)->None:
    db.session.delete(user)
    db.session.commit()

def get_all_users()->db.Query:
    return User.query.all()

def add_file(file:File)->None:
    db.session.add(file)
    db.session.commit()