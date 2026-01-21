from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

# since we are inheriting from Blog so we will have title and body here also
class ShowBlog(Blog):
    class Config():   # to tell Pydantic that this model is compatible with ORM objects
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str   
