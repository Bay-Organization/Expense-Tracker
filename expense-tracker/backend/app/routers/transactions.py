from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.transaction import Transaction as TransactionModel
from app.models.user import User
from app.schemas.transaction import(
    CreateTransaction,
    ResponseTransaction,
)
from app.utils.deps import get_current_user


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)

@router.get("/", response_model=List[ResponseTransaction])
def list_transactions(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    #List all Transactions for authenticated user.
    transactions = (
        db.query(TransactionModel)
        .filter(TransactionModel.user_id == current_user.id)
        .order_by(TransactionModel.date.desc())
        .all()
    )
    return transactions

@router.post("/", response_model=ResponseTransaction, status_code=status.HTTP_201_CREATED)
def create_transaction(transaction_in: CreateTransaction, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    #Create transaction for authenticated user.
    transaction = TransactionModel (
        amount = transaction_in.amount,
        type = transaction_in.type,
        description = transaction_in.description,
        date = transaction_in.date,
        category_id = transaction_in.category_id,
        user_id = current_user.id,
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

@router.get("/{transaction_id}", response_model=ResponseTransaction)
def get_transaction(transaction_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    #Get a single transaction owned by authenticated user
    transaction = (
        db.query(TransactionModel).filter(TransactionModel.id == transaction_id, TransactionModel.user_id == current_user.id).first()
    )
    
    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found",
        )
    return transaction

@router.delete("/{transaction_id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_transaction(transaction_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    #For deletion a transaction owned by authenticated user.
    transaction = (
        db.query(TransactionModel).filter(
            TransactionModel.id == transaction_id,
            TransactionModel.user_id == current_user.id,
        ).first()
    )

    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail= "Transaction not found"
        )
    
    db.delete(transaction)
    db.commit()
    return None