from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.category import Category as CategoryModels
from app.schemas.category import CreateCategory, ResponseCategory
from app.utils.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=list[ResponseCategory])
def list_categories(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    #List all categories for authenticated user
    catergories = db.query(CategoryModels).filter(CategoryModels.user_id == current_user.id).all()
    return catergories

@router.post("/", response_model=ResponseCategory, status_code=status.HTTP_201_CREATED)
def create_category(category_in: CreateCategory, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    #Create a new category for the authenticated user.
    existing_category = db.query(CategoryModels).filter(CategoryModels.name == category_in.name,CategoryModels.user_id == current_user.id).first()

    if existing_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    
    category = CategoryModels(
        name = category_in.name,
        #Link the category to the authenticated user
        user_id = current_user.id, 
    )
    
    db.add(category)
    db.commit()
    db.refresh(category)
    return category
