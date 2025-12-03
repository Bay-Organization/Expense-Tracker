from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date,timedelta

from app.database import get_db
from app.models.category import Category
from app.models.transaction import Transaction
from app.utils.deps import get_current_user
from app.models.user import User

router=APIRouter(prefix="/summary",tags=["Summary"])

@router.get("/totals")
def get_totals(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    income = db.query(func.sum(Transaction.amount)).filter(Transaction.user_id==user.id, Transaction.type == "income").scalar() or 0
    expense = db.query(func.sum(Transaction.amount)).filter(Transaction.user_id==user.id, Transaction.type == "expense").scalar() or 0

    balance = income - expense

    return {
        "total income" : income,
        "total expence" : expense,
        "balance" : balance
    }

@router.get("/categories")
def spending_by_category(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    results = (
        db.query(Category.name, func.sum(Transaction.amount))
        .join(Transaction, Transaction.category_id == Category.id)
        .filter(
            Transaction.user_id == user.id,
            Transaction.type == "expense"
        )
        .group_by(Category.name)
        .all()
    )

    return [{"category": name, "total": total} for name, total in results]

@router.get("/monthly")
def monthly_summary(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    results = (
        db.query(
            func.strftime("%Y-%m", Transaction.date).label("month"),
            func.sum(Transaction.amount).label("total")
        )
        .filter(Transaction.user_id == user.id)
        .group_by("month")
        .order_by("month")
        .all()
    )

    return [{"month": m, "total": t} for m, t in results]

@router.get("/weekly")
def weekly_summary(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    seven_days_ago = date.today() - timedelta(days=6)

    results = (
        db.query(
            Transaction.date,
            func.sum(Transaction.amount)
        )
        .filter(
            Transaction.user_id == user.id,
            Transaction.date >= seven_days_ago
        )
        .group_by(Transaction.date)
        .order_by(Transaction.date)
        .all()
    )

    return [{"date": str(d), "total": t} for d, t in results]

