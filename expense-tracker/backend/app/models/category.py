from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
<<<<<<< HEAD
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    
=======
    name = Column(String)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=text("CURRENT_TIMESTAMP"))
>>>>>>> a8a15a16215bdb95d88eafe92685abb9e3551fd1
