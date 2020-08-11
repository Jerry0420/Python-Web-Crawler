import requests
from enum import Enum
from .user_agents import OS, Browser, get_user_agent
import time
from .proxies import get_proxy
import logging

logger = logging.getLogger()

class HTTPMethods(Enum):
    GET = "GET"
    POST = "POST"

boundary = "----WebKitFormBoundaryJXrxC79Dpyal5JFf"

class ContentType(Enum):
    TEXTHTML = "text/html; charset=UTF-8"
    JSON = "application/json"
    URLENCODED = "application/x-www-form-urlencoded"
    MULTIPART = "multipart/form-data" + '; boundary={}'.format(boundary)

default_headers = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

class RequestUtil:

    def __init__(self, main_page_url=None, retry_times=5, sleep_seconds=30, default_headers_enable=True, headers={}, cookies={}, timeout=30, proxy_countries=None, os=OS.MACOS.value, browser=Browser.CHROME.value):
        self.session = requests.Session()
        self.main_page_url = main_page_url
        self.retry_times = retry_times
        self.timeout = timeout
        self.sleep_seconds = sleep_seconds
        self.os = os
        self.browser = browser
        self.headers = default_headers if default_headers else {}
        self.headers['user-agent'] = get_user_agent(os, browser)
        
        if isinstance(headers, str):
            headers = self.__class__.__get_headers_dict_from_string(headers)
        self.headers.update(headers)

        self.cookies = self.__class__.__get_cookies_dict_from_string(cookies) if isinstance(cookies, str) else cookies

        self.proxy = None
        self.proxy_countries = proxy_countries
        if proxy_countries:
            self.proxy = get_proxy(proxy_countries)

    def reset(self):
        time.sleep(self.sleep_seconds)
        self.session.close()
        self.session = requests.session()
        self.headers['user-agent'] = get_user_agent(self.os, self.browser)
        if self.proxy_countries:
            self.proxy = get_proxy(self.proxy_countries)
        self.init_cookie()

    def init_cookie(self):
        if self.main_page_url:
            # 因為要初始化 cookie，所以用原本的 requests，不用客製化的
            self.session.get(self.main_page_url, headers=self.headers)

    @classmethod
    def __get_cookies_dict_from_string(cls, cookies_string):
        cookies = {}
        for line in cookies_string.split(';'):
            key, value = line.strip().split('=', 1)
            cookies[key]=value
        return cookies

    @classmethod
    def __get_headers_dict_from_string(cls, headers_string):
        headers = {}
        for line in headers_string.split('\n'):
            splitted_header = line.strip().split(':')
            if len(splitted_header) == 2:
                headers[splitted_header[0]] = splitted_header[1]
        return headers

    def get(self, url, query_strings=None, headers=None, cookies=None, referer=None, allow_redirects=True, json_response=False, retry_function=None):
        response = self.__request(HTTPMethods.GET, url, query_strings, body=None, json_body=None, headers=headers, cookies=cookies, referer=referer, allow_redirects=allow_redirects, json_response=json_response, retry_function=retry_function)
        return response

    def post(self, url, query_strings=None, body=None, json_body=None, headers=None, cookies=None, referer=None, allow_redirects=True, json_response=False, retry_function=None):
        response = self.__request(HTTPMethods.POST, url, query_strings, body=body, json_body=json_body, headers=headers, cookies=cookies, referer=referer, allow_redirects=allow_redirects, json_response=json_response, retry_function=retry_function)
        return response

    def __retry_function(self, response):
        result = False
        try:
            if response.ok and response.content:
                result = True
        except Exception as error:
            logger.warning('Retry %s', response.url)
        return result

    def __request(self, method, url, query_strings=None, body=None, json_body=None, headers=None, cookies=None, referer=None, allow_redirects=True, json_response=False, retry_function=None):
        if referer:
            self.headers['referer'] = referer
        
        if headers:
            if isinstance(headers, str):
                headers = self.__class__.__get_headers_dict_from_string(headers)
            self.headers.update(headers)

        if cookies:
            if isinstance(cookies, str):
                cookies = self.__class__.__get_cookies_dict_from_string(cookies)
            self.cookies.update(cookies)

        retry_function = retry_function if retry_function else self.__retry_function

        for retry_time in range(self.retry_times):
            try:
                response = self.session.request(
                    method=method.value, 
                    url=url,
                    params=query_strings,
                    data=body,
                    json=json_body,
                    headers=self.headers,
                    cookies=self.cookies,
                    timeout=self.timeout,
                    allow_redirects=allow_redirects,
                    proxies=self.proxy
                )
                if not retry_function(response):
                    raise
                response = response.json() if json_response else response.content
                break
            except Exception as error:
                self.reset()
        else:
            logger.warning('Retry and Fail of %s', url)
            response = None
        return response