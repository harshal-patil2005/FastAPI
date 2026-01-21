# import 
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base


Base.metadata.create_all(bind=engine)

# instance
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# decorator amd ("/") is path or route 
@app.get("/")
def index():
    return {"message": "Hello, World!"}
    # function for which u can give any name 

@app.get("/blog")
def hlw(limit=10 , published : bool = True , sort: Optional[str] = None): 
    # http://127.0.0.1:8000/blog?limit=10&published=false url should be like this for this

    if published:
        return {'data': f'{limit} published blogs from the db'}
    else :
        return {'data': f'{limit} blogs from the db'}

@app.get("/blog/unpublished")
def show():
    # order matters 
    return {'data': 'all unpublished blog'}

@app.get("/blog/{id}")
def show(id: int): 
    # id must be accepted by function in order to use it inside function 
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id: int , limit = 10):
    # this limit will not be treated as path parameter 
    # because it is not defined in pat
    return {'data': {'1' , '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

# post is used to create data
# paydantic = request body
# request: Blog is request body defined by pydantic model
@app.post("/blog")
def create_blog(request: Blog):
    return request


# if __name__ == "__main__":      
#         import uvicorn
#         uvicorn.run(app, host="127.0.0.1", port=9000)


@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, user=user)
    return db_user