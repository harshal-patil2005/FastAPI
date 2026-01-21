from fastapi import Depends, FastAPI
from blog import schemas
from blog import models, database
from sqlalchemy.orm import Session


app = FastAPI()

# Create tables automatically on startup
models.Base.metadata.create_all(bind=database.engine)


@app.post("/blog")
def create(request: schemas.Blog , db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    
@app.get("/blog")
def get_all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{limit}")
def get_all(limit, db: Session = Depends(database.get_db)):
    # .limit(limit) tells Postgres to stop after finding number limit rows
    blogs = db.query(models.Blog).limit(limit).all()
    return blogs

@app.get("/blog/id/{id}")
def get_all(id, db: Session = Depends(database.get_db)):
    # .limit(limit) tells Postgres to stop after finding number limit rows
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blogs




# @app.post("/blog")
# def create_blog(blog: Blog):
#     return {"data": f"Blog titled '{blog.title}' with body '{blog.body}' has been created."}