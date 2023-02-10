from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib import parse

import pymysql.cursors

config_env = dotenv_values(".env")

engine = create_engine("mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8mb4".format(
    user=config_env['USER'],
    password=parse.quote_plus(config_env['PASSWORD']),
    host=config_env['HOST'],
    port=config_env['PORT'],
    db_name=config_env['DB_NAME'],
    connection_timeout=60,
    buffered=True
))

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()


config_env = dotenv_values(".env")

connection = pymysql.connect(host=config_env["HOST"],
                             user=config_env["USER"],
                             password=config_env["PASSWORD"],
                             db=config_env["DB_NAME"],
                             charset=config_env["CHARSET"],
                             cursorclass=pymysql.cursors.DictCursor)
