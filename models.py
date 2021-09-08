"""
This is the Table's file means it contains the models or table for a particular database.
There is a table having some columns like
            id, title, body and datetime field.
"""




from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from database_connection import Base


class Blog(Base):

    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    date_and_time = Column(DateTime, default=datetime.now())
