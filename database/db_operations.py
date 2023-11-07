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
    with DatabaseConnection("database\\vaccine_tracker.db") as connection:
        cursor = connection.cursor()
        data = (cursor.execute(db_query, *args)).fetchone()
        return data

# def add_user(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)

# def fetchdata_by_dose(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         data = (cursor.execute(db_query, *args)).fetchall()
#         return data

# def fetchdata_by_vaccine(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         data = (cursor.execute(db_query, *args)).fetchall()
#         return data

# def fetch_by_date(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         data = (cursor.execute(db_query, *args)).fetchall()
#         return data
        
# def fetch_approval_data(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         data = (cursor.execute(db_query, *args)).fetchall()
#         return data
    
# def update_dose_1_approval(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)

# def update_dose_2_approval(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query,*args)

# def add_vaccine(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)

# def fetch_status(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         status = (cursor.execute(db_query, *args)).fetchone()
#         return status
    
# def add_dose_details(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)

# def add_user_details(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)
        
# def fetch_vaccine_names(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         data = (cursor.execute(db_query, *args)).fetchall()
#         return data
    
# def update_dose1_details(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)

# def update_dose2_details(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)

# def update_vacc_status(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)

# def update_name(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)

# def update_gender(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)

# def is_available(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         return (cursor.execute(db_query, *args)).fetchall()
    
# def fetch_date(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)
#         data = cursor.fetchone()
#         return data

# def find_vaccine(db_query, *args):
#     with DatabaseConnection('database\\vaccine_tracker.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(db_query, *args)
#         data = cursor.fetchone()
#         return data