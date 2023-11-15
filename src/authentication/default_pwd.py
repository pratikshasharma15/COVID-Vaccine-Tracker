import maskpass
import hashlib
from utils import utils
from database import db_operations
from database.db_queries import DbConfig
from config.prints import Prints
from config.prompts import PromptsConfig


def change_default_pwd(username):
        """ 
        Change default password on first time login.
        """
        while True:
            new_password = maskpass.askpass(prompt = PromptsConfig.NEW_PWD)

            if utils.pwd_validator(new_password) == False:
                print(Prints.ENTER_STRONG_PWD)
                continue

            confirm_password = maskpass.askpass(prompt = PromptsConfig.CONFIRM_NEW_PWD)

            if new_password != confirm_password:
                print(Prints.CONFIRM_PWD_NOT_MATCHED)
                continue
            else:
                hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                db_operations.db_dao(DbConfig.UPDATE_PWD,(hashed_password, username))
                break