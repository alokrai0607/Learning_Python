#Imports the declarative_base function from SQLAlchemy's ext.declarative module.
from sqlalchemy.ext.declarative import declarative_base

#for Imports the sessionmaker function from SQLAlchemy's ORM module.
from sqlalchemy.orm import sessionmaker

# Imports the create_engine function from SQLAlchemy.
#  create_engine manages the connections to the database and executes SQL statements.
from sqlalchemy import create_engine

#provides a way to interact with the operating system, including accessing 
#environment variables, file paths, and other system-related functions.
import os

#url
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:0303@localhost/todo")

#logging of all SQL statements emitted to the database-->(echo=True)
engine = create_engine(DATABASE_URL, echo=True)
#sessionmaker() returns a new session class bound to the database engine.

# changes are not committed automatically; 

#prevents the session from automatically flushing pending changes to the 
#database before query execution.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#declarative_base() is a factory function that constructs a base class for 
#declarative class definitions (ORM models).
Base = declarative_base()

# Defines a function to initialize the database.
# You can call init_db() to create all tables defined by your ORM models.
def init_db():
    Base.metadata.create_all(bind=engine)
