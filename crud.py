from sqlalchemy.orm import Session
import models, schemas

def get_user_by_login(db: Session, user_login: int)->Session.query:
    return db.query(models.User).filter(models.User.login == user_login).first()

def get_user_by_fname(db: Session, user_fname: str)->Session.query:
    return db.query(models.User).filter(models.User.user_fname == user_fname).all()

def get_all_users(db: Session, skip: int = 0, limit: int = 100)->Session.query:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate)->models.User:
    new_user = models.User(login=user.login, 
                            user_fname=user.user_fname,
                            user_sname=user.user_sname,
                            password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


