from .database_util import DatabaseUtil
from multiprocessing import Pool

class BaseCrawler:

    database = None

    def __init__(self, process_num=3, logger=None):
        self.logger = logger
        self.process_num = process_num
        self.collected_data = []

    def append(self, data):
        self.collected_data.extend(data)
        if len(self.collected_data) >= 1000:
            self.save()
            self.collected_data = []

    def __del__(self):
        self.save()

    def save(self):
        self.__class__.database.save(self.collected_data)
    
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