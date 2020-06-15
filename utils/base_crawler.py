from .database_util import DatabaseUtil
from multiprocessing import Pool

class BaseCrawler:

    database = None

    def __init__(self, process_num=3, logger=None, session):
        self.logger = logger
        self.session = session
        self.process_num = process_num
        self.collected_data = []

    def append(self, data):
        self.collected_data.extend(data)
        if len(self.collected_data) >= 1000:
            self.save()
            self.collected_data = []

    def save(self):
        try:
            self.__class__.database.save(self.collected_data)
        except Exception as error:
            pass
    
    def map(self, function, inputs):
        total_count = 0
        pool = Pool(processes=self.process_num)
        results = pool.imap_unordered(function, inputs)
        for result in results:
            total_count += len(result)
            self.append(result)
        pool.close()
        pool.join()
        return total_count