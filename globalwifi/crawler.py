#!/usr/local/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from utils.requests_util import RequestUtil
from utils.log_util import init_log, logging
from utils.base_crawler import BaseCrawler
from utils.database_util import init_database
from table import GlobalWifi 

from bs4 import BeautifulSoup
import argparse

site_name = 'globalwifi'
main_page_url = "https://sim.globalwifi.com.tw/"

logger = init_log(logger_name=site_name)
database = init_database(table=GlobalWifi, file_name=site_name, logger=logger)
session = RequestUtil(logger=logger)

class Crawler(BaseCrawler):

    database = database

    def __init__(self, process_num, session):
        super().__init__(process_num=process_num, session=session)

    def job(self, url):
        document = self.session.get(url)
        document = BeautifulSoup(document, 'lxml')
        contents = document.select('ul.boxify-container li.boxify-item.product-item')
        result = []
        for content in contents:
            title = content.select_one('div.title').text.strip()
            result.append({
                'title': title
            })
        logger.info('Got %s items', len(result))
        return result

    def start_crawler(self, inputs):
        try:
            count = self.map(self.job, inputs)
            logger.info('Saved %s items', count)
            self.save()
        except Exception as error:
            logger.exception(error)
            self.save()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--processes", help="crawl with n processes", type=int, default=4)
    args = parser.parse_args()
    crawler = Crawler(process_num=args.processes, session=session)
    crawler.start_crawler([
        'https://sim.globalwifi.com.tw/categories/5b307bf98d1db966a70002d8',
        'https://sim.globalwifi.com.tw/categories/%E7%86%B1%E9%96%80%E5%95%86%E5%93%81',
        'https://sim.globalwifi.com.tw/categories/oceania-sim',
        'https://sim.globalwifi.com.tw/categories/travel-accessories'
    ])