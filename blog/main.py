from fastapi import Depends, FastAPI , status , Response , HTTPException
from blog import schemas
from blog import models, database
from sqlalchemy.orm import Session


app = FastAPI()

# Create tables automatically on startup
models.Base.metadata.create_all(bind=database.engine)


# Status code for created is 201
@app.post("/blog" , status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog , db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete("/blog/{id}" )
def destroy(id , db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Deleted Successfully"


@app.put("/blog/{id}" )
def update(id, request: schemas.Blog , db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return "Updated Successfully"

@app.get("/blog" )
def get_all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{limit}")
def get_all(limit, db: Session = Depends(database.get_db)):
    # .limit(limit) tells Postgres to stop after finding number limit rows
    blogs = db.query(models.Blog).limit(limit).all()
    return blogs

@app.get("/blog/id/{id}" , status_code=200)
def get_all(id ,response: Response,db: Session = Depends(database.get_db)):
    # .limit(limit) tells Postgres to stop after finding number limit rows
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
        # or you can use below code
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f"Blog with id {id} not found"}
    return blogs






# @app.post("/blog")
# def create_blog(blog: Blog):
#     return {"data": f"Blog titled '{blog.title}' with body '{blog.body}' has been created."}