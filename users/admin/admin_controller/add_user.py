import maskpass
import hashlib
from utils import utils
from database import db_operations
from config.prompts import PromptsConfig
from config.prints import Prints
from database.db_queries import DbConfig


def add_new_user():
    user_id = utils.generate_uuid()
    username = utils.generate_valid_email()
    password = maskpass.askpass(prompt = PromptsConfig.ASSIGN_DEFAULT_PWD)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    db_operations.db_dao(DbConfig.ADD_USER, (user_id, username, hashed_password,))
    db_operations.db_dao(DbConfig.ADD_USER_DETAILS, (user_id, username))
    print(Prints.USER_ADDED_SUCCESS)