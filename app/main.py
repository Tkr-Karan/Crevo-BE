from fastapi import FastAPI, Depends
from typing import Annotated
from sqlalchemy.orm import Session

from app.db.database import engine, Session_Local, Base
from app.models.user import User
from app.schemas.user import UserCreate
app = FastAPI(
    title="My FastAPI App",
    description="My FastAPI App",
    version="0.0.1",
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session ,Depends(get_db)]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    return {"status": "Your server is working fine, and FastAPI working and running FINE!!!! :)"}


@app.post("/test_db")
async def test_db(user_data:UserCreate ,db: db_dependency):
    user = User(
        email=user_data.email,
        password=user_data.password,
    )

    db.add(user)
    db.commit()
    db.refresh(user)


    users = db.query(User).all()

    return {
        "total_users": len(users),
        "users": [u.email for u in users],
    }
