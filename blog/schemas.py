from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

# since we are inheriting from Blog so we will have title and body here also
class ShowBlog(Blog):
    class Config():   # to tell Pydantic that this model is compatible with ORM objects
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str 

class ShowUser(BaseModel):  
    name: str
    email: str
    class Config():   # to tell Pydantic that this model is compatible with ORM objects
        from_attributes = True
