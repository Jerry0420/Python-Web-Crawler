#!/usr/local/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from utils.requests_util import RequestUtil
from utils.log_util import init_log, logging
from utils.base_crawler import BaseCrawler, Parser
from utils.database_util import init_database, DataBaseType
from table import Fragrantica

from bs4 import BeautifulSoup
import argparse
import json
from selenium import webdriver

site_name = 'fragrantica'
main_page_url = "https://www.fragrantica.com/"

logger = init_log(site_name=site_name)
database = init_database(fields=Fragrantica, file_name=site_name)
# database = init_database(fields=['title'], database_type=DataBaseType.CSV, file_name=site_name)
# database = init_database(database_type=DataBaseType.JSON, file_name=site_name)
session = RequestUtil()

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

    def collect_perfumers(self):
        # url = "https://www.fragrantica.asia/noses/"
        # document = self.session.get(url)
        # document = BeautifulSoup(document, Parser.LXML.value)
        # contents = document.select('div.cell.small-12.medium-4')
        # perfumers = set()
        # for content in contents:
        #     perfumers.add(content.a.text)
        # with open('perfumers.json','w') as f:
        #     json.dump(list(perfumers), f)
        # logger.info("Collected %s perfumers", len(perfumers))
        # return list(perfumers)

        url = "https://www.fragrantica.com/perfume/Chanel/Coco-Mademoiselle-611.html"
        # driver = webdriver.Firefox()
        # driver.get(url)
        # driver.close()

        document = self.session.get(url)
        document = BeautifulSoup(document.decode('utf-8', 'ignore'), Parser.HTMLPARSER.value)
        print(document)
        # contents = document.select('span.rtgNote')
        # print(contents)
        # for content in contents:
        #     print(content)


    def start_crawler(self):
        perfumers = self.collect_perfumers()
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--processes", help="crawl with n processes", type=int, default=4)
    args = parser.parse_args()
    crawler = Crawler(process_num=args.processes, session=session)
    crawler.start_crawler()