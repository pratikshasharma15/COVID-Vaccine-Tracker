import sys
import logging
from os import system
from utils import utils
from config.logs import Logs
from config.prints import Prints
from config.constants import Constants
from config.prompts import PromptsConfig
from users.admin.admin_operations import vaccines,approve_details,add_user
from users.admin.admin_operations.view_vaccinated_emp import view_vacc_emp_menu as vacc_menu

logger = logging.getLogger('admin_menu')

class Admin:
    def __init__(self, user_id) -> None:
        logger.info(Logs.ADMIN_MSG)
        self.user_id = user_id
        system('cls')
        self.menu()

    def menu(self):   
        admin_choice = (input(PromptsConfig.ADMIN_PROMPT))
        while admin_choice != '8':
            match admin_choice:
                case '1':
                    add_user.add_new_user()
                case '2':
                    vacc_menu.view_vacc_status_menu()
                case '3':
                    vaccines.add_vaccine()
                case '4':
                    vaccines.view_vaccine()
                case '5':
                    approve_details.approval_prompt()
                case '6':
                    approve_details.view_approved_details()
                case '7':
                    system('cls')
                    return
                case _:
                    print(Prints.ENTER_VALID)
            admin_choice = (input(PromptsConfig.ADMIN_PROMPT))
        sys.exit()