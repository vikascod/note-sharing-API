from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db
from werkzeug.security import generate_password_hash



router = APIRouter(
    tags=['User']
)

@router.post('/create-user', status_code=status.HTTP_201_CREATED)
async def create_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
    hashed_password = generate_password_hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
