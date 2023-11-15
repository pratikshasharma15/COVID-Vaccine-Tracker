import logging
import re
from tabulate import tabulate
from utils import utils
from utils.exceptions import VaccineNameError
from database import db_operations
from database.db_queries import DbConfig


logger = logging.getLogger('vaccines')


def add_vaccine():
    name = input("Enter vaccine name: ")
    try:
        if len(name.strip()) == 0:
            raise VaccineNameError("Cannot input empty name!")
        elif re.match(name, '^[a-z,A-Z][a-zA-Z ]+[a-zA-Z]$') ==  False:
            raise VaccineNameError("Vaccine name must be alphanumeric only!\n")
        
        data = db_operations.db_fetchone_dao('SELECT * FROM vaccine WHERE vaccine_name = ?', (name, ))
        if data:
            raise VaccineNameError("Vaccine name already exists!\n")
        
    except VaccineNameError as v:
        print(v.msg)
    
    else:
        id = utils.generate_uuid()
        db_operations.db_dao(DbConfig.ADD_VACCINE,(id, name))
        logger.info('New Vaccine Added!')


def view_vaccine():
    data = db_operations.db_fetchall_dao('SELECT * FROM vaccine')
    print(tabulate(data, headers = ["Vaccine ID", "Vaccine Name"]), "\n")