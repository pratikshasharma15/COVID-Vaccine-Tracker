import re
import logging
from tabulate import tabulate
from utils import utils
from utils.exceptions import VaccineNameError
from config.Queries.db_queries import DbConfig
from config.Prompts.prompts import PromptsConfig
from database import db_operations


logger = logging.getLogger('vaccines')


def add_vaccine():

    name = input("Enter vaccine name: ")

    try:
        if len(name.strip()) == 0:
            raise VaccineNameError(PromptsConfig.EMPTY_NAME_ERROR)
        elif re.fullmatch(name, '^[a-zA-Z]*$') is None:
            raise VaccineNameError(PromptsConfig.NOT_ALPHABETIC_NAME)
        
        data = db_operations.db_fetchone_dao(DbConfig.FETCH_VACCINE_DETAILS, (name, ))
        
        if data:
            raise VaccineNameError(PromptsConfig.NAME_ALREADY_EXISTS)
        
    except VaccineNameError as v:
        print(v.msg)
    
    else:
        id = utils.generate_uuid()
        db_operations.db_dao(DbConfig.ADD_VACCINE,(id, name))
        logger.info('New Vaccine Added!')


def view_vaccine():

    data = db_operations.db_fetchall_dao(DbConfig.FETCH_VACCINE)
    print(tabulate(data, headers = ["Vaccine ID", "Vaccine Name"]), "\n")