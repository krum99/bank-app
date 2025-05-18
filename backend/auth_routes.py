from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from auth import hash_password
from models.user import User
from database import SessionLocal
from auth import verify_password
from fastapi import status

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    db = SessionLocal()
    user = db.query(User).filter(User.username == request.username).first()
    
    if not user:
        db.close()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    if not verify_password(request.password, user.password_hash):
        db.close()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    db.close()
    return {"message": "Login successful", "user_id": user.id}


class RegisterRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(request: RegisterRequest):
    db = SessionLocal()

    existing_user = db.query(User).filter(User.username == request.username).first()
    if existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    user = User(
        username=request.username,
        password_hash=hash_password(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return {"message": "User created successfully", "user_id": user.id}
