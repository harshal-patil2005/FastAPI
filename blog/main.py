from fastapi import Depends, FastAPI
from blog.schemas import Blog
from blog import models, database
from sqlalchemy.orm import Session


app = FastAPI()

# Create tables automatically on startup
models.Base.metadata.create_all(bind=database.engine)

@app.get("/users/")
def read_users(db: Session = Depends(database.get_db)):
    users = db.query(models.Blog).all()
    return users


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"Blog titled '{blog.title}' with body '{blog.body}' has been created."}