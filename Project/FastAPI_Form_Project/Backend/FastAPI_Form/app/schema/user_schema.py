from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    user_name: str
    user_age: int
    user_gender: str

class UserUpdateSchema(BaseModel):
    user_name: Optional[str] = None
    user_age: Optional[int] = None
    user_gender: Optional[str] = None

    class Config:
        orm_mode = True
