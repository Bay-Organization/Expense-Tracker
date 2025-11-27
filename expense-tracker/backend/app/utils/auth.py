from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

#for hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


#Secret key for JWT (in production put in .env)
SECRET_KEY  = "supersecretkey123"
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 60

#Hashing password 
def hash_password(password : str):
    return pwd_context.hash(password)

#Password Verification
def verify_password(plain : str, hashed : str ):
    return pwd_context.hash(plain, hash)

#Creating JWT token
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes = ACCES_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt 