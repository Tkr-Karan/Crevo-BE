from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db:Session =  Depends(get_db)):
    db_user = User(
        id= "123432",
        email=user.email,
        password=user.password,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user