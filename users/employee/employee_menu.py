import sys
import logging
from os import system
from datetime import datetime
from utils import utils
from users.employee.emp_operations.vaccination_status import VaccinationStatus
from users.employee.emp_operations.profile import Profile
from config.logs import Logs
from config.prints import Prints
from config.prompts import PromptsConfig
from config.constants import Constants
from database import db_operations
from database.db_queries import DbConfig

logger = logging.getLogger('employee_menu')

class Employee:
    def __init__(self, user_id) -> None:
        logger.info(Logs.EMPLOYEE_MSG)
        print("*******WELCOME TO EMPLOYEE DASHBOARD**********")
        system('cls')
        self.user_id = user_id
        self.status = (db_operations.db_fetchone_dao(DbConfig.FETCH_VACC_STATUS,(self.user_id,)))[0]
        self.show_reminders()
        self.menu()

    def menu(self):
        self.vacc_obj = VaccinationStatus(self.user_id)
        employee_choice = (input(PromptsConfig.EMPLOYEE_PROMPT))
        while employee_choice != '5':
            match employee_choice:
                case '1':
                    self.vacc_obj.print_vacc_status()
                case '2':
                    self.vacc_obj.update_vacc_details_menu()
                case '3':
                    Profile(self.user_id)
                case '4':
                    system('cls')
                    return
                case _:
                    print(Prints.ENTER_VALID)    
            employee_choice = (input(PromptsConfig.EMPLOYEE_PROMPT))
        sys.exit()
  
    def show_reminders(self):
        if self.status == 0:
            print("\n",Prints.REMINDER_1)
        elif self.status == 1:
            self.dose_1_date = (db_operations.db_fetchone_dao(DbConfig.SELECT_DOSE1_DATE,(self.user_id,)))[0]
            is_eligible_for_dose2 = utils.check_date_diff((datetime.now()).strftime("%d/%m/%Y"), self.dose_1_date )
            if is_eligible_for_dose2 == True:
                print("\n",Prints.REMINDER_2)
            else:
                print("\n",Prints.REMINDER_3, Constants.NEWLINE)
        else:
            print("\n",Prints.REMINDER_4)