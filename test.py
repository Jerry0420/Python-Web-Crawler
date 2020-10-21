from bs4 import BeautifulSoup
import requests
import datetime
import json
import os

courts = []
base_url = "https://law.judicial.gov.tw/FJUD"

def get_info_for_every_search(date_info):
    q = ""
    today_total = 0

    data = {
        '__VIEWSTATE': '+NRdE4cWARfTHoh5QEQSAxM6VCT7zumKyyVg1WH12j3APveLYA7mlN/8grfIz53VLPjNYPWt+iWd9n+v9nEaxd/wNz8b9RO7/2fYGMd3g1kldQ+k68Y4KxLu2tJBU5hfMCp4KLA+DURNr7/RlWXlaJh6kM6jY/p/Te0rLw==',
        '__EVENTVALIDATION': 'uMfD/hlXvQlMWxyEr62IbdI3ok3vQl6iM++mxzr45+CJrAc18/1DS5C+Ehkl7oz4wWUYH04JW7R+WGpUwDBvlGfPkDw=',
        'judtype': 'JUDBOOK',
        'whosub': '1',
        'ctl00$cp_content$btnQry': "送出查詢"
    }
    data.update(date_info)
    response = requests.post(base_url + '/Default_AD.aspx', data=data)
    document = BeautifulSoup(response.content, 'lxml')
    q = document.select_one("input#hidQID")['value']
    today_total_element = document.select_one("span.badge")
    today_total = today_total_element.text.strip()
    today_total = int(today_total)
    return today_total, q

def crawl_page(url, params):
    links_per_page = []
    try:
        response = requests.get(url, params=params)
        document = BeautifulSoup(response.content, 'lxml')
        a_elements = document.select('a.hlTitle_scroll')
        for a_element in a_elements:
            a_link = base_url + "/" + a_element['href']
            links_per_page.append(a_link)
    except BaseException as error:
        print("Error in crawl_page")
    finally:
        return links_per_page

def loop_pages_of(q):
    links = []
    url = base_url + "/qryresultlst.aspx"
    for page in range(1, 26): # 26頁, 500 筆是極限
        params = {
            'q': q,
            'Page': page
        }
        links_per_page = crawl_page(url, params)
        if not links_per_page:
            break
        links.extend(links_per_page)
    return links

def get_courts():
    global courts
    if not courts:
        try:
            response = requests.get(base_url + "/default_AD.aspx")
            document = BeautifulSoup(response.content, 'lxml')
            option_elements = document.select("option")
            for option_element in option_elements:
                court = option_element['value']
                if court:
                    courts.append(court)
        except BaseException as error:
            print("Error in get_courts")
            courts = ['TPC', 'TPU', 'TPS', 'TPA', 'TPP', 'TPJ', 'TPH', '001', 'TPB', 'TCB', 'KSB', 'IPC', 'TCH', 'TNH', 'KSH', 'HLH', 'TPD', 'SLD', 'PCD', 'ILD', 'KLD', 'TYD', 'SCD', 'MLD', 'TCD', 'CHD', 'NTD', 'ULD', 'CYD', 'TND', 'KSD', 'CTD', 'HLD', 'TTD', 'PTD', 'PHD', 'KMH', 'KMD', 'LCD', 'KSY']

def post_to_server(links):
    if links:
        print(links)
        # TODO: 丟回 server
        pass

def get_error_date():
    error_date = {}
    file_path = "error_date.json"
    if os.path.isfile(file_path):
        with open(file_path,'r') as f:
            error_date = json.loads(f.read())
        os.remove(file_path)
    return error_date

def start(date_info):
    global courts
    get_courts()
    total_links = []
    try:
        today_total, q = get_info_for_every_search(date_info)
        if not today_total:
            raise Exception("Zero of first get_info_for_every_search")
        
        if today_total <= 500:
            links = loop_pages_of(q)
            total_links.extend(links)
            post_to_server(total_links)
            total_links = []
        else:
            for court in courts:
                date_info['jud_court'] = court
                today_total, q = get_info_for_every_search(date_info)
                if not today_total:
                    continue
                links = loop_pages_of(q)
                total_links.extend(links)
                post_to_server(links)
                total_links = []
    except BaseException as error:
        print("Error occured!!")
        with open('error_date.json','w') as f:
            json.dump(date_info, f)
    finally:
        post_to_server(total_links)

if __name__ == "__main__":

    error_date = get_error_date()
    if error_date:
        start(error_date)

    now = datetime.datetime.now()
    date_info = {
        'dy1': str(now.year - 1911),
        'dm1': str(now.month),
        'dd1': str(now.day),
        'dy2': str(now.year - 1911),
        'dm2': str(now.month),
        'dd2': str(now.day),
    }
    start(date_info)