#!/usr/local/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from utils.async_requests_util import AsyncRequestUtil
from utils.base_crawler import init_log, change_log_path, init_database, DataBaseType, Pool, Parser, Info, BaseCrawler
from table import GlobalWifi 

from bs4 import BeautifulSoup
import argparse
import asyncio
import time

site_name = 'globalwifi'
main_page_url = "https://sim.globalwifi.com.tw/"

logger = init_log(site_name=site_name)
# database = init_database(database_type=DataBaseType.JSON, file_name=site_name)
# database = init_database(fields=GlobalWifi, file_name=site_name)
session = AsyncRequestUtil()

def get_page(input):
        document, info = input
        result = []
        if not document: return result

        document = BeautifulSoup(document, Parser.LXML.value)
        contents = document.select('ul.boxify-container li.boxify-item.product-item')
        for content in contents:
            title = content.select_one('div.title').text.strip()
            result.append({
                'title': title
            })
        logger.info('Got %s items', len(result))
        
        if result:
            info.next_info['page'] = info.next_info['page'] + 1
        else:
            info = Info(current_info=None, next_info=None, retry_info=None)
        return result, info

class AsyncCrawler(BaseCrawler):
    
    def __init__(self, process_num, site_name, session, loop):
        super().__init__(process_num=process_num, site_name=site_name, session=session, loop=loop)

    async def request_page(self, info):
        next_info = info.next_info
        url = next_info['url']
        page = next_info['page']
        url = url + '?page=' + str(page)
        response = await self.session.get(url)
        return response, info

    def start_crawler(self, inputs):
        self.init_database(fields=GlobalWifi)
        pool = Pool(processes=self.process_num)
        all_next_info = [
            self.request_page(
                Info(current_info=None, next_info={ 'url': url, 'page': 1 }, retry_info=None)
                ) 
            for url in inputs
            ]
        while True:
            try:
                done_response, pending = self.loop.run_until_complete(asyncio.wait(all_next_info))
                all_page_dom = [response.result() for response in done_response]
                all_next_info = self.map(pool, get_page, all_page_dom)
                all_next_info = [self.request_page(Info(current_info=None, next_info=next_info, retry_info=None)) for next_info in all_next_info if next_info]
                if not all_next_info:
                    break
            except Exception as error:
                logger.exception(error)
                break
        self.save()
        self.loop.run_until_complete(self.session.close())
        self.close()
        logger.info('Saved %s items', self.total_count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--processes", help="crawl with n processes", type=int, default=4)
    args = parser.parse_args()

    urls = ['https://sim.globalwifi.com.tw/products' for _ in range(10)]
    
    async_crawler = AsyncCrawler(
        process_num=args.processes,
        site_name=site_name,
        session=session,
        loop=asyncio.get_event_loop()
        )

    async_crawler.start_crawler(urls)