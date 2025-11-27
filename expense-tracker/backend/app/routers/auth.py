from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import CreateUser, ResponseUser
from app.utils.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth",tags=["Auth"])

#Register

@router.post("/register", response_model = ResponseUser)
def register(user: CreateUser, db: Session = Depends(get_db)):

    #Email check wheather its exicts
    existing = db.query(User).filter(User.email == user.email).first()
    if(existing):
        raise HTTPException(status_code=400,detail="Email already registered")

    hashed_pw = hash_password(user.password)

    new_user = User(
        username = user.name,
        email = user.email,
        password_hash = hashed_pw
    )

    db.add(user)
    db.commit()
    db.refresh(new_user)

    return new_user
