import logging
from utils.decorators import load_config
from config.Logs.logs import Logs
from authentication.auth import Auth
from database.db_creation import CreateDB

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = 'src\\config\\Logs\\logs.txt')

logger = logging.getLogger('main')

if __name__ == "__main__":
    
    @load_config
    def my_main():
        logger.info(Logs.WELCOME)
        CreateDB()
        Auth()

    my_main()
    