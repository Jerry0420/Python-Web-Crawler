from .database_util import init_database, DataBaseType
from .log_util import init_log, logging

from multiprocessing import Pool
from enum import Enum
import json
from collections import namedtuple
import time

logger = logging.getLogger(__name__)

class Parser(Enum):
    LXML = 'lxml'
    HTMLPARSER = 'html.parser'
    HTML5LIB = 'html5lib'

Info = namedtuple('Info', ['current_info', 'next_info', 'retry_info'])

class BaseCrawler:

    database = None

    def __init__(self, process_num=4, session=None, loop=None):
        self.process_num = process_num
        self.session = session
        self.collected_data = []
        self.retry_info = []
        self.total_count = 0
        self.loop = loop

    def append(self, data):
        self.collected_data.extend(data)
        if len(self.collected_data) >= 1000:
            self.save()

    def save(self):
        self.total_count += len(self.collected_data)
        logger.info("Saved %s into database", len(self.collected_data))
        self.__class__.database.save(self.collected_data)
        self.collected_data = []

    def save_retry_info(self):
        with open('retry_info.json', 'w', encoding='utf-8') as f:
            json.dump(self.retry_info, f, ensure_ascii=False)

    def close(self):
        self.loop.stop()
        self.loop.run_forever()
        self.loop.close()

    def map(self, pool, function, inputs):
        all_next_info = []
        results = pool.imap_unordered(function, inputs)
        for result in results:
            if isinstance(result, tuple):
                result, info = result
                if info:
                    if info.retry_info:
                        self.retry_info.append(info.retry_info)
                    if info.next_info:
                        all_next_info.append(info.next_info)
            if len(result):
                self.append(result)
        if self.retry_info:
            self.save_retry_info()
        return all_next_info