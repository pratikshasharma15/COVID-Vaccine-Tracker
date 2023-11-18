import maskpass
import hashlib
import logging
from utils import utils
from database import db_operations
from config.Prompts.prompts import PromptsConfig
from config.Prints.prints import Prints
from config.Queries.db_queries import DbConfig


logger = logging.getLogger('new_user')


def add_new_user():

    user_id = utils.generate_uuid()
    username = utils.input_valid_email()
    password = maskpass.askpass(prompt = PromptsConfig.ASSIGN_DEFAULT_PWD)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    db_operations.db_dao(DbConfig.ADD_USER, (user_id, username, hashed_password,))
    db_operations.db_dao(DbConfig.ADD_USER_DETAILS, (user_id, username))

    logger.info("New User Added!")
    print(Prints.USER_ADDED_SUCCESS)