from sqlalchemy import Integer, Column, DateTime, ForeignKey, String, Text
from ..database import Base



class category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=Text("CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Shanghai'"))
