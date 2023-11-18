import logging
from config.Prompts.prompts import PromptsConfig
from config.Prints.prints import Prints
from config.Constants.constants import Constants
from config.Queries.db_queries import DbConfig
from database import db_operations

logger = logging.getLogger('profile')

class Profile:
    def __init__(self,user_id) -> None:
        self.user_id = user_id
        self.update_name()
        self.update_gender()
        logger.info('Profile Updated!')


    def update_name(self):
        name = input(PromptsConfig.GET_NAME)
        db_operations.db_dao(DbConfig.UPDATE_NAME,(name, self.user_id))


    def update_gender(self):
        while(True):
            gender = input(PromptsConfig.ENTER_GENDER)
            if gender.lower() == "male" or gender.lower() == "female":
                break
            print(Prints.ENTER_VALID)
        db_operations.db_dao(DbConfig.UPDATE_GENDER,(gender, self.user_id,))

    