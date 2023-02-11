from sqlalchemy.orm import Session
from models.items.items_model import TableStatus
from models.database import get_connection
from fastapi import HTTPException, status


def check_update(db: Session):
    return db.query(TableStatus).all()


def read_items(table: str, db: Session):
    allow_table = db.query(TableStatus).all()
    allow_table_name = [i.table_name for i in allow_table]
    if table not in allow_table_name:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Table {table} not found or not allow to access.")

    connection = get_connection()
    try:
        sql = "SELECT * FROM %s" % table
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
        return result
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=e.args[1])

    finally:
        connection.close()



