import sqlite3
from config.constants import Constants
from config.prints import Prints
from database.db_connection import DatabaseConnection


def db_dao(db_query, *args):
    with DatabaseConnection(Constants.DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(db_query, *args)

def db_fetchall_dao(db_query, *args):
    with DatabaseConnection(Constants.DB_NAME) as connection:
        cursor = connection.cursor()
        data = (cursor.execute(db_query, *args)).fetchall()
        return data
    
def db_fetchone_dao(db_query, *args):
    with DatabaseConnection(Constants.DB_NAME) as connection:
        cursor = connection.cursor()
        data = (cursor.execute(db_query, *args)).fetchone()
        return data