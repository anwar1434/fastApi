from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from blog import models, schemas, database
from blog.hashing import Hash

def create(db: Session, request: schemas.User):
    # Hash password before storing
    hashed_password = Hash.hash_password(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Fetch updated data from DB
    return new_user

def get_all(db: Session):
    # Get all users (without rehashing passwords)
    users = db.query(models.User).all()
    return users


def get_specific( id: int, db:Session):
    user= db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'User with the id {id} is not available')
    return user

def destroy(id:int, db:Session):
    users = db.query(models.User).filter(models.User.id == id)
    if not users.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'User with the id {id} is not found')
    users.delete(synchronize_session=False)
    db.commit()
    return {'Delete blog is done sucssfuly'}