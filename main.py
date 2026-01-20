# import 
from fastapi import FastAPI


# instance
app = FastAPI()

# decorator amd ("/") is path or route 
@app.get("/")
def index():
    return {"message": "Hello, World!"}
    # function for which u can give any name 


@app.get("/blog/{id}")
def show(id: int): 
    # id must be accepted by function in order to use it inside function 
    return {'data': id}