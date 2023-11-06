from config.prompts import PromptsConfig
from config.prints import Prints
from config.constants import Constant_stmt
from database.db_queries import DbConfig
from database import db_operations


class PersonalDetails:
    def __init__(self,user_id) -> None:
        self.user_id = user_id
        self.update_name()
        self.update_gender()

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