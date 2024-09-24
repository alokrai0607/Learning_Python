from sqlalchemy import Column, Integer, String
from ..config import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100))
    user_age = Column(Integer)
    user_gender = Column(String(10))

    def __repr__(self):
        return f"<User(user_id={self.user_id}, user_name='{self.user_name}', user_age={self.user_age}, user_gender='{self.user_gender}')>"
