from pydantic import BaseModel



class UserBase(BaseModel):
    login: str
    user_fname: str
    user_sname: str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True
