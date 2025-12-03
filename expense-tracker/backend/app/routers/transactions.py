from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from datetime import date

from app.database import get_db
from app.schemas.transaction import CreateTransaction,ResponseTransaction
from app.models.transaction import Transaction
from app.models.category import Category
from app.utils.deps import get_current_user
from app.models.user import User

router=APIRouter("/transaction",tags=["Transaction"])

@router.post("/",response_model=ResponseTransaction)
def create_transaction(
    tx: CreateTransaction,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    category=(
        db.query(Category).filter(
            Category.id==tx.category_id,
            Category.user_id==user.id
        )
    ).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    new_tx = Transaction(
        amount=tx.amount,
        type=tx.type,
        description=tx.description,
        date=tx.date,
        user_id=user.id,
        category_id=tx.category_id
    )

    db.add(new_tx)
    db.commit()
    db.refresh(new_tx)

    return new_tx

@router.get("/",response_model=list[ResponseTransaction])
def get_transactions(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return db.query(Transaction).filter(Transaction.user_id==user.id).order_by(Transaction.date.desc()).all()

@router.get("/{tx_id}",response_model=ResponseTransaction)
def get_transaction(
    tx_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    tx = db.query(Transaction).filter(Transaction.id==tx_id, Transaction.user_id==user.id).first()

    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not Found")
    
    return tx

router.delete("/{tx_id}")
def delete_transaction(
        tx_id: int,
        db: Session = Depends(get_db),
        user: User = Depends(get_current_user)
):
    tx = (db.query(Transaction).filter(Transaction.id==tx_id, Transaction.user_id==user.id).first())

    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not Found")
    
    return {"message":"Transaction Deleted"}