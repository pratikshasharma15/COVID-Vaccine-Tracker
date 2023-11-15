from tabulate import tabulate
from utils import utils
from config.prompts import PromptsConfig
from database import db_operations
from config.prints import Prints
from config.constants import Constants
from users.admin import admin_menu
from database.db_queries import DbConfig

        
def view_all():
    data = db_operations.db_fetchall_dao(DbConfig.FETCH_USER_DETAILS)
    print(tabulate(data, headers= ["UserID","Email", "Vaccination Status" ]))


def view_by_dose(status):
    data = db_operations.db_fetchall_dao(DbConfig.FETCH_BY_DOSE,(status,))
    if data :
        print(tabulate(data, headers = ["User ID", "Username", "Vaccination Status"]))
        print(Prints.SHOW_STATUS_MEANING)
    else:
        print(Prints.NO_VACC_USER)


def view_by_vaccine():
    utils.vaccine_names()
    choice = input(PromptsConfig.GET_VACCINE)
    while choice != Constants.EXIT:
        data = db_operations.db_fetchall_dao(DbConfig.FETCH_BY_VACCINE,(choice,))
        vaccine = db_operations.db_fetchone_dao(DbConfig.FETCH_VACCINE_DETAILS,(choice,))
        if data:
            print(tabulate(data, headers= ["User ID", "email", "Vaccine Name", "Vaccination Status"]), "\n")
        elif vaccine:
            print(Prints.VACCINE_NO_USER)
        else:
            print(Prints.ENTER_VALID_NAME)
        utils.vaccine_names()
        choice = input(PromptsConfig.GET_VACCINE)


def view_by_dose_date(dose_num):
    while True:
        date = input(PromptsConfig.GET_DATE)
        if utils.date_validator(date) == True :
            break
        print(Prints.ENTER_VALID_DATE)

    if dose_num == 1 :
        data = db_operations.db_fetchall_dao(DbConfig.FETCH_BY_DOSE1_DATE,(date,))
    else :
        data = db_operations.db_fetchall_dao(DbConfig.FETCH_BY_DOSE2_DATE,(date,))
        
    if len(data) == 0:
        print(Prints.NO_INFO_FOR_DATE)
    else:
        print(tabulate(data, headers= ["User ID","email", "Vaccine Name", "Dose1 Date", "Dose1 CID", "Dose2 Date", "Dose2 CID"]),"\n")