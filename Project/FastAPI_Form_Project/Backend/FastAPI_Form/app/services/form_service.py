from sqlalchemy.orm import Session
from ..models.user import User
from ..repositories.form_repository import UserRepository
from ..schema.user_schema import UserSchema, UserUpdateSchema

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, user_data: UserSchema):
        user = User(**user_data.dict())
        return self.repository.create_user(user)

    def get_all_users(self):
        return self.repository.get_all_users()

    def get_user_by_id(self, user_id: int):
        return self.repository.get_user(user_id)

    def update_user_by_id(self, user_id: int, user_data: UserSchema):
        user = self.repository.get_user(user_id)
        if user:
            for key, value in user_data.dict().items():
                setattr(user, key, value)
            return self.repository.update_user(user)
        return None

    def patch_user_by_id(self, user_id: int, user_data: UserUpdateSchema):
        user = self.repository.get_user(user_id)
        if user:
            for key, value in user_data.dict(exclude_unset=True).items():
                setattr(user, key, value)
            return self.repository.update_user(user)
        return None

    def delete_user_by_id(self, user_id: int):
        return self.repository.delete_user(user_id)
