from tabulate import tabulate
from database.db_queries import DbConfig
from config.prompts import PromptsConfig
from config.prints import Prints
from config.constants import Constant_stmt
from database import db_operations


def approval_prompt():
    choice = int(input(PromptsConfig.APPROVE_DETAILS_PROMPT))
    while choice != 3:
        if choice == 1:
            approve_details(choice)
        elif choice == 2:
            approve_details(choice)
        else:
            choice = input(PromptsConfig.VALID_CHOICE)
        choice = int(input(PromptsConfig.APPROVE_DETAILS_PROMPT))


def approve_details(dose_num):
    if dose_num == 1 :
        data = db_operations.db_fetchall_dao(DbConfig.FETCH_1APPROVAL_DATA)
    else : 
        data = db_operations.db_fetchall_dao(DbConfig.FETCH_2APPROVAL_DATA)    
    if data:
        print(tabulate(data, headers= ["User ID", "Dose-1 CID", "Approved", "Dose-2 CID", "Approved"]))
        user_id = int(input(PromptsConfig.ASK_USER_ID))
        if dose_num == 1 :
            response = input(PromptsConfig.ASK_APPROVAL_DOSE1)
        else : 
            response = input(PromptsConfig.ASK_APPROVAL_DOSE2)
        if response.upper() == 'Y':
            if dose_num == 1 :
                row = db_operations.db_dao(DbConfig.APPROVE_DOSE_1,(user_id,))
            else :
                row = db_operations.db_dao(DbConfig.APPROVE_DOSE_2,(user_id,))
            # if row:
            print(Prints.APPROVAL_SUCCESS)
            # else:
            #     print(Prints.DATA_NOT_FOUND)
    else:
        print(Prints.DATA_NOT_FOUND) 

        
def view_approved_details():
    data = db_operations.db_fetchall_dao(DbConfig.APPROVED_DATA)
    print(tabulate(data, headers=["User ID", "Dose-1 CID", "Approved", "Dose-2 CID", "Approved"]))