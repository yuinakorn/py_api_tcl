from sqlalchemy.orm import Session
from models.items.items_model import TableStatus
from models.database import connection


def check_update(db: Session):
    return db.query(TableStatus).all()


def read_items(table: str):
    sql = "SELECT * FROM %s" % table
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()

        return result
    except Exception as e:
        print(e)
        return {"error": e}

