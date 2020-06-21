#!/usr/local/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from utils.requests_util import RequestUtil
from utils.log_util import init_log, logging
from utils.base_crawler import BaseCrawler, Parser
from utils.database_util import init_database, DataBaseType
from api_keys import get_api_key

from bs4 import BeautifulSoup
import argparse
import json
import urllib.parse

site_name = 'fragrantica'
main_page_url = "https://www.fragrantica.com/"

logger = init_log(site_name=site_name)
database = init_database(database_type=DataBaseType.JSON, file_name=site_name)
session = RequestUtil(timeout=10, sleep_seconds=0)

class Crawler(BaseCrawler):

    database = database

    def __init__(self, process_num, session):
        super().__init__(process_num=process_num, session=session)

    def collect_perfumes(self, brand, page):
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
        return perfumes, failed_brand
    
    def loop_brand(self, brand):
        page = 0
        perfumes_of_brand = []
        failed_brand = None
        while True:
            try:
                perfumes_of_one_page, failed_brand = self.collect_perfumes(brand, page)
                perfumes_of_brand.extend(perfumes_of_one_page)
                if len(perfumes_of_one_page):
                    page += 1
                else:
                    break
            except Exception as error:
                logger.exception(error)
                break
        msg = "https://www.fragrantica.com/designers/{}.html".format(brand)
        logger.info('Got %s of %s  %s', len(perfumes_of_brand), msg, brand)
        return perfumes_of_brand, failed_brand

    def collect_brands(self):
        url = "https://www.fragrantica.asia/designer/"
        document = self.session.get(url)
        document = BeautifulSoup(document, Parser.LXML.value)
        contents = document.select('div#ndalphabet a')
        urls = []
        for content in contents:
            url = 'https://www.fragrantica.asia' + content['href']
            urls.append(url)
        
        brands = set()
        for url in urls:
            document = self.session.get(url)
            document = BeautifulSoup(document, Parser.LXML.value)
            contents = document.select('div.nduList a')
            for content in contents:
                brands.add(content.text.strip())
            logger.info("Collected %s brands of %s", len(contents), url)
        with open('brands.json','w') as f:
            json.dump(list(brands), f)
        
        logger.info("Collected %s brands", len(brands))
        return list(brands)

    def start_crawler(self):
        # brands = ["Rose & Co Manchester"]
        # brands = self.collect_brands()
        
        brands = []
        with open('other_info.json','r') as f:
            brands = json.loads(f.read())
        
        total_count = 0
        try:
            total_count = self.map(self.loop_brand, brands)
        except:
            pass
        finally:
            self.save()
            logger.info('Total Got %s perfumes', total_count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--processes", help="crawl with n processes", type=int, default=10)
    args = parser.parse_args()
    crawler = Crawler(process_num=args.processes, session=session)
    crawler.start_crawler()