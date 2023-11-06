import yaml
from config.constants import Constant_stmt
from config.prints import Prints

FPATH = "config\\logs.yml"

class Logs:

    @classmethod
    def load(cls):
        with open(FPATH, 'r') as f:
            data=yaml.safe_load(f)
            cls.WELCOME = data['WELCOME']
            cls.LOGIN_ATTEMPTS_EXCEEDED = data['LOGIN_ATTEMPTS_EXCEEDED']
            cls.SUCCESS_LOGIN = data['SUCCESS_LOGIN']
            cls.ADMIN_MSG = data['ADMIN_MSG']
            cls.EMPLOYEE_MSG = data['EMPLOYEE_MSG']
            