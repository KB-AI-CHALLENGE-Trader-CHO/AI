# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List
# from app.database import get_db
# from app.schemas.user import User, UserCreate, UserUpdate
# from app.models.user import User as UserModel
#
# router = APIRouter()
#
#
# @router.get("/", response_model=List[User])
# async def get_users(
#         skip: int = 0,
#         limit: int = 100,
#         db: Session = Depends(get_db)
# ):
#     """사용자 목록 조회"""
#     users = db.query(UserModel).offset(skip).limit(limit).all()
#     return users
#
#
# @router.get("/{user_id}", response_model=User)
# async def get_user(user_id: int, db: Session = Depends(get_db)):
#     """특정 사용자 조회"""
#     user = db.query(UserModel).filter(UserModel.id == user_id).first()
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#     return user
#
#
# @router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     """새 사용자 생성"""
#     db_user = UserModel(**user.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# @router.put("/{user_id}", response_model=User)
# async def update_user(
#         user_id: int,
#         user: UserUpdate,
#         db: Session = Depends(get_db)
# ):
#     """사용자 정보 수정"""
#     db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#
#     for field, value in user.dict(exclude_unset=True).items():
#         setattr(db_user, field, value)
#
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# @router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_user(user_id: int, db: Session = Depends(get_db)):
#     """사용자 삭제"""
#     db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#
#     db.delete(db_user)
#     db.commit()
#     return None
