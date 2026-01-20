# import 
from fastapi import FastAPI


# instance
app = FastAPI()

# decorator
@app.get("/")
def index():
    return {"message": "Hello, World!"}
    # function
