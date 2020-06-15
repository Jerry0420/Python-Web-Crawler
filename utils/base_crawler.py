from .database_util import DatabaseUtil
from multiprocessing import Pool

class BaseCrawler:

    def __init__(self, process_num=3, path='', table=None, file_name='', logger=None):
        self.logger = logger
        if not table:
            # json....
            self.database = None
        else:
            self.database = DatabaseUtil(table=table, path=path, file_name=file_name, logger=self.logger)
        self.collected_data = []
        self.process_num = process_num

    def append(self, data):
        self.collected_data.extend(data)
        if len(self.collected_data) >= 5000:
            self.save()
            self.collected_data = []

    def save(self):
        self.database.save(self.collected_data)
    
    def map(self, function, inputs):
        total_count = 0
        pool = Pool(processes=self.process_num)
        results = pool.imap_unordered(function, inputs)
        for result in results:
            total_count += len(result)
            self.append(result)
        return total_count