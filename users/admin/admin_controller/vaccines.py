from tabulate import tabulate
from utils import utils
from database import db_operations
from database.db_queries import DbConfig


def add_vaccine():
    name = input("Enter vaccine name: ")
    id = utils.generate_uuid()
    db_operations.db_dao(DbConfig.ADD_VACCINE,(id, name))


def view_vaccine():
    data = db_operations.db_fetchall_dao('SELECT * FROM vaccine')
    print(tabulate(data, headers = ["Vaccine ID", "Vaccine Name"]), "\n")