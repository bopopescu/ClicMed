import settings
import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
import os

class LevelFilter(logging.Filter):
    def __init__(self, low, high):
        self._low = low
        self._high = high
        logging.Filter.__init__(self)
    def filter(self, record):
        if self._low <= record.levelno <= self._high:
            return True
        return False

def init_log():

    create_log_directory()
    directory = get_log_directory()
    formatter_debug = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(module)s -- %(filename)s -- %(funcName)s --  %(message)s")
    formatter_error = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(module)s -- %(filename)s -- %(funcName)s --  %(message)s")
    formatter_warning = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(module)s -- %(filename)s -- %(funcName)s --  %(message)s")
    formatter_info = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")

    handler_error = logging.handlers.TimedRotatingFileHandler(os.path.join(directory, "user_mgmt_error.log"), when='d',  interval=1, backupCount=31, encoding="utf-8")
    handler_warning = logging.handlers.TimedRotatingFileHandler(os.path.join(directory, "user_mgmt_warning.log"), when='d',  interval=1, backupCount=31, encoding="utf-8")
    handler_info = logging.handlers.TimedRotatingFileHandler(os.path.join(directory, "user_mgmt_info.log"), when='d',  interval=1, backupCount=31, encoding="utf-8")
    handler_debug = logging.handlers.TimedRotatingFileHandler(os.path.join(directory, "user_mgmt_debug.log"), when='d',  interval=1, backupCount=31, encoding="utf-8")

    handler_error.setFormatter(formatter_error)
    handler_warning.setFormatter(formatter_warning)
    handler_info.setFormatter(formatter_info)
    handler_debug.setFormatter(formatter_debug)


    handler_error.addFilter(LevelFilter(40, 50))
    handler_warning.addFilter(LevelFilter(30, 30))
    handler_info.addFilter(LevelFilter(20, 20))
    handler_debug.addFilter(LevelFilter(10, 10))

    logger = logging.getLogger("ClicMed")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler_error)
    logger.addHandler(handler_warning)
    logger.addHandler(handler_info)
    logger.addHandler(handler_debug)
   

def create_log_directory():
    directory = get_log_directory()
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_log_directory():
    home = str(Path.home())
    directory = os.path.join(home, ".ClicMed")
    return directory