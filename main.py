# import 
from fastapi import FastAPI


# instance
app = FastAPI()

# decorator amd ("/") is path or route 
@app.get("/")
def index():
    return {"message": "Hello, World!"}
    # function for which u can give any name 

@app.get("/blog")
def hlw(limit , published : bool):
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
def comments(id: int):
    return {'data': {'1' , '2'}}