import yaml
from config.constants import Constants
from config.prints import Prints

FPATH = "config\\prompts.yml"

class PromptsConfig:

    @classmethod
    def load(cls):
        with open(FPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.ADMIN_PROMPT = data['ADMIN_PROMPT']
            cls.LOGIN_PROMPT = data['LOGIN_PROMPT']
            cls.GET_USERNAME = data['GET_USERNAME']
            cls.GET_PWD = data['GET_PWD']
            cls.NEW_PWD = data['NEW_PWD']
            cls.CONFIRM_NEW_PWD = data['CONFIRM_NEW_PWD']
            cls.ASSIGN_USERNAME = data['ASSIGN_USERNAME']
            cls.ASSIGN_DEFAULT_PWD = data['ASSIGN_DEFAULT_PWD']
            cls.GET_VACCINE = data['GET_VACCINE']
            cls.VALID_CHOICE = data['VALID_CHOICE']
            cls.ASK_USER_ID = data['ASK_USER_ID']
            cls.APPROVE_DETAILS_PROMPT = data['APPROVE_DETAILS_PROMPT']
            cls.ASK_APPROVAL_DOSE1 = data['ASK_APPROVAL_DOSE1']
            cls.ASK_APPROVAL_DOSE2 = data['ASK_APPROVAL_DOSE2']
            cls.GET_DATE = data['GET_DATE']
            cls.VALID_VACCINE = data['VALID_VACCINE']
            cls.VIEW_VACC_STATUS_PROMPT = data['VIEW_VACC_STATUS_PROMPT']
            cls.VACCINE_NAMES = data['VACCINE_NAMES']
            cls.EMPLOYEE_PROMPT = data['EMPLOYEE_PROMPT']
            cls.UPDATE_VACC_STATUS = data['UPDATE_VACC_STATUS']
            cls.GET_NAME = data['GET_NAME']
            cls.UPDATE_DETAILS_PROMPT1 = data['UPDATE_DETAILS_PROMPT1']
            cls.UPDATE_DETAILS_PROMPT2 = data['UPDATE_DETAILS_PROMPT2']
            cls.ENTER_GENDER = data['ENTER_GENDER']
            cls.GET_DOSE1_CID = data['GET_DOSE1_CID']
            cls.GET_DOSE2_CID = data['GET_DOSE2_CID']
            cls.ENTER_USERNAME = data['ENTER_USERNAME']