from sqlalchemy import Column, Integer, String, ForeignKey, text, DateTime, Float, Date
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.category import Category


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable = False)
    type = Column(String, nullable = False)  # income or expense
    description = Column(String, nullable=True)
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    #Foreign Keys
    user_id = Column(Integer,ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    #Relationships
    user = relationship("User", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")

