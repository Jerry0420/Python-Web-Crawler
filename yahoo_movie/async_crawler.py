#!/usr/local/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from utils.async_requests_util import AsyncRequestUtil
from utils.base_crawler import init_log, init_database, DataBaseType, Pool, Parser, Info, BaseCrawler
from table import YahooMovie

from bs4 import BeautifulSoup
import argparse
import asyncio

site_name = 'yahoo_movie'
main_page_url = "https://movies.yahoo.com.tw/index.html"

logger = init_log(site_name=site_name)
database = init_database(database_type=DataBaseType.JSON, file_name=site_name)
# session = AsyncRequestUtil()

def split_chunk(list, n=3):
    for i in range(0, len(list), n):
        yield list[i: i + n]

def get_page(document):
    result = {}
    if not document: return []
    document = BeautifulSoup(document, Parser.LXML.value)
    #url, id
    url = document.select_one('meta[property="og:url"]')
    movie_intro_info_r = document.select_one(".movie_intro_info_r")

    try:
        url = url['content']
        if '/id=' not in url: raise
        movie_id = int(url.split('=')[-1])
    except Exception as error:
        return []
    
    

    # # for content in contents:
    # #     title = content.select_one('div.title').text.strip()
    # #     result.append({
    # #         'title': title
    # #     })
    
    # logger.info('Got %s', result)
    return [result]

# class AsyncCrawler(BaseCrawler):
    
#     database = database
    
#     def __init__(self, process_num, session, loop):
#         super().__init__(process_num=process_num, session=session, loop=loop)

#     async def request_page(self, info):
#         next_info = info.next_info
#         url = next_info['url']
#         page = next_info['page']
#         url = url + '?page=' + str(page)
#         response = await self.session.get(url)
#         return response, info

#     def start_crawler(self, inputs):
#         pool = Pool(processes=self.process_num)
#         all_next_info = [
#             self.request_page(
#                 Info(current_info=None, next_info={ 'url': url, 'page': 1 }, retry_info=None)
#                 ) 
#             for url in inputs
#             ]
#         while True:
#             try:
#                 done_response, pending = self.loop.run_until_complete(asyncio.wait(all_next_info))
#                 all_page_dom = [response.result() for response in done_response]
#                 all_next_info = self.map(pool, get_page, all_page_dom)
#                 all_next_info = [self.request_page(Info(current_info=None, next_info=next_info, retry_info=None)) for next_info in all_next_info if next_info]
#                 if not all_next_info:
#                     break
#             except Exception as error:
#                 logger.exception(error)
#                 break
#         self.save()
#         self.loop.run_until_complete(self.session.close())
#         self.loop.close()
#         logger.info('Saved %s items', self.total_count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--processes", help="crawl with n processes", type=int, default=8)
    args = parser.parse_args()
    import requests

    url = "https://movies.yahoo.com.tw/movieinfo_main.html/id=9116"
    doc = requests.get(url)
    print(get_page(doc.content))
    #11000
    # ids = split_chunk([i for i in range(10)])

    # urls = ['https://sim.globalwifi.com.tw/products' for _ in range(5)]
    
    # async_crawler = AsyncCrawler(
    #     process_num=args.processes,
    #     session=session,
    #     loop=asyncio.get_event_loop()
    #     )

    # async_crawler.start_crawler(urls)