from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.wsgi import WSGIMiddleware
import crud, models, schemas
from database import SessionLocal, engine
from web.flask_main import app

models.Base.metadata.create_all(bind=engine)


fapp = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    
    finally:
        db.close()


@fapp.post("/users/create/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.get_user_by_login(db, user_login=user.login)

    if new_user:
        raise HTTPException(status_code=400, detail="Login is already taken by another user.")
    return crud.create_user(db=db, user=user)


@fapp.get("/users/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    return users


@fapp.get("/users/fname/{user_fname}", response_model=list[schemas.User])
def get_users_by_name(user_fname, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_user_by_fname(db=db, user_fname=user_fname)
    return users

@fapp.get("/users/{login}", response_model=schemas.User)
def get_certain_user(login, db: Session = Depends(get_db)):
    return crud.get_user_by_login(db, login)

fapp.mount("/", WSGIMiddleware(app))