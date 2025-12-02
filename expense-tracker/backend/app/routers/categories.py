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

@router.get("/{category_id}", response_model = ResponseCategory)
def get_category(category_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    #get single category by its ID for the authenticated user
    category = db.query(CategoryModels).filter(
        CategoryModels.id == category_id,
        CategoryModels.user_id == current_user.id,
    ).first()

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return category

@router.put("/{catergory_id}", response_model=ResponseCategory)
def update_category(category_id: int, category_in: CreateCategory, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    #Update catergory by its ID for authenticated user
    category = db.query(CategoryModels).filter(
        CategoryModels.id == category_id,
        CategoryModels.user_id == current_user.id,
    ).first()

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    category.name = category_in.name
    db.commit()
    db.refresh(category)

    return category

@router.delete("/{catergory_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    #Delete a category by its ID for authenticated user
    category = db.query(CategoryModels).filter(
        CategoryModels.id == category_id,
        CategoryModels.user_id == current_user.id,
    ).first()

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.delete(category)
    db.commit()

    return None