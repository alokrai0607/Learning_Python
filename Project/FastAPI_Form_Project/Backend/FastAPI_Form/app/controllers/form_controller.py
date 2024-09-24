from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config import SessionLocal
from ..services.form_service import UserService
from ..schema.user_schema import UserSchema, UserUpdateSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)

@router.get("/users/")
def get_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()

@router.get("/users/{user_id}/")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}/")
def update_user_by_id(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    service = UserService(db)
    updated_user = service.update_user_by_id(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.patch("/users/{user_id}/")
def patch_user_by_id(user_id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):
    service = UserService(db)
    existing_user = service.get_user_by_id(user_id)
    
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = service.patch_user_by_id(user_id, user)
    return updated_user

@router.delete("/users/{user_id}/")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    success = service.delete_user_by_id(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
