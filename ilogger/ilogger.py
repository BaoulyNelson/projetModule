import logging
import os
from datetime import datetime

LOG_DIR = "logs"
ERROR_LOG_FILE = "error.log"
WARNING_LOG_FILE = "warning.log"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

error_logger = logging.getLogger("error_logger")
warning_logger = logging.getLogger("warning_logger")

error_handler = logging.FileHandler(os.path.join(LOG_DIR, ERROR_LOG_FILE))
warning_handler = logging.FileHandler(os.path.join(LOG_DIR, WARNING_LOG_FILE))

error_logger.addHandler(error_handler)
warning_logger.addHandler(warning_handler)

def log(message, level):
    if len(message) > 100:
        raise ValueError("Mesaj la pa dwe depase 100 karakte")

    if level == "ERROR":
        error_logger.error(message)
    elif level == "WARNING":
        warning_logger.warning(message)
    else:
        raise ValueError("Nivo log la envalid. itilize 'ERROR' oubyen 'WARNING'.")
    

def get_logs(log_level):
    if log_level == "ERROR":
        log_file = os.path.join(LOG_DIR, ERROR_LOG_FILE)
    elif log_level == "WARNING":
        log_file = os.path.join(LOG_DIR, WARNING_LOG_FILE)
    else:
        raise ValueError("Nivo log la envalid. itilize 'ERROR' oubyen 'WARNING'.")

    with open(log_file, "r") as file:
        return file.readlines()
