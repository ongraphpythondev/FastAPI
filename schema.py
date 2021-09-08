"""
This is the schema or the json content field, we need from user to perform different operations.
"""


from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

