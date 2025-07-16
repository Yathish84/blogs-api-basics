from pydantic import BaseModel

class Blog_Schema(BaseModel):
    title:str
    body:str