#!/usr/local/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from bs4 import BeautifulSoup
import time

from utils.log_util import init_log, logging
from utils.base_crawler import BaseCrawler, Parser
from utils.database_util import init_database, DataBaseType

site_name = 'fragrantica'
database = init_database(database_type=DataBaseType.CSV, file_name=site_name, fields=["title", "brand", "product_id", "url", "top", "middle", "base", "others"])
logger = init_log(site_name=site_name)

class CrawlerSelenium(BaseCrawler):

    database = database

    def __init__(self):
        super().__init__()

        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--incognito')
        self.opts.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36)')
        self.opts.add_argument('--disable-dev-shm-usage')
        self.opts.add_argument('--disable-gpu')
        self.opts.add_argument('--no-sandbox')
        self.opts.add_argument('--allow-running-insecure-content')
        self.opts.add_experimental_option('useAutomationExtension', False)
        self.opts.add_experimental_option("excludeSwitches", ["enable-automation"])

        self.opts.experimental_options["prefs"] = {
            "profile.default_content_settings": {"images": 2},
            "profile.managed_default_content_settings": {"images": 2}
        }

    def reload_driver(self):
        # PROXY = ""
        webdriver.DesiredCapabilities.CHROME['proxy']={
            "httpProxy":PROXY,
            "ftpProxy":PROXY,
            "sslProxy":PROXY,
            "proxyType":"MANUAL",
        }
        self.driver = webdriver.Chrome(options=self.opts, desired_capabilities=DesiredCapabilities.CHROME)

    def open_browser(self, product_id, content):
        url = content['url']
        result = content
        self.driver.get(url)
        html = self.driver.page_source
        document = BeautifulSoup(html, Parser.LXML.value)
        notes_block = document.select('div.effect6 p')
        if not notes_block:
            raise "too many request"
        top = ''
        middle = ''
        base = ''
        others = ''
        for timing_notes in notes_block:
            try:
                notes = timing_notes.select('span.rtgNote img.btHover')
                if not len(notes):
                    continue
                timing = timing_notes.select_one('b')
                timing = timing.text.strip() if timing else ''
                for note in notes:
                    if 'Top' in timing:
                        top += note['alt'] + ','
                    if 'Middle' in timing:
                        middle += note['alt'] + ','
                    if 'Base' in timing:
                        base += note['alt'] + ','
                    if not timing:
                        others += note['alt'] + ','
            except Exception as error:
                self.retry_info.append({product_id: content})
                logger.error('Fail to get notes of %s', url)
                result = None
        if result:
            result["top"] = top[:-1].strip() if top else top
            result["middle"] = middle[:-1].strip() if middle else middle
            result["base"] = base[:-1].strip() if base else base
            result["others"] = others[:-1].strip() if others else others
        return result
    
    def start_crawler(self):
        self.reload_driver()

        # file_content = {}
        # with open('all_perfumes_simple.json', 'r') as f:
            # file_content = json.loads(f.read())

        file_content = {
            "48688": {
                "title": "Fabruary 14\u00ba", 
                "brand": "The Society of Scent", 
                "product_id": "48688", 
                "url": "https://www.fragrantica.com/perfume/The-Society-of-Scent/Fabruary-14--48688.html"
                }, 
            "60283": {
                "title": "Asphalt Noir(e)", 
                "brand": "The Society of Scent", 
                "product_id": "60283", 
                "url": "https://www.fragrantica.com/perfume/The-Society-of-Scent/Asphalt-Noir-e--60283.html"
                },
            "19991": {
                "title": "Saison d'Amour", 
                "brand": "Novaya Zarya \u041d\u043e\u0432\u0430\u044f \u0417\u0430\u0440\u044f", 
                "product_id": "19991", 
                "url": "https://www.fragrantica.com/perfume/Novaya-Zarya-/Saison-d-Amour-19991.html"
                }, 
            "19987": {
                "title": "Mon Bijou Vert", 
                "brand": "Novaya Zarya \u041d\u043e\u0432\u0430\u044f \u0417\u0430\u0440\u044f", 
                "product_id": "19987", 
                "url": "https://www.fragrantica.com/perfume/Novaya-Zarya-/Mon-Bijou-Vert-19987.html"
                }
        }

        try:
            for key, value in file_content.items():
                try:
                    perfume = self.open_browser(key, value)
                    if perfume:
                        logger.info('Got %s', perfume)
                        self.append([perfume])
                except Exception as error:
                    logger.error('Fail to get page %s', value['url'])
                    self.retry_info.append({key: value})
                    self.reload_driver()
                time.sleep(15)
        except KeyboardInterrupt as keyboard_error:
            logger.exception(keyboard_error)
        except Exception as error:
            logger.exception(error)
        finally:
            self.save()
            self.driver.quit()
            self.save_retry_info()

if __name__ == "__main__":
    crawler = CrawlerSelenium()
    crawler.start_crawler()