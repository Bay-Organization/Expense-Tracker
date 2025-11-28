from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

#For hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

#Secret key for JWT (in production put in .env)
SECRET_KEY= "supersecretkey123"
ALGORITH = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# hashing passwords
def hash_password(password: str):
    return pwd_context.hash(password)

# Verificatoin password
def verify_password(plain: str, hash: str):
    return pwd_context.verify(plain, hash)

# Create JWT token
def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update("exp": expire)

    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITH)
    return encoded_jwt
