#Imports the FastAPI class, which is used to create an instance of
#the FastAPI application.
from fastapi import FastAPI
#Imports the todo_controller module from the app.controllers
from app.controllers import todo_controller
#Imports the init_db() function from the app.config module.
#This function is used to initialize the database (e.g., creating tables 
#and setting up connections) when the application starts.
from app.config import init_db

# useful when your frontend and backend are hosted on different servers.
from fastapi.middleware.cors import CORSMiddleware

# Imports FileResponse, a FastAPI utility to send files as responses
from fastapi.responses import FileResponse

#Creates an instance of the FastAPI application, app, which is the core object 
#that handles incoming HTTP requests and routing them to appropriate endpoints.
app = FastAPI()

# A small icon displayed in the top of the browser tab
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("path_to_favicon/favicon.ico")

# triggers the startup_event() function when the application starts. 
# This function calls init_db() to initialize the database 
# (e.g., create tables if they don't exist).
@app.on_event("startup")
def startup_event():
    init_db()
 
 #Includes the todo_controller router in the main application.
 #FastAPI app, allowing the app to serve those routes.
app.include_router(todo_controller.router)

#Adds the CORS middleware to handle cross-origin requests, 
#allowing the backend to accept requests from different origins.
app.add_middleware(
    #Cross-Origin Resource Sharing
    CORSMiddleware,
    allow_credentials=True, #allows cookies and authentication to be sent across domains.
    allow_origins=["*"],  # Allow all origins for development; adjust for production
    allow_methods=["*"],#allows all HTTP methods (GET, POST, DELETE, etc.).
    allow_headers=["*"], # allows all headers (e.g., content-type, authorization).
)

#GET route at /todos to retrieve all todo items.
@app.get("/todos")
def get_todos():
    pass #means the function does nothing for now

# POST route at /todos to create a new todo item. 
@app.post("/todos")
def create_todo():
    pass #means the function does nothing for now

#DELETE route at /todos/{todo_id} to delete a todo item by its todo_id.
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    pass #means the function does nothing for now
