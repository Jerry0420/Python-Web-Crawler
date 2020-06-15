import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from utils.requests_util import RequestUtil
from utils.log_util import init_log, logging
from utils.base_crawler import BaseCrawler
from table import User

class Crawler(BaseCrawler):
    def __init__(self):
        super().__init__(path=os.getcwd(), table=User, file_name='yahoo')
        # self.....

    def job(self, x):
        return [x + 'kerker']

    def start_crawler(self, inputs):
        count = self.map(self.job, inputs)
        print(count)
        print(self.collected_data)

if __name__ == "__main__":
    crawler = Crawler()
    crawler.start_crawler(['a', 'b', 'c'])