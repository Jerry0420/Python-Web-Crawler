#!/usr/local/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from utils.requests_util import RequestUtil
from utils.base_crawler import init_log, change_log_path, init_database, DataBaseType, Pool, Parser, Info, BaseCrawler
from table import GlobalWifi 

from bs4 import BeautifulSoup
import argparse

site_name = 'globalwifi'
main_page_url = "https://sim.globalwifi.com.tw/"

logger = init_log(site_name=site_name)

# database = init_database(fields=GlobalWifi, file_name=site_name)
# database = init_database(fields=['title'], database_type=DataBaseType.CSV, file_name=site_name)
# database = init_database(database_type=DataBaseType.JSON, file_name=site_name)

session = RequestUtil()

class Crawler(BaseCrawler):

    def __init__(self, process_num, site_name, session):
        super().__init__(process_num=process_num, site_name=site_name, session=session)

    def get_page(self, url):
        document = self.session.get(url)
        document = BeautifulSoup(document, Parser.LXML.value)
        contents = document.select('ul.boxify-container li.boxify-item.product-item')
        result = []
        for content in contents:
            title = content.select_one('div.title').text.strip()
            result.append({
                'title': title
            })
        logger.info('Got %s items', len(result))
        return result

    def loop_page(self, url):
        page = 1
        items_all = []
        failed_brand = None
        while True:
            try:
                items_per_page = self.get_page(url + '?page=' + str(page))
                items_all.extend(items_per_page)
                if len(items_per_page):
                    page += 1
                else:
                    break
            except Exception as error:
                logger.exception(error)
                break
        logger.info('Got %s of %s', len(items_per_page), url)
        return items_all

    def start_crawler(self, inputs):
        self.init_database(fields=GlobalWifi)
        pool = Pool(processes=self.process_num)
        try:
            all_next_info = self.map(pool, self.loop_page, inputs)
            self.save()
            logger.info('Saved %s items', self.total_count)
        except Exception as error:
            logger.exception(error)
        finally:
            self.save()
            self.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--processes", help="crawl with n processes", type=int, default=4)
    args = parser.parse_args()
    urls = ['https://sim.globalwifi.com.tw/products' for _ in range(20)]
    crawler = Crawler(process_num=args.processes, site_name=site_name, session=session)
    crawler.start_crawler(urls)