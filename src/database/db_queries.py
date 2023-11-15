import yaml
from config.prints import Prints

FPATH = "src\\database\\db_queries.yml"

class DbConfig:

    @classmethod
    def load(cls):
        with open(FPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.CREATE_AUTH_TABLE = data['CREATE_AUTH_TABLE']
            cls.CREATE_USER_DETAILS_TABLE = data['CREATE_USER_DETAILS_TABLE']
            cls.CREATE_DOSE_DETAILS_TABLE = data['CREATE_DOSE_DETAILS_TABLE']
            cls.CREATE_ADMIN_APPROVAL_TABLE = data['CREATE_ADMIN_APPROVAL_TABLE']
            cls.CREATE_VACCINE_TABLE = data['CREATE_VACCINE_TABLE']
            cls.USER_DATA = data['USER_DATA']
            cls.UPDATE_PWD = data['UPDATE_PWD']
            cls.ADD_USER = data['ADD_USER']
            cls.FETCH_BY_DOSE = data['FETCH_BY_DOSE']
            cls.FETCH_BY_VACCINE = data['FETCH_BY_VACCINE']
            cls.FETCH_BY_DOSE1_DATE = data['FETCH_BY_DOSE1_DATE']
            cls.FETCH_BY_DOSE2_DATE = data['FETCH_BY_DOSE2_DATE']
            cls.ADD_VACCINE = data['ADD_VACCINE']
            cls.APPROVE_DOSE_1 = data['APPROVE_DOSE_1']
            cls.APPROVE_DOSE_2 = data['APPROVE_DOSE_2']
            cls.FETCH_1APPROVAL_DATA = data['FETCH_1APPROVAL_DATA']
            cls.FETCH_2APPROVAL_DATA = data['FETCH_2APPROVAL_DATA']
            cls.FETCH_VACC_STATUS = data['FETCH_VACC_STATUS']
            cls.FETCH_DOSE_DETAILS = data['FETCH_DOSE_DETAILS']
            cls.FETCH_VACCINE_DETAILS = data['FETCH_VACCINE_DETAILS']
            cls.ADD_DOSE_DETAILS = data['ADD_DOSE_DETAILS']
            cls.ADD_TO_ADMIN_APPROVAL = data['ADD_TO_ADMIN_APPROVAL']
            cls.UPDATE_VACC_STATUS = data['UPDATE_VACC_STATUS']
            cls.UPDATE_DOSE_DETAILS = data['UPDATE_DOSE_DETAILS']
            cls.UPDATE_ADMIN_APPROVAL = data['UPDATE_ADMIN_APPROVAL']
            cls.UPDATE_DOSE2_DETAILS = data['UPDATE_DOSE2_DETAILS']
            cls.UPDATE_ADMIN_APPROVAL2 = data['UPDATE_ADMIN_APPROVAL']
            cls.SELECT_DOSE1_DATE = data['SELECT_DOSE1_DATE']
            cls.UPDATE_NAME = data['UPDATE_NAME']
            cls.UPDATE_GENDER = data['UPDATE_GENDER']
            cls.APPROVED_DATA = data['APPROVED_DATA']
            cls.ADD_USER_DETAILS = data['ADD_USER_DETAILS']
            cls.FETCH_AUTH_DATA = data['FETCH_AUTH_DATA']
            cls.FETCH_VACCINE_NAME = data['FETCH_VACCINE_NAME']
            cls.FETCH_USER_DETAILS = data['FETCH_USER_DETAILS']