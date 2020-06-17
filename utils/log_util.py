import logging
import os
from datetime import datetime

def init_log(path=os.getcwd(), logger_name=''):
    file_name = logger_name + "_{:%Y-%m-%d_%H-%M-%S}".format(datetime.now()) + ".log"

    logging.captureWarnings(True)
    formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(process)d | %(message)s', "%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    if not os.path.exists(path + '/logs'):
        os.makedirs(path + '/logs')

    file_handler = logging.FileHandler(path + '/logs/' + file_name, 'w', 'utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger