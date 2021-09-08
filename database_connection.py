"""
This python File is to make the Database connection to this project.
"""



from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This is the DATABASE URL variable means the name and path of the database.
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'


# This is the engine to run the database. This is same as the engine of Bike.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


# This is for creating a session for the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
