import yaml
from config.constants import Constant_stmt

FPATH = "config\\prints.yml"

class Prints:

    @classmethod
    def load(cls):
        with open(FPATH,'r') as f:
            data=yaml.safe_load(f)
            cls.WELCOME_MSG = data['WELCOME_MSG']
            cls.ENTER_VALID = data['ENTER_VALID']
            cls.NOT_VACCINATED = data['NOT_VACCINATED']
            cls.VACC_STATUS_1 = data['VACC_STATUS_1']
            cls.VACC_STATUS_2 = data['VACC_STATUS_2']
            cls.REMINDER_1 = data['REMINDER_1']
            cls.REMINDER_2 = data['REMINDER_2']
            cls.REMINDER_3 = data['REMINDER_3']
            cls.REMINDER_4 = data['REMINDER_4']
            cls.DOSE2_DATE_INVALID = data['DOSE2_DATE_INVALID']
            cls.ENTER_VALID_DATE = data['ENTER_VALID_DATE']
            cls.CANNOT_UPDATE_DOSE2 = data['CANNOT_UPDATE_DOSE2']
            cls.ENTER_DOSE2_DETAILS = data['ENTER_DOSE2_DETAILS']
            cls.STATUS_UPDATED = data['STATUS_UPDATED']
            cls.ENTER_VALID_NAME = data['ENTER_VALID_NAME']
            cls.NO_VACC_USER = data['NO_VACC_USER']
            cls.STATUS_ALREADY_UPTODATE = data['STATUS_ALREADY_UPTODATE']
            cls.VACC_NAME = data['VACC_NAME']
            cls.TRY_AGAIN = data['TRY_AGAIN']
            cls.ENTER_DOSE1_DETAILS = data['ENTER_DOSE1_DETAILS']
            cls.FUTURE_DATE_MSG = data['FUTURE_DATE_MSG']
            cls.APPROVAL_SUCCESS = data['APPROVAL_SUCCESS']
            cls.DATA_NOT_FOUND = data['DATA_NOT_FOUND']
            cls.USER_ADDED_SUCCESS = data['USER_ADDED_SUCCESS']
            cls.NO_INFO_FOR_DATE = data['NO_INFO_FOR_DATE']
            cls.CHANGE_DEFAULT_PWD = data['CHANGE_DEFAULT_PWD']
            cls.CONFIRM_PWD_NOT_MATCHED = data['CONFIRM_PWD_NOT_MATCHED']
            cls.INVALID_CREDENTIALS = data['INVALID_CREDENTIALS']
            cls.ATTEMPTS_LEFT = data['ATTEMPTS_LEFT']
            cls.ENTER_VALID_EMAIL = data['ENTER_VALID_EMAIL']
            cls.SHOW_STATUS_MEANING = data['SHOW_STATUS_MEANING']
            cls.VACCINE_NO_USER = data['VACCINE_NO_USER']
            cls.ENTER_STRONG_PWD = data['ENTER_STRONG_PWD']


            # cls.NEWLINE = data['NEWLINE']
            # cls.DB_NAME = data['DB_NAME']
            # cls.EMP_MENU_FILE = data['EMP_MENU_FILE']
            # cls.AUTH_FILE = data['AUTH_FILE']
            # cls.EXIT = data['EXIT']
            # cls.MALE = data['MALE']
            # cls.FEMALE = data['FEMALE']
            # cls.ADMIN_MENU_FILE = data['ADMIN_MENU_FILE']
            # cls.APPROVAL_HEADER = data['APPROVAL_HEADER']
            # cls.YES = data['YES']
            # cls.FPATH_DB_QUERIES = data['FPATH_DB_QUERIES']
            # cls.READ_FILE = data['READ_FILE']
            # cls.FPATH_PROMPTS = data['FPATH_PROMPTS']
            # cls.FPATH_PRINTS = data['FPATH_PRINTS']
            # cls.FPATH_LOGS = data['FPATH_LOGS']
            # cls.ADMIN = data['ADMIN']
            # cls.FALSE = data['FALSE']
            # cls.MAIN_FILE = data['MAIN_FILE']
            # cls.LOGS_FILE_PATH = data['LOGS_FILE_PATH']
            # cls.MAIN = data['MAIN']
            # cls.USERNAME_PRESENT_MSG = data['USERNAME_PRESENT_MSG']
            # cls.PWD_PATTERN = data['PWD_PATTERN']
            # cls.EMAIL_PATTERN = data['EMAIL_PATTERN']
            # cls.DATE_PATTERN = data['DATE_PATTERN']