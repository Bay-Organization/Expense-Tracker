from sqlalchemy import Integer, Column, DateTime, ForeignKey, String, text
from ..database import Base



class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=True)
    created_at = Column(DateTime(timezone=True),
                         server_default=text("CURRENT_TIMESTAMP"))
