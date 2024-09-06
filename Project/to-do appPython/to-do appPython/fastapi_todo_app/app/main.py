from fastapi import FastAPI
from app.controllers import todo_controller
from app.config import init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()
 
app.include_router(todo_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todos")
def get_todos():
    # Your code here
    pass

@app.post("/todos")
def create_todo():
    # Your code here
    pass

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    # Your code here
    pass
