import yaml

FPATH='config\\constants.yml'

class Constant_stmt:

    @classmethod
    def load(cls):
        with open(FPATH,'r') as f:
            data=yaml.safe_load(f)
            