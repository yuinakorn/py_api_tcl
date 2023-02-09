from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.database import get_db
from routers.items import items_controller
from utils.oauth2 import access_user_token

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/check_update", dependencies=[Depends(access_user_token)])
def check_update(db: Session = Depends(get_db)):
    return items_controller.check_update(db)


@router.post("/{table}", dependencies=[Depends(access_user_token)])
def read_items(table: str, db: Session = Depends(get_db)):
    return items_controller.read_items(table, db)
