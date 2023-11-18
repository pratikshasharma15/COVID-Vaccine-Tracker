import sys
import logging
from os import system
from config.Logs.logs import Logs
from config.Prints.prints import Prints
from config.Constants.constants import Constants
from config.Prompts.prompts import PromptsConfig
from users.admin.admin_operations import vaccines,approve_details,add_user
from users.admin.admin_operations.view_vaccinated_emp import view_menu 


logger = logging.getLogger('admin_menu')


class Admin:
   
    def __init__(self, user_id) -> None:
        logger.info(Logs.ADMIN_MSG)
        self.user_id = user_id
        system('cls')
        self.menu()

    def menu(self):  

        """
            Menu function which shows different operations admin can perform.
        """

        admin_choice = (input(PromptsConfig.ADMIN_PROMPT))

        while admin_choice != '8':
            
            match admin_choice:
                case '1':
                    add_user.add_new_user()
                case '2':
                    view_menu.view_vacc_status_menu()
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