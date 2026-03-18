from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    id: str
    email: EmailStr
    password: str

class EarlyAccessUserCreate(BaseModel):
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True