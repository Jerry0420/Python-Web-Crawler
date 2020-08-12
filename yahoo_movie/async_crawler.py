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
import re
from datetime import datetime

site_name = 'yahoo_movie'
main_page_url = "https://movies.yahoo.com.tw/index.html"

logger = init_log(site_name=site_name)
# database = init_database(database_type=DataBaseType.JSON, file_name=site_name)
database = init_database(fields=YahooMovie, file_name=site_name)
session = AsyncRequestUtil()

def split_chunk(list, n=100):
    for i in range(0, len(list), n):
        yield list[i: i + n]

def get_page(document):
    document = BeautifulSoup(document, 'lxml')
    result = {}
    url_block = document.select_one('meta[property="og:url"]')
    if url_block and  '/id=' not in url_block['content']: return []

    movie_info_block = document.select_one('.movie_intro_info_r')
    name_ch_block = movie_info_block.select_one('h1') if movie_info_block else ''
    name_en_block = movie_info_block.select_one('h3') if movie_info_block else ''
    genres_blocks = movie_info_block.select('.level_name')
    all_info = movie_info_block.select('span')
    big_image_block = document.select_one('.movie_intro_info_l .btn_zoomin')
    image_block = document.select_one('meta[property="og:image"]')
    content_block = document.select_one('#story')
    yahoo_score_block = document.select_one('.score_num.count')
    vote_count_block = document.select_one('.starbox2 span')

    try:
        result['url'] = url_block['content']
        result['movie_id'] = int(result['url'].split('=')[-1])
        result['name_ch'] = name_ch_block.text if name_ch_block else ''
        result['name_en'] = name_en_block.text if name_en_block else ''
        
        genres = ""
        for genres_block in genres_blocks:
            genres += genres_block.text.strip() + '|'
        result['genres'] = genres[:-1] if genres else ''

        release_date = None #date
        company = ''
        imdb_score = 0.0
        directors = ''
        actors = ''
        for info in all_info:
            if '上映日期' in info.text:
                release_date = info.text.split('：')[-1]
            if '發行公司' in info.text:
                company = info.text.split('：')[-1]
            if 'IMDb分數' in info.text:
                imdb_score = info.text.split('：')[-1]
            if '導演' in info.text:
                directors = info.findNext('div').text.strip().replace(' ', '').replace('\n', '').replace('、', '|')
            if '演員' in info.text:
                actors = info.findNext('div').text.strip().replace(' ', '').replace('\n', '').replace('、', '|')
        result['release_date'] = datetime.strptime(release_date, "%Y-%m-%d").date() if release_date and '未定' not in release_date else None
        result['company'] = company
        result['imdb_score'] = float(imdb_score)
        result['directors'] = directors
        result['actors'] = actors

        img_url = ''
        if big_image_block:
            img_url = big_image_block['href']
        elif image_block:
            img_url = image_block['content']
        result['img_url'] = img_url

        result['content'] = content_block.text.strip().replace('\r', '').replace('\n', '') if content_block else ''
        # 滿分 5
        result['yahoo_score'] = float(yahoo_score_block.text) if yahoo_score_block else 0.0
        
        vote_count = vote_count_block.text if vote_count_block else ''
        vote_count = re.findall(r'\d+', vote_count)
        result['vote_count'] = int(vote_count[0]) if vote_count else 0
    except Exception as error:
        logger.exception("Error occurred %s ", result['url'])
        return [], Info(current_info=None, next_info=None, retry_info=result['url'])
    logger.info("Crawlered %s", result['url'])
    return [result]

class AsyncCrawler(BaseCrawler):
    
    database = database
    
    def __init__(self, process_num, session, loop):
        super().__init__(process_num=process_num, session=session, loop=loop)

    async def request_page(self, url):
        response = await self.session.get(url)
        return response

    def start_crawler(self, upper_limit):
        inputs_chunks = split_chunk([self.request_page("https://movies.yahoo.com.tw/movieinfo_main.html/id={}".format(i)) for i in range(1, upper_limit)], 100)
        pool = Pool(processes=self.process_num)
        try:
            for inputs_chunk in inputs_chunks:
                try:
                    done_response, pending = self.loop.run_until_complete(asyncio.wait(inputs_chunk))
                    all_page_dom = [response.result() for response in done_response]
                    _ = self.map(pool, get_page, all_page_dom)
                except Exception as error:
                    logger.exception(error)
        except KeyboardInterrupt as error:
            pass
        finally:
            self.save()
            self.loop.run_until_complete(self.session.close())
            self.loop.close()
            logger.info('Saved %s items', self.total_count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--processes", help="crawl with n processes", type=int, default=8)
    args = parser.parse_args()

    async_crawler = AsyncCrawler(
        process_num=args.processes,
        session=session,
        loop=asyncio.get_event_loop()
        )

    async_crawler.start_crawler(100)

    # import requests
    # import json

    # url = "https://movies.yahoo.com.tw/movieinfo_main.html/id=10522"
    # doc = requests.get(url)
    # result = get_page(doc.content)
    # result = json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False)
    # print(result)