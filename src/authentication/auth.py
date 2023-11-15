import sys
import hashlib
import maskpass
import logging
from os import system
from authentication.default_pwd import change_default_pwd
from config.prints import Prints
from config.prompts import PromptsConfig
from config.constants import Constants
from users.admin import admin_menu
from users.employee import employee_menu
from database.db_queries import DbConfig
from config.prompts import PromptsConfig
from database import db_operations


logger = logging.getLogger('auth')


class Auth:
    def __init__(self) -> None:
        while True:
            choice = (input(PromptsConfig.LOGIN_PROMPT))
            if choice == '1':
                system('cls')
                print("**********WELCOME TO LOGIN SECTION*********")
                user_id, role = self.login()
                if role == "Admin":
                    admin_menu.Admin(user_id)
                else:
                    employee_menu.Employee(user_id)
            elif choice == '2':
                sys.exit(0)
            else:
                print(Prints.ENTER_VALID)
            
    def login(self):
        attempts = 3
        while attempts:
            self.username = input(PromptsConfig.GET_USERNAME)
            self.password = maskpass.askpass(prompt = PromptsConfig.GET_PWD)
            self.hashed_password = hashlib.sha256(self.password.encode()).hexdigest()

            user_info = db_operations.db_fetchone_dao(DbConfig.USER_DATA,(self.username.lower(),))

            if user_info is not None:
                db_pwd = user_info[2]
                if db_pwd == self.hashed_password:
                    break

            print(Prints.INVALID_CREDENTIALS)
            attempts -= 1
            print(Prints.ATTEMPTS_LEFT.format(attempts = attempts))
            continue

        if attempts == 0:
            sys.exit()
        else:
            if user_info[4] == "False" :
                print(Prints.CHANGE_DEFAULT_PWD)
                change_default_pwd(self.username)
            return user_info[0], user_info[3]