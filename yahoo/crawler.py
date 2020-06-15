import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from utils.requests_util import RequestUtil
from utils.log_util import init_log, logging
from utils.base_crawler import BaseCrawler
from utils.database_util import DatabaseUtil
from table import User 

class Crawler(BaseCrawler):

    database = DatabaseUtil(table=User, path=os.getcwd(), file_name='yahoo')

    def __init__(self):
        super().__init__()
        # self.....

    def job(self, x):
        return [{
            'name': x
        }]

    def start_crawler(self, inputs):
        count = self.map(self.job, inputs)
        self.save()

if __name__ == "__main__":
    crawler = Crawler()
    crawler.start_crawler(['a', 'b', 'c', 'd', 'e', 'f', 'g'])