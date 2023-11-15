import logging
from utils import utils
from config.prints import Prints
from config.prompts import PromptsConfig
from config.constants import Constants
from database import db_operations
from database.db_queries import DbConfig
from users.employee.emp_operations.dose_details import DoseDetails

logger = logging.getLogger('vaccination_details')

class VaccinationStatus:
    def __init__(self,user_id) -> None:
        self.user_id = user_id
        self.status = db_operations.db_fetchone_dao(DbConfig.FETCH_VACC_STATUS,(self.user_id,))[0]
        self.dose_obj = DoseDetails(user_id)

    def print_vacc_status(self):
            if self.status == 0:
                print(Prints.NOT_VACCINATED)
            elif self.status == 1:
                print(Prints.VACC_STATUS_1)
            else: 
                print(Prints.VACC_STATUS_2)

    @staticmethod
    def get_vaccine_name():
        while True:
                print(Prints.VACC_NAME)
                utils.vaccine_names()
                vaccine = input(PromptsConfig.GET_VACCINE)
                if vaccine == 'e' :
                    return None
                data = db_operations.db_fetchone_dao(DbConfig.FETCH_VACCINE_DETAILS,(vaccine,))
                if data == None:
                    print(Prints.ENTER_VALID_NAME)
                else:
                    break
        return vaccine


    def update_vacc_details_menu(self):
        while True:
            self.choice = (input(PromptsConfig.UPDATE_VACC_STATUS))
            if self.choice != '1' and self.choice != '2' and self.choice != '3':
                print(Prints.ENTER_VALID)
            else:
                break
        if self.choice == '3':
            return
        if int(self.choice) <= self.status:
            print(Prints.STATUS_ALREADY_UPTODATE)
            return
        self.update_vacc_status()
        

    def update_vacc_status(self):
        if int(self.choice) == 1 and self.status == 0 :
            self.vaccine = VaccinationStatus.get_vaccine_name()
            if self.vaccine == None : 
                print('Vaccine name is not selected!\n')
                return
            [return_value, date] = self.dose_obj.get_dose1_details()
            if return_value == True :
                self.dose_obj.update_dose1_details(self.vaccine)
            else :
                print(Prints.TRY_AGAIN)
                return
            
        elif int(self.choice) == 2 and self.status == 0 :
            self.vaccine = VaccinationStatus.get_vaccine_name()
            if self.vaccine == None : 
                print('Vaccine name is not selected!\n')
                return
            [return_value_1, date] = self.dose_obj.get_dose1_details()
            if return_value_1 == True : 
                print(Prints.ENTER_DOSE2_DETAILS)
                return_value_2 = self.dose_obj.get_dose2_details(date)
                if return_value_2 == True : 
                    self.dose_obj.update_dose1_details(self.vaccine)
                    self.dose_obj.update_dose2_details()
                else :
                    print(Prints.TRY_AGAIN)
                    return
            else : 
                print(Prints.TRY_AGAIN)
                return
            # db_operations.add_dose_details(DbConfig.ADD_DOSE_DETAILS,(self.user_id, self.vaccine, None, None))
        elif int(self.choice) == 2 and self.status == 1:
            return_value = self.dose_obj.get_dose2_details(self.dose_obj.dose_1_date)
            if return_value : 
                self.dose_obj.update_dose2_details()
            else :
                print(Prints.TRY_AGAIN)
                return
            
        db_operations.db_dao(DbConfig.UPDATE_VACC_STATUS,(int(self.choice), self.user_id,))
        self.status = int(self.choice)
        logger.info('Vaccination details update for employee ID: {id}'.format(id = self.user_id))
        print(Prints.STATUS_UPDATED)
            # if check_date_diff(dose_2_date):
            #     # db_operations.update_vacc_status(DbConfig.UPDATE_VACC_STATUS,(choice, user_id,))
            #     update_dose2_details(user_id)
            # else : 
            #     print("Enter valid date")
        
            # vaccine = get_vaccine_name()
            # db_operations.add_dose_details(DbConfig.ADD_DOSE_DETAILS,(user_id, vaccine, None, None))
            # update_dose1_details()
            # db_operations.add_dose_details(DbConfig.ADD_TO_ADMIN_APPROVAL, (user_id, dose_1_cid,))
            # if choice == 2:
            #     print(Prints.ENTER_DOSE2_DETAILS)
            #     update_dose2_details()
            #     if check_date_diff(dose_2_date):
            #         db_operations.update_vacc_status(DbConfig.UPDATE_VACC_STATUS,(choice, user_id,))
            #         return
            # db_operations.update_vacc_status(DbConfig.UPDATE_VACC_STATUS,(choice, user_id,))
            # status = choice