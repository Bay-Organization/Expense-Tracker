from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.transaction import Transaction
from app.models.category import Category
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.utils.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=TransactionResponse)
def create_transaction(
    tx: TransactionCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    category = db.query(Category).filter(
        Category.id == tx.category_id,
        Category.user_id == user.id
    ).first()

    if not category:
        raise HTTPException(404, "Category not found")

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

@router.get("/", response_model=list[TransactionResponse])
def get_transactions(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return (
        db.query(Transaction)
        .filter(Transaction.user_id == user.id)
        .order_by(Transaction.date.desc())
        .all()
    )

@router.get("/{tx_id}", response_model=TransactionResponse)
def get_one(
    tx_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    tx = db.query(Transaction).filter(
        Transaction.id == tx_id,
        Transaction.user_id == user.id
    ).first()

    if not tx:
        raise HTTPException(404, "Transaction not found")
    return tx

@router.delete("/{tx_id}")
def delete_transaction(
    tx_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    tx = db.query(Transaction).filter(
        Transaction.id == tx_id,
        Transaction.user_id == user.id
    ).first()

    if not tx:
        raise HTTPException(404, "Transaction not found")

    db.delete(tx)
    db.commit()
    return {"message": "Transaction deleted"}
