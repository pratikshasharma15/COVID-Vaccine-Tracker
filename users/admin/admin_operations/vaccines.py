import logging
import re
from tabulate import tabulate
from utils import utils
from database import db_operations
from database.db_queries import DbConfig


logger = logging.getLogger('vaccines')


def add_vaccine():
    name = input("Enter vaccine name: ")
    if len(name.strip()) == 0:
        print("Cannot input empty name")
        return
    elif re.match(name, '[a-z,A-Z,,0-9]+') ==  False:
        print("Vaccine name must be alphanumeric only!\n")
        return
    try:
        data = db_operations.db_fetchone_dao('SELECT * FROM vaccine WHERE vaccine_name = ?', (name, ))
        if data:
            raise Exception
    except Exception as e:
        print("Vaccine name already exists!\n")
    id = utils.generate_uuid()
    db_operations.db_dao(DbConfig.ADD_VACCINE,(id, name))
    logger.info('New Vaccine Added!')


def view_vaccine():
    data = db_operations.db_fetchall_dao('SELECT * FROM vaccine')
    print(tabulate(data, headers = ["Vaccine ID", "Vaccine Name"]), "\n")