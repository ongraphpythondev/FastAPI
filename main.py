import schema
import models
from database_connection import SessionLocal, engine
from fastapi import FastAPI, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm.session import Session




# This is for creating(if not) the database and table
models.Base.metadata.create_all(engine)




# This is the object of FastAPI.
blog_app = FastAPI()



# This is to define the "db" variable and to create the Session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    
    finally:
        db.close()



# This is for creating the
@blog_app.post('/blog/create/', status_code=status.HTTP_201_CREATED)
def create(request: schema.Blog,  db: Session = Depends(get_db)):
    try:
        new_blog = models.Blog(title = request.title, body = request.body)
        db.add(new_blog)
    except Exception as e:
        return str(e)
    db.commit() # This is for commit the changes
    db.refresh(new_blog)
    return {'msg': "created", 'data': request}




# This is for getting all blogs from table.
@blog_app.get('/blog/get', status_code=status.HTTP_200_OK)
def get_all(db: Session = Depends(get_db)):
    try:
        blogs = db.query(models.Blog).all()
    except Exception as e:
        return str(e)
    if not blogs:
        return HTTPException(status_code=status.HTTP_201_CREATED, detail="No content")
    return blogs




# This is for getting a particular blog with the reference of title.
@blog_app.get('/blog//get/{title}', status_code=status.HTTP_200_OK)
def get_one(title: str, db: Session = Depends(get_db)):
    try:
        blog = db.query(models.Blog).filter(models.Blog.title == title).all()
    except Exception as e:
        return str(e)
    
    if not blog:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail= f"No matching content regarding{id}")

    return blog




# This is for Update the blog with id.
@blog_app.put('/blog/update/{id}', status_code=status.HTTP_200_OK)
def update_blog(id: int, request: schema.Blog, db: Session = Depends(get_db)):

    try:
        blog = db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    except Exception as e:
        return str(e)
    
    if not blog:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail= f"No matching content regarding {id}")
    
    db.commit()
    return {'msg': f"Successfully Updated {id}", 'data': request.dict()}




# This is for delete a particular blog with reference of id of that blog.
@blog_app.delete('/blog/delete/{id}', status_code=status.HTTP_200_OK)
def delete_blog(id: int, db: Session = Depends(get_db)):
    
    try:
        blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    except Exception as e:
        return str(e)

    if not blog:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"No content regarding {id}")
    
    db.commit()
    return f"id {id} deleted"


