# The controller manages HTTP requests from clients, processes them, 
# and sends appropriate responses. 

#Usefull for partial Update .
from typing import Optional

#Allows you to create a modular router to handle a group of related endpoints.

#Depends: Used for dependency injection in FastAPI, allowing automatic injection
#of dependencies like the database session into the route functions.

#Used to raise HTTP exceptions with specific status codes and error messages
from fastapi import APIRouter, Depends, HTTPException

#Represents a database session provided by SQLAlchemy.
from sqlalchemy.orm import Session

#This imports the service layer 
from app.services.todo_service import TodoService

#This is the database session factory from config.py, used to interact with the database.
from app.config import SessionLocal

#Used for request body validation in FastAPI.
from pydantic import BaseModel

#This creates an API router for handling the /todos routes.
#we can register this router in our FastAPI app to group our
#routes logically.
router = APIRouter()

#request models :: These Pydantic models define the structure of request bodies 
#that the API expects for creating and updating todos.
class TodoCreate(BaseModel):
    title: str
    description: str

class TodoPartialUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

#Dependency Injection for the Database Session (get_db)
def get_db():
    #It creates a database session
    db = SessionLocal()
    try:
        yield db #Inject db session into routes
    finally:
        #session is closed after the request is processed
        db.close()

@router.get("/todos")
def get_todos(db: Session = Depends(get_db)):# db is used to access the database.
    return TodoService(db).get_all_todos()

@router.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = TodoService(db).get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return TodoService(db).create_new_todo(todo.title, todo.description)

@router.patch("/todos/{todo_id}")
def patch_todo(todo_id: int, todo: TodoPartialUpdate, db: Session = Depends(get_db)):
    existing_todo = TodoService(db).get_todo_by_id(todo_id)
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.title is not None:
        existing_todo.title = todo.title
    if todo.description is not None:
        existing_todo.description = todo.description
    if todo.is_completed is not None:
        existing_todo.is_completed = todo.is_completed
    return TodoService(db).update_existing_todo(todo_id, existing_todo.title, existing_todo.description, existing_todo.is_completed)

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return TodoService(db).delete_todo_by_id(todo_id)

@router.put("/todos/{todo_id}")
def put_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    existing_todo = TodoService(db).get_todo_by_id(todo_id)
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.title:
        existing_todo.title = todo.title
    if todo.description:
        existing_todo.description = todo.description
    if todo.is_completed:
        existing_todo.is_completed = todo.is_completed
    return TodoService(db).update_existing_todo(todo_id, existing_todo.title, existing_todo.description, existing_todo.is_completed)
