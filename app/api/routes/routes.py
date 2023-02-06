from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from api.controllers import controller
from api.models import UserDB, UserSchema
from api.utils.database.user import SessionLocal


router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/create",responseModel=UserDB,status_code=201)
def create_user(*,db: Session = Depends(get_db), payload: NoteSchema):
    note = controller.post(db_session=db, payload = payload)
    return note 


@router.get("/{id}/",response_model=UserDB)
def get_user_by_id(*,db: Session = Depends(get_db), id: int = Path(..., gt=0),):
    user = controller.get(db_session=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user