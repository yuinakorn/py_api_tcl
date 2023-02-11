from dotenv import dotenv_values
from sqlalchemy.orm import Session
from models.items.items_model import TableStatus
from fastapi import HTTPException, status
import pymysql.cursors

config_env = dotenv_values(".env")


def check_update(db: Session):
    return db.query(TableStatus).all()


def read_items(table: str, db: Session):
    allow_table = db.query(TableStatus).all()
    allow_table_name = [i.table_name for i in allow_table]
    if table not in allow_table_name:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Table {table} not found or not allow to access.")

    try:
        connection = pymysql.connect(host=config_env["HOST"],
                                     user=config_env["USER"],
                                     password=config_env["PASSWORD"],
                                     db=config_env["DB_NAME"],
                                     charset=config_env["CHARSET"],
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        sql = "SELECT * FROM %s" % table
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
        connection.close()
        return result
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=e.args[1])





