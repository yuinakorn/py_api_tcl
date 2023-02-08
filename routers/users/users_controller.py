import time

from sqlalchemy.orm import Session

from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from models.users.users_model import UserBase, DbUser
from utils.hash import Hash


def create(db: Session, request: UserBase):
    if check_user_exist(db, request.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Username {request.username} already exist",
        )
    current_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    new_user = DbUser(username=request.username, password=Hash.bcrypt(request.password), created_date=current_date, level=2)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def read_users(db: Session):
    return db.query(DbUser).all()


def delete(db: Session, id: int):

    if not check_user_id_exist(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User id {id} not found"
        )

    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return JSONResponse(content={"detail": f"Username {id} deleted"})


def read_user_by_id(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()


def update(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if user.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User id {id} not found"
        )
    else:
        user.update(
            {
                DbUser.username: request.username,
                DbUser.password: Hash.bcrypt(request.password),
            }
        )
        db.commit()
        return JSONResponse(
            content={"detail": f"User id {id} updated successful"},
            status_code=status.HTTP_200_OK,
        )


def check_user_exist(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if user is None:
        return False
    else:
        return True


def check_user_id_exist(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if user is None:
        return False
    else:
        return True
