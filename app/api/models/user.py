from pydantic import BaseModel, Field
from sqlalchemy import Column,Integer, String,DateTime
from sqlalchemy import func

from api.utils.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True),
    names = Column(String(50))
    email = Column(String(30))
    address = Column(String(40))
    mobile = Column(String(15))
    password = Column(String)
    created_at = Column(DateTime, default=func.now(),nullable=False)

    def __init__ (self, names, email, address, mobile, password):
        self.names = names
        self.email = email
        self.address = address
        self.mobile = mobile
        self.password = password
    



class UserSchema(BaseModel):
    names: str = Field(...,min_length = 3 ,maxlength= 50)
    email: str = Field(...,min_length = 3 ,maxlength= 40)
    address: str = Field(...,min_length = 3 ,maxlength=30)
    mobile: str = Field(...,min_length = 10 ,maxlength=15)
    password: str = Field(...,min_length = 4 ,maxlength=16)

class UserDB(UserSchema):
    id: int

    class Config:
        orm_mode = True
