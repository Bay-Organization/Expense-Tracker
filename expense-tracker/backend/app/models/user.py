from sqlalchemy import Column, Integer, String, text, DateTime
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True)
    email = Column(String,unique=True,index=True)
    password_hash = Column(
        String)
    created_at = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP")
    ) 