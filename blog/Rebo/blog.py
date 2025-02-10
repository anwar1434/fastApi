from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db:Session ):
    new_blog = models.Blog(title=request.title, body=request.body, user_id= 1)  # Convert Pydantic to ORM model
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)  # Fetch updated data from DB
    return new_blog

def destory(id: int, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Blog with the id {id} is not found')
    
    blogs.delete(synchronize_session=False)
    db.commit()
    return {'Delete blog is done sucssfuly'}

def update(id: int, db: Session, request: schemas.Blog ):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Blog with the id {id} is not found')
    
    blogs.update(request)
    db.commit()
    return 'update done'

def get_specific(id: int, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Blog with the id {id} is not available')
    return blogs