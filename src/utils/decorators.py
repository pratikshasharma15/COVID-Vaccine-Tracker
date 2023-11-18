import logging
import functools
from config.Logs.logs import Logs
from config.Prints.prints import Prints
from config.Prompts.prompts import PromptsConfig
from config.Queries.db_queries import DbConfig
from config.Constants.constants import Constants


def load_config(func):
    def function():
        # Load all config files
        DbConfig.load()
        PromptsConfig.load()
        Constants.load()
        Prints.load()
        Logs.load()
        func()
    return function


def log_function_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed successfully.")
        return result
    return wrapper