import sys
import hashlib
import maskpass
import logging
from config.logs import Logs
from config.prints import Prints
from config.prompts import PromptsConfig
from config.constants import Constant_stmt
from users.admin import admin_menu
from utils import utils
from users.employee import employee_menu
from database.db_queries import DbConfig
from config.prompts import PromptsConfig
from database.db_connection import DatabaseConnection

logger = logging.getLogger('auth')

class Auth:
    def __init__(self) -> None:
        print(Prints.WELCOME_MSG)
        choice = int(input(PromptsConfig.LOGIN_PROMPT))
        while True:
            if choice == 1:
                user_id, role = self.login()
                if role == "Admin":
                    admin_menu.Admin(user_id)
                else:
                    employee_menu.Employee(user_id)
            elif choice == 2:
                sys.exit()
            else:
                print(Prints.ENTER_VALID)
            choice = input(PromptsConfig.LOGIN_PROMPT)
            

    def login(self):
        attempts = 3
        while attempts:
            self.username = input(PromptsConfig.GET_USERNAME)
            self.password = maskpass.askpass(prompt = PromptsConfig.GET_PWD)
            self.hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
            with DatabaseConnection('database\\vaccine_tracker.db') as connection:
                cursor = connection.cursor()
                user_info = (cursor.execute(DbConfig.USER_DATA,(self.username,))).fetchone()
                if user_info:
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
                self.change_default_pwd()
            return user_info[0], user_info[3]

    def change_default_pwd(self):
        while True:
            self.new_password = maskpass.askpass(prompt = PromptsConfig.NEW_PWD)
            if utils.pwd_validator(self.new_password) == False:
                print(Prints.ENTER_STRONG_PWD)
                continue
            self.confirm_password = maskpass.askpass(prompt = PromptsConfig.CONFIRM_NEW_PWD)
            if self.new_password != self.confirm_password:
                print(Prints.CONFIRM_PWD_NOT_MATCHED)
                continue
            else:
                self.hashed_password = hashlib.sha256(self.new_password.encode()).hexdigest()
                with DatabaseConnection('database\\vaccine_tracker.db') as connection:
                    cursor = connection.cursor()
                    cursor.execute(DbConfig.UPDATE_PWD, (self.hashed_password, self.username))
                break
