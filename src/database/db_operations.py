import logging
from config.Constants.constants import Constants
from config.Prints.prints import Prints
from config.Queries.db_queries import DbConfig
from database.db_connection import DatabaseConnection

logger = logging.getLogger('Database')

def db_dao(db_query, *args):
    try:
        with DatabaseConnection(Constants.DB_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(db_query, *args)
    except Exception as e:
        logger.error(e)
        print("Something went wrong! Please try again!")

def db_fetchall_dao(db_query, *args):
    try:
        with DatabaseConnection(Constants.DB_NAME) as connection:
            cursor = connection.cursor()
            data = (cursor.execute(db_query, *args)).fetchall()
            return data
    except Exception as e:
        logger.error(e)
        print("Something went wrong! Please try again!")
    
def db_fetchone_dao(db_query, *args):
    try:
        with DatabaseConnection(Constants.DB_NAME) as connection:
            cursor = connection.cursor()
            data = (cursor.execute(db_query, *args)).fetchone()
            return data
    except Exception as e:
        logger.error(e)
        print("Something went wrong! Please try again!")