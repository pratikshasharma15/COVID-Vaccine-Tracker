import logging
from config.logs import Logs
from config.prints import Prints
from config.prompts import PromptsConfig
from config.constants import Constant_stmt
import authentication.auth as auth
from database.db_queries import DbConfig
from database.db_creation import create_db

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = 'utils\\logs.txt')

logger = logging.getLogger('main')


if __name__ == "__main__":
    DbConfig.load()
    PromptsConfig.load()
    Constant_stmt.load()
    Prints.load()
    Logs.load()
    logger.info(Logs.WELCOME)
    create_db()
    auth.Auth()