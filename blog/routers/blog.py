from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from blog.Rebo import blog


router = APIRouter(
  prefix= "/blog",
  tags= ['Blogs']
)

get_db = database.get_db

@router.get('/', response_model= List[schemas.ShowBlog])
def All_blog(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)): 
  return blog.get_all(db)

@router.post('/log', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
  return blog.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
  return blog.destory(id, db)


@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def UP_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
  return blog.update(id, db, request)

@router.get('/{id}', status_code=200, response_model= schemas.ShowBlog) #
def Sp_blog(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
  return blog.get_specific(id, db)