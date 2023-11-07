import re
import shortuuid
from datetime import datetime
from tabulate import tabulate
from database import db_operations
from config.prints import Prints
from config.prompts import PromptsConfig
from config.constants import Constants
from utils.exceptions import UsernameAlreadyExistsError
from database.db_queries import DbConfig


def generate_uuid():
        user_id = int(shortuuid.ShortUUID("123456789").random(4))
        return user_id

def generate_valid_email():
    while True:
        email=input(PromptsConfig.ENTER_USERNAME)
        pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,7}$'
        if(re.match(pattern, email)):
            try:
                if(db_operations.db_fetchall_dao(DbConfig.FETCH_AUTH_DATA,(email.lower(),))):
                   raise UsernameAlreadyExistsError("Username already present!")
                return email
            except UsernameAlreadyExistsError as ue:
                print(ue.msg)
        else:
             print(Prints.ENTER_VALID_EMAIL)           

def pwd_validator(password):
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    if re.match(pattern,password) is not None:
        return True
    else:
        return False
       
def date_validator(date):
    pattern = '(0[1-9]|[12][0-9]|3[01])(\/)(0[1-9]|1[0,1,2])(\/)(20)((19)|(2)[01234])'
    if re.fullmatch(pattern,date):
        return True
    else:
        return False
    
def convert_to_datetime_obj(date):
    date = datetime.strptime(str(date), "%d/%m/%Y")
    return date

def vaccine_names():
    data = db_operations.db_fetchall_dao(DbConfig.FETCH_VACCINE_NAME)
    for i,vacc in enumerate(data, start=1):
        print(i,vacc[0])
    print('\n')

def check_date_diff(date_1, date_2):
    today_date = convert_to_datetime_obj(date_1)
    dose_1_date = convert_to_datetime_obj(date_2)
    date_diff = today_date - dose_1_date
    days = int((date_diff).days)
    if days > 60:
        return True
    else:
        return False

def is_future_date(date):
    date = convert_to_datetime_obj(date)
    today_date = convert_to_datetime_obj((datetime.now()).strftime("%d/%m/%Y"))
    if date > today_date : 
        return True
    else : 
        return False
    
def is_acceptable_id(id):
    db_id_1 = db_operations.db_fetchone_dao('SELECT * FROM dose_details WHERE dose_1_cid = ?',(id, ))
    db_id_2 = db_operations.db_fetchone_dao('SELECT * FROM dose_details WHERE dose_2_cid = ?',(id, ))
    if db_id_1 == None:
        if db_id_2 == None:
            return True
        else :
            return False
    else:
        return False
    
def cid_validator(id):
    pattern = '[a-zA-Z]+[0-9]+'
    if re.match(pattern,id):
        return True
    else:
        return False