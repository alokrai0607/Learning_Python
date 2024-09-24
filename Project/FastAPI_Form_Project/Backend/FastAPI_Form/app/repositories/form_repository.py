from sqlalchemy.orm import Session
from ..models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.user_id == user_id).first()

    def get_all_users(self):
        return self.db.query(User).all()

    def update_user(self, user: User):
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id: int):
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False

