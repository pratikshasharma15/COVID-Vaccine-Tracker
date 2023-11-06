from utils import utils
from config.prints import Prints
from config.prompts import PromptsConfig
from config.constants import Constant_stmt
from database import db_operations
from database.db_queries import DbConfig
from users.employee.emp_controller.dose_details import DoseDetails

class VaccinationStatus:
    def __init__(self,user_id) -> None:
        self.user_id = user_id
        self.status = db_operations.db_fetchone_dao(DbConfig.FETCH_VACC_STATUS,(self.user_id,))[0]
        self.dose_obj = DoseDetails(user_id)
    # def get_vacc_status(user_id):
    #     status = db_operations.fetch_status(DbConfig.FETCH_VACC_STATUS,(user_id,))
    #     return status

    def print_vacc_status(self):
            # status = get_vacc_status(user_id)
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
                data = db_operations.db_fetchone_dao(DbConfig.FETCH_VACCINE_DETAILS,(vaccine,))
                if data == None:
                    print(Prints.ENTER_VALID_NAME)
                elif vaccine == 'e':
                    return
                else:
                    break
        return vaccine

    def update_vacc_status(self):
        while True:
            choice = int(input(PromptsConfig.UPDATE_VACC_STATUS))
            if choice != 1 and choice != 2 and choice != 3:
                print(Prints.ENTER_VALID)
            else:
                break
        if choice == 3:
            return
        if choice <= self.status:
            print(Prints.STATUS_ALREADY_UPTODATE)
            return
        
        if choice == 1 and self.status == 0 :
            self.vaccine = VaccinationStatus.get_vaccine_name()
            return_value = self.dose_obj.get_dose1_details()
            if return_value == True :
                self.dose_obj.update_dose1_details(self.vaccine)
            else :
                print(Prints.TRY_AGAIN)
                return
            
        elif choice == 2 and self.status == 0 :
            self.vaccine = VaccinationStatus.get_vaccine_name()
            return_value_1 = self.dose_obj.get_dose1_details()
            if return_value_1 == True : 
                print(Prints.ENTER_DOSE2_DETAILS)
                return_value_2 = self.dose_obj.get_dose2_details()
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
        elif choice == 2 and self.status == 1:
            return_value = self.dose_obj.get_dose2_details()
            if return_value : 
                self.dose_obj.update_dose2_details()
            else :
                print(Prints.TRY_AGAIN)
                return
        db_operations.db_dao(DbConfig.UPDATE_VACC_STATUS,(choice, self.user_id,))
        self.status = choice
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
        
