from sqlalchemy import Column, Integer, String, ForeignKey, text, DateTime, Float, Date
from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable = False)
    type = Column(String, nullable = False)  # income or expense
    description = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))