from utils import utils
from datetime import datetime
from config.prompts import PromptsConfig
from config.prints import Prints
from database.db_queries import DbConfig
from database import db_operations

class DoseDetails:
    def __init__(self,user_id) -> None:
        self.user_id = user_id
        
    def get_dose1_details(self):
        print(Prints.ENTER_DOSE1_DETAILS)
        # while True:
        self.dose_1_date = input(PromptsConfig.GET_DATE)
        if utils.date_validator(self.dose_1_date) == False:
            print(Prints.ENTER_VALID_DATE)
            return False
        elif utils.is_future_date(self.dose_1_date) == True:
            print(Prints.FUTURE_DATE_MSG)
            return False
        self.dose_1_cid = input(PromptsConfig.GET_DOSE1_CID)
        self.dose_2_date = None
        self.dose_2_cid = None
        return True

    def get_dose2_details(self):
        is_eligible_for_dose2 = utils.check_date_diff((datetime.now()).strftime("%d/%m/%Y"), self.dose_1_date)
        if is_eligible_for_dose2 == False:
            print(Prints.CANNOT_UPDATE_DOSE2)
            return
        # while True:
        print(Prints.ENTER_DOSE2_DETAILS)
        self.dose_2_date = input(PromptsConfig.GET_DATE)
        if utils.date_validator(self.dose_2_date) == False:
            print(Prints.ENTER_VALID_DATE)
            return False
        elif utils.check_date_diff(self.dose_2_date, self.dose_1_date) == False:
            print(Prints.DOSE2_DATE_INVALID)
            return False
        elif utils.is_future_date(self.dose_2_date) == True:
            print(Prints.FUTURE_DATE_MSG)
            return False  
        self.dose_2_cid = input(PromptsConfig.GET_DOSE2_CID)
        return True


    def update_dose1_details(self, vaccine):
        db_operations.db_dao(DbConfig.ADD_DOSE_DETAILS,(self.user_id, vaccine, self.dose_1_date, self.dose_1_cid, ))
        db_operations.db_dao(DbConfig.ADD_TO_ADMIN_APPROVAL, (self.user_id, self.dose_1_cid,))
        # db_operations.update_dose1_details(DbConfig.UPDATE_DOSE_DETAILS,(self.dose_1_date, self.dose_1_cid, self.user_id))
        # db_operations.update_dose1_details(DbConfig.UPDATE_ADMIN_APPROVAL, (self.dose_1_cid, self.user_id,))


    def update_dose2_details(self):  
        db_operations.db_dao(DbConfig.UPDATE_DOSE2_DETAILS,(self.dose_2_date, self.dose_2_cid, self.user_id,))
        db_operations.db_dao(DbConfig.UPDATE_ADMIN_APPROVAL2, (self.dose_2_cid, self.user_id,))