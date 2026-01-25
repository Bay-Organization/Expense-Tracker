from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True)
    email = Column(String,unique=True,index=True)
    password_hash = Column(String, nullable=False)
<<<<<<< HEAD
    
=======
    created_at = Column(DateTime(timezone=True),server_default=text("CURRENT_TIMESTAMP")) 
   
>>>>>>> a8a15a16215bdb95d88eafe92685abb9e3551fd1
