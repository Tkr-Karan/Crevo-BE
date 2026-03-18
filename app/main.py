import os
from fastapi import FastAPI, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from app.db.database import engine, Session_Local, Base, get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
import os
from dotenv import load_dotenv
from app.routes import users


load_dotenv()

ENV = os.getenv("ENV", "development")

app = FastAPI(
    title="My FastAPI App",
    description="My FastAPI App",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# def get_db():
#     db = Session_Local()
#     try:
#         yield db
#     finally:
#         db.close()


db_dependency = Annotated[Session ,Depends(get_db)]


app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    return {"status": "Your server is working fine, and FastAPI working and running FINE!!!! :)"}


@app.get("/test_db")
async def test_db(db: db_dependency):
    # user = User(
    #     email=user_data.email,
    #     password=user_data.password,
    # )
    #
    # db.add(user)
    # db.commit()
    # db.refresh(user)
    #

    users = db.query(User).all()

    return {
        "total_users": len(users),
        "users": [u.email for u in users],
    }
