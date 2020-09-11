import logging
import os
from datetime import datetime
import fcntl
from logging.handlers import RotatingFileHandler
from shutil import copyfile
import platform

class MultiprocessingHandler(RotatingFileHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__lock_pool = {}
        self.__lock_filename = os.path.join(os.path.dirname(self.baseFilename, ), '.loglockfile')
        assert self.mode == 'a'

    def emit(self, record):
        """
        Emit a record.

        Output the record to the file, catering for rollover as described
        in doRollover().
        """
        f = None
        try:
            f = self.__lock_pool.get(os.getpid())
            if f == None:
                f = open(self.__lock_filename, 'wb')
                self.__lock_pool[os.getpid()] = f
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            logging.FileHandler.emit(self, record)
            if self.shouldRollover(record):
                self.doRollover()

        except Exception:
            self.handleError(record)
        finally:
            if f:
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)

    def rotate(self, source, dest):
        copyfile(source, dest)
        with open(source, 'wb'):
            pass

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
    file_name = site_name + ".log"
    file_path = path + '/logs/' + file_name
    m_file_handler = MultiprocessingHandler(filename=file_path, maxBytes=1024 * 1024, backupCount=1)
    m_file_handler.setFormatter(fmt=formatter)

    logger.addHandler(console_handler)
    logger.addHandler(m_file_handler)
    return logger

def creation_date(file_path):
    if platform.system() == 'Windows':
        return os.path.getctime(file_path)
    else:
        stat = os.stat(file_path)
        try:
            return stat.st_birthtime
        except AttributeError:
            return stat.st_ctime

def change_log_path(path=os.getcwd(), site_name=''):
    file_path = path + '/logs/' + site_name + ".log"
    if os.path.isfile(file_path):
        date_time = creation_date(file_path)
        date_time = datetime.fromtimestamp(date_time)
        str_time = date_time.strftime("%Y-%m-%d_%H-%M-%S")
        original_file_name = path + '/logs/' + site_name + "_{}".format(str_time) + ".log"
        os.rename(file_path, original_file_name)