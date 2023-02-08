from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

from models.database import Base
from pydantic import BaseModel


class TableStatus(Base):
    __tablename__ = "table_status"
    table_name = Column(String, primary_key=True, index=True)
    d_update = Column(String)


class TableStatusBase(BaseModel):
    table_name: str
    d_update: str

    class Config:
        orm_mode = True
