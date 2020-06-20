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

    def job(self, perfumer, page):
        result = []
        query_strings = (
            ('x-algolia-application-id', 'FGVI612DFZ'),
            ('x-algolia-api-key', 'NDI2YWY5NjgyY2FjOWE0MTkyODI2YTI4OGZhNmRkOTE4ZWUxMjBhMTA3NzFkMGE1MDVkZmViOGQwZjcwNmYxOXZhbGlkVW50aWw9MTU5MzQyNjgzNQ=='),
        )

        body = '{"requests":[{"indexName":"fragrantica_perfumes","params":'
        params = "\"hitsPerPage=80&maxValuesPerFacet=10&page={page}&attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22url.EN%22%2C%22thumbnail%22%5D&facets=%5B%22spol%22%2C%22dizajner%22%5D&facetFilters=%5B%5B%22nosevi%3A{perfumer}%22%5D%5D\"".format(page=page, perfumer=perfumer)
        body = ''.join([body, params, '}]}'])

        url = "https://fgvi612dfz-3.algolianet.com/1/indexes/*/queries"

        response = self.session.post(url=url, query_strings=query_strings, body=body, json_response=True)
        try:
            print(response['results'][0]['hits'][0])
        except Exception as error:
            logger.exception(error)
        
        return result
    
    def loop_perfumers(self, perfumer):
        perfumer = perfumer
        page = 0
        results = []
        while True:
            try:
                items = self.job(perfumer, page)
                results.extend(items)
                logger.info('Got %s of %s in page %s', len(items), perfumer, page)
                page += 1
            except Exception as error:
                logger.exception(error)
                break
        return results

    def collect_perfumers(self):
        url = "https://www.fragrantica.asia/noses/"
        document = self.session.get(url)
        document = BeautifulSoup(document, Parser.LXML.value)
        contents = document.select('div.cell.small-12.medium-4')
        perfumers = set()
        for content in contents:
            perfumers.add(content.a.text)
        with open('perfumers.json','w') as f:
            json.dump(list(perfumers), f)
        logger.info("Collected %s perfumers", len(perfumers))
        return list(perfumers)

    def start_crawler(self):
        # perfumers = self.collect_perfumers()
        perfumers = ['Alberto Morillas']
        try:
            count = self.map(self.loop_perfumers, perfumers)
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
    crawler.start_crawler()