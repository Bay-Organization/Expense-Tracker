from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryResponse
from app.utils.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    new_cat = Category(
        name=category.name,
        user_id=user.id
    )
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat

@router.get("/", response_model=list[CategoryResponse])
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
    cat = db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == user.id
    ).first()

    if not cat:
        raise HTTPException(404, "Category not found")

    db.delete(cat)
    db.commit()
    return {"message": "Category deleted"}
