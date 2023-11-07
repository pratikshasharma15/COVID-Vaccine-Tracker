import yaml

FPATH='config/constants.yml'

class Constants:

    @classmethod
    def load(cls):
        with open(FPATH,'r') as f:
            data=yaml.safe_load(f)
            cls.DB_NAME = data['DB_NAME']
            cls.MAIN_FILE = data['MAIN_FILE']
            cls.ADMIN_MENU = data['ADMIN_MENU']
            cls.EXIT = data['EXIT']
            cls.NEWLINE = data['NEWLINE']