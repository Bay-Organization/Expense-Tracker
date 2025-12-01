from sqlalchemy import Column, Integer, String, ForeignKey, text, DateTime, Float, Date
from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)
    description = Column(String, nullable=True)
    date = Column(Date)
    user_id = Column(Integer,ForeignKey("users.id"))
    category_id = Column(String, ForeignKey("categories.id"))
    created_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))