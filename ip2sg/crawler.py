#!/usr/local/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from utils.requests_util import RequestUtil, OS, Browser
from utils.log_util import init_log, logging
from utils.base_crawler import BaseCrawler, Parser
from utils.database_util import init_database, DataBaseType

from bs4 import BeautifulSoup
import argparse
import json
import urllib.parse

site_name = 'ip2sg'
main_page_url = "https://www.ip2.sg/RPS/WP/CM/SearchFastP.aspx"

logger = init_log(site_name=site_name)
database = init_database(database_type=DataBaseType.JSON, file_name=site_name)
session = RequestUtil(main_page_url=main_page_url, timeout=120, sleep_seconds=10, retry_times=3, os=OS.MACOS, browser=Browser.FIREFOX.value)

class Crawler(BaseCrawler):

    database = database

    def __init__(self, process_num, session):
        super().__init__(process_num=process_num, session=session)

    def collect_items(self, input, page):
        perfumes = []
        failed_brand = None
        api_key = get_api_key()
        query_strings = (
            ('x-algolia-application-id', 'FGVI612DFZ'),
            ('x-algolia-api-key', api_key),
        )

        body = '{"requests":[{"indexName":"fragrantica_perfumes","params":'
        params = "\"hitsPerPage=80&maxValuesPerFacet=10&page={page}&attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22url.EN%22%2C%22thumbnail%22%5D&facets=%5B%22spol%22%2C%22dizajner%22%5D&facetFilters=%5B%5B%22dizajner%3A{brand}%22%5D%5D\"".format(page=page, brand=brand)
        body = ''.join([body, params, '}]}'])

        url = "https://fgvi612dfz-3.algolianet.com/1/indexes/*/queries"

        response = self.session.post(url=url, query_strings=query_strings, body=body, json_response=True)
        results = []
        
        try:
            results = response['results'][0]['hits']
        except Exception as error:
            logger.error('Fail to parse %s', brand)
            failed_brand = brand

        for result in results:
            perfume = {}
            try:
                title = result['naslov']
                brand = result['dizajner']
                product_id = result['objectID']
                url = result['url']['EN'][0]
                perfume['title'] = title
                perfume['brand'] = brand
                perfume['product_id'] = product_id
                perfume['url'] = url
                perfumes.append(perfume)
            except Exception as error:
                logger.warning('Fail to get item ', result)
                continue
        logger.info('Got %s items at pgae %s ', len(items), page)
        return items, total_page
    
    def loop_pages(self, input):
        page = 1
        results = []
        total_page = 0
        while True:
            try:
                items, total_page = self.collect_items(input, page)
                results.extend(items)
                if page < total_page:
                    page += 1
                else:
                    break
            except Exception as error:
                logger.exception(error)
                break
        for result in results:
            self.append(result)
        logger.info('Got %s of %s ', len(results), input)
        return len(results)

    def start_crawler(self, input):
        total_count = 0
        try:
            self.session.init_cookie()
            total_count = self.loop_pages(input)
        except:
            pass
        finally:
            self.save()
            logger.info('Total Got %s items', total_count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--processes", help="crawl with n processes", type=int, default=10)
    args = parser.parse_args()
    crawler = Crawler(process_num=args.processes, session=session)
    crawler.start_crawler("math")