import sys
import logging
from datetime import datetime
from utils import utils
from users.employee.emp_controller.vaccination_status import VaccinationStatus
from users.employee.emp_controller.personal_details import PersonalDetails
from config.logs import Logs
from config.prints import Prints
from config.prompts import PromptsConfig
from config.constants import Constant_stmt
from database import db_operations
from database.db_queries import DbConfig


logger = logging.getLogger('employee_menu')

class Employee:
    def __init__(self, user_id) -> None:
        logger.info(Logs.EMPLOYEE_MSG)
        self.user_id = user_id
        self.status = (db_operations.db_fetchone_dao(DbConfig.FETCH_VACC_STATUS,(self.user_id,)))[0]
        self.see_reminders()
        self.menu()

    def menu(self):
        self.vacc_obj = VaccinationStatus(self.user_id)
        employee_choice = int(input(PromptsConfig.EMPLOYEE_PROMPT))
        while employee_choice != 6:
            match employee_choice:
                case 1:
                    self.vacc_obj.print_vacc_status()
                case 2:
                    self.vacc_obj.update_vacc_status()
                case 3:
                    PersonalDetails(self.user_id)
                case 4:
                    return
                case _:
                    print(Prints.ENTER_VALID)    
            employee_choice = int(input(PromptsConfig.EMPLOYEE_PROMPT))
        sys.exit()
  
    def see_reminders(self):
        if self.status == 0:
            print(Prints.REMINDER_1)
        elif self.status == 1:
            is_eligible_for_dose2 = utils.check_date_diff((datetime.now()).strftime("%d/%m/%Y"))
            if is_eligible_for_dose2 == True:
                print(Prints.REMINDER_2)
            else:
                print(Prints.REMINDER_3,self.days, Prints.NEWLINE)
        else:
            print(Prints.REMINDER_4)