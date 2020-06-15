import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from utils.requests_util import RequestUtil
from utils.log_util import init_log, logging
from utils.base_crawler import BaseCrawler
from table import database

class Crawler(BaseCrawler):

    database = database

    def __init__(self):
        super().__init__()
        # self.....

    def job(self, x):
        return [x + 'kerker']

    def start_crawler(self, inputs):
        count = self.map(self.job, inputs)
        print(count)

if __name__ == "__main__":
    crawler = Crawler()
    crawler.start_crawler(['a', 'b', 'c', 'd', 'e', 'f', 'g'])