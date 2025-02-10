from typing import List
from fastapi import APIRouter, Depends, status, Response
from blog import schemas, database
from sqlalchemy.orm import Session
from blog.Rebo import user

router = APIRouter(
  prefix= "/user",
  tags= ['Users'] 
)
get_db = database.get_db

#Add User information (name, email, password):

@router.post("/", response_model= schemas.ShowUser)
def creat_User(request: schemas.User, db: Session = Depends(get_db)):
  return user.create(db, request)

@router.get("/", response_model=List[schemas.ShowUser]) #response model to show user, we add "List" when get all user data
def All_user(response: Response ,db: Session = Depends(get_db)):
  return user.get_all(db)

@router.get('/{id}', response_model=schemas.ShowUser) 
def SP_user(id, db: Session = Depends(get_db)):
  return user.get_specific(id, db)


@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy_user(id, response: Response, db: Session = Depends(get_db)):
  return user.create(id, db)