from .database_util import DatabaseUtil
from multiprocessing import Pool
from enum import Enum
import logging

logger = logging.getLogger()

class Parser(Enum):
    LXML = 'lxml'
    HTMLPARSER = 'html.parser'
    HTML5LIB = 'html5lib'

class BaseCrawler:

    database = None

    def __init__(self, process_num=4, session=None):
        self.process_num = process_num
        self.session = session
        self.collected_data = []

    def append(self, data):
        self.collected_data.extend(data)
        if len(self.collected_data) >= 1000:
            self.save()

    def save(self):
        logger.info("Saved %s into database", len(self.collected_data))
        self.__class__.database.save(self.collected_data)
        self.collected_data = []
    
    def map(self, function, inputs):
        total_count = 0
        pool = Pool(processes=self.process_num)
        results = pool.imap_unordered(function, inputs)
        for result in results:
            if len(result):
                total_count += len(result)
                self.append(result)
        return total_count