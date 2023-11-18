import sys
import logging
from os import system
from datetime import datetime
from utils import utils
from utils.decorators import log_function_call
from config.Logs.logs import Logs
from config.Prints.prints import Prints
from config.Queries.db_queries import DbConfig
from config.Prompts.prompts import PromptsConfig
from config.Constants.constants import Constants
from database import db_operations
from users.employee.emp_operations.profile import Profile
from users.employee.emp_operations.vaccination_status import VaccinationStatus

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
        """
            Menu functions which shows different operations an employee can perform.
        """
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
            print(Constants.NEWLINE,Prints.REMINDER_1)
        elif self.status == 1:
            self.dose_1_date = (db_operations.db_fetchone_dao(DbConfig.SELECT_DOSE1_DATE,(self.user_id,)))[0]
            is_eligible_for_dose2 = utils.check_date_diff((datetime.now()).strftime("%d/%m/%Y"), self.dose_1_date )
            if is_eligible_for_dose2 == True:
                print(Constants.NEWLINE,Prints.REMINDER_2)
            else:
                print(Constants.NEWLINE,Prints.REMINDER_3, Constants.NEWLINE)
        else:
            print(Constants.NEWLINE,Prints.REMINDER_4)