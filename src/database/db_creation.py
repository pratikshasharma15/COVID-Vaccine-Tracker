from config.constants import Constants
from config.prints import Prints
from database.db_queries import DbConfig
from database.db_connection import DatabaseConnection

class create_db:
    """
    Create all the tables if not exists in database.
    """
    def __init__(self) -> None:
        with DatabaseConnection(Constants.DB_NAME) as connection:
            self.cursor=connection.cursor()
            self.create_tables()

    def create_tables(self):
        self.cursor.execute(DbConfig.CREATE_AUTH_TABLE)
        self.cursor.execute(DbConfig.CREATE_USER_DETAILS_TABLE)
        self.cursor.execute(DbConfig.CREATE_DOSE_DETAILS_TABLE)
        self.cursor.execute(DbConfig.CREATE_ADMIN_APPROVAL_TABLE)
        self.cursor.execute(DbConfig.CREATE_VACCINE_TABLE)
        # self.cursor.execute("delete from vaccine where vaccine_id = 2985 ")
        # self.cursor.execute("delete from vaccine where vaccine_id = 2139 ")