import logging
import os
from datetime import datetime

now_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def init_log(path=os.getcwd(), site_name=''):
    logging.captureWarnings(True)
    
    logger = logging.getLogger()
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(process)d | %(filename)s:%(lineno)d | %(message)s', "%Y-%m-%d %H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    if not os.path.exists(path + '/logs'):
        os.makedirs(path + '/logs')
    file_name = site_name + "_{}".format(now_str) + ".log"
    file_handler = logging.FileHandler(path + '/logs/' + file_name, 'w', 'utf-8')
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger