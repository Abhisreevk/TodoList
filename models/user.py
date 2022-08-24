from pydantic import BaseModel

class User(BaseModel):
    Title:str
    Sub_title:str
    Todo:str
    Category:str