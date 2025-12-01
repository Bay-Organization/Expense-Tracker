from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer # OAuth2 authentication scheme for bearer tokens
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.utils.auth import ALGORITHM, SECRET_KEY

#OAuth2 scheme that extracts bearer token from Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Dependency function that validates JWT token and returns authenticated user
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    #create exception to raise if authentication fails
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate" : "Bearer"}, #Tell client Bearer auth is required 
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credential_exception
    
    return user