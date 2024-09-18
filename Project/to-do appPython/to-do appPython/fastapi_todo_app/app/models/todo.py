#raw SQL queries.
# Imports necessary classes and types from SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
#importing the Base class from config module
#The Base class was created using SQLAlchemy's declarative_base() 
from app.config import Base

#CLASS nAME = TodoItem
# This model inherits from Base
#The TodoItem class is created to define the structure of the todo_items 
#table in your database
# Define the Table Structure:
# Mapping Between Database Rows and Python Objects:
class TodoItem(Base):
    __tablename__ = 'todo_items'
    #Is indexed (index=True) for faster lookups and searches based on id
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    is_completed = Column(Boolean , default=True)
