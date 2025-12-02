from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 

from app.database import get_db
from app.schemas.category import CreateCategory, ResponseCategory
from app.models.category import Category
from app.utils.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/categories",tags=["Categories"])

@router.post("/",response_model=ResponseCategory)
def create_category(
    category: CreateCategory,
    db: Session= Depends(get_db),
    user: User = Depends(get_current_user)
):
    new_category = Category(
        name = category.name,
        user_id=user.id
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

@router.get("/",response_model=list[ResponseCategory])
def get_categories(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return db.query(Category).filter(Category.user_id == user.id).all()

@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    category = (
        db.query(Category)
        .filter(
            Category.id == category_id,
            Category.user_id == user.id
        )
        .first()
    )

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()

    return {"message": "Category deleted"}