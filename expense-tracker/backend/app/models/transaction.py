from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable = False)
    type = Column(String, nullable = False)  # income or expense
    description = Column(String, nullable=True)
    date = Column(Date, nullable=False)
<<<<<<< HEAD

    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    
=======
    user_id = Column(Integer,ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
>>>>>>> a8a15a16215bdb95d88eafe92685abb9e3551fd1
