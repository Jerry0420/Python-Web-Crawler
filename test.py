# import requests
# import urllib.parse

# query = 'Alberto Morillas'
# print(urllib.parse.quote(query))

# headers = {
#     'accept': 'application/json',
#     'content-type': 'application/x-www-form-urlencoded',
# }

# params = (
#     ('x-algolia-application-id', 'FGVI612DFZ'),
#     ('x-algolia-api-key', 'NDI2YWY5NjgyY2FjOWE0MTkyODI2YTI4OGZhNmRkOTE4ZWUxMjBhMTA3NzFkMGE1MDVkZmViOGQwZjcwNmYxOXZhbGlkVW50aWw9MTU5MzQyNjgzNQ=='),
# )

# page = 0
# perfumer = 'Alberto%20Morillas'

# # data = '{"requests":[{"indexName": "fragrantica_perfumes","params":"hitsPerPage=80&maxValuesPerFacet=10&page=34&attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22godina%22%2C%22url.EN%22%2C%22thumbnail%22%5D&facets=%5B%22spol%22%2C%22dizajner%22%2C%22godina%22%2C%22ingredients.EN%22%2C%22rating_rounded%22%2C%22nosevi%22%2C%22osobine.EN%22%2C%22designer_meta.country%22%2C%22designer_meta.category%22%2C%22designer_meta.parent_company%22%2C%22designer_meta.main_activity%22%5D"}]}'
# # data = '{"requests":[{"indexName":"fragrantica_perfumes","params":"hitsPerPage=80&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22godina%22%2C%22url.EN%22%2C%22thumbnail%22%5D&facets=%5B%22spol%22%2C%22dizajner%22%2C%22godina%22%2C%22ingredients.EN%22%2C%22rating_rounded%22%2C%22nosevi%22%2C%22osobine.EN%22%2C%22designer_meta.country%22%2C%22designer_meta.category%22%2C%22designer_meta.parent_company%22%2C%22designer_meta.main_activity%22%5D&facetFilters=%5B%5B%22nosevi%3AAlberto%20Morillas%22%5D%5D"}]}'

# data = '{"requests":[{"indexName":"fragrantica_perfumes","params":'
# www = "\"hitsPerPage=80&maxValuesPerFacet=10&page={page}&attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22url.EN%22%2C%22thumbnail%22%5D&facets=%5B%22spol%22%2C%22dizajner%22%5D&facetFilters=%5B%5B%22nosevi%3A{perfumer}%22%5D%5D\"".format(page=page, perfumer=perfumer)
# data = ''.join([data, www, '}]}'])
# print(urllib.parse.unquote(data))

# response = requests.post('https://fgvi612dfz-3.algolianet.com/1/indexes/*/queries', headers=headers, params=params, data=data)

# print('====================================================')
# print(response.json()['results'][0]['hits'][0])
# print(response.json()['results'][0]['hits'][0]['naslov'])
# print(len(response.json()['results'][0]['hits']))

# %5B [
# %22 "
# %2C ,
# %5D ]

# {
#     "requests":[
#         {
#             "indexName": "fragrantica_perfumes",
#             "params": "hitsPerPage=80&maxValuesPerFacet=10&page=0
#             &
#             attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22godina%22%2C%22url.EN%22%2C%22thumbnail%22%5D
#             &
#             facets=%5B%22spol%22%2C%22dizajner%22%2C%22godina%22%2C%22ingredients.EN%22%2C%22rating_rounded%22%2C%22nosevi%22%2C%22osobine.EN%22%2C%22designer_meta.country%22%2C%22designer_meta.category%22%2C%22designer_meta.parent_company%22%2C%22designer_meta.main_activity%22%5D"
#         }
#     ]
# }

# curl 'https://fgvi612dfz-3.algolianet.com/1/indexes/*/queries?x-algolia-application-id=FGVI612DFZ&x-algolia-api-key=NDI2YWY5NjgyY2FjOWE0MTkyODI2YTI4OGZhNmRkOTE4ZWUxMjBhMTA3NzFkMGE1MDVkZmViOGQwZjcwNmYxOXZhbGlkVW50aWw9MTU5MzQyNjgzNQ%3D%3D' \
#   -H 'accept: application/json' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   --data-raw '{"requests":[{"indexName": "fragrantica_perfumes","params": "hitsPerPage=80&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22godina%22%2C%22url.EN%22%2C%22thumbnail%22%5D&facets=%5B%22spol%22%2C%22dizajner%22%2C%22godina%22%2C%22ingredients.EN%22%2C%22rating_rounded%22%2C%22nosevi%22%2C%22osobine.EN%22%2C%22designer_meta.country%22%2C%22designer_meta.category%22%2C%22designer_meta.parent_company%22%2C%22designer_meta.main_activity%22%5D"}]}' \
#   --compressed

# %5B [
# %22 "
# %2C ,
# %5D ]

# {"requests":[{
#     "indexName":"fragrantica_perfumes",
#     "params":"hitsPerPage=80&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22godina%22%2C%22url.EN%22%2C%22thumbnail%22%5D&
#     facets=%5B%22spol%22%2C%22dizajner%22%2C%22godina%22%2C%22ingredients.EN%22%2C%22rating_rounded%22%2C%22nosevi%22%2C%22osobine.EN%22%2C%22designer_meta.country%22%2C%22designer_meta.category%22%2C%22designer_meta.parent_company%22%2C%22designer_meta.main_activity%22%5D&
#     facetFilters=%5B%5B%22nosevi%3AAlberto%20Morillas%22%5D%5D"
#     }]}

# curl 'https://fgvi612dfz-3.algolianet.com/1/indexes/*/queries?x-algolia-application-id=FGVI612DFZ&x-algolia-api-key=NDNjN2U3ZmY0OTYwN2NlYTc4ZTEzNzdhZTRlNGE4MmE1NzE2MzNjZGFlNDJlZjg1MGFlZWQ5NjVmMGM0OTM2ZnZhbGlkVW50aWw9MTU5MzQzNTQ3OQ%3D%3D' \
#   -H 'accept: application/json' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   --data-raw '{"requests":[{"indexName":"fragrantica_perfumes","params":"hitsPerPage=80&maxValuesPerFacet=10&page=13&attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22godina%22%2C%22url.EN%22%2C%22thumbnail%22%5D&facets=%5B%22spol%22%2C%22dizajner%22%2C%22godina%22%2C%22ingredients.EN%22%2C%22rating_rounded%22%2C%22nosevi%22%2C%22osobine.EN%22%2C%22designer_meta.country%22%2C%22designer_meta.category%22%2C%22designer_meta.parent_company%22%2C%22designer_meta.main_activity%22%5D&facetFilters=%5B%5B%22nosevi%3AAlberto%20Morillas%22%5D%5D"}]}' \
#   --compressed

from bs4 import BeautifulSoup
import requests

cookies = {
    'visid_incap_454533': 'AAr8b/LGR6uDT8L8WSmWLjpY8V4AAAAAQUIPAAAAAACgl23oN90CWYTPKl6JrfyA',
    'incap_ses_932_454533': 'rRIOGDQfBwhZHoVFGSHvDGrE8V4AAAAAaq5NXNcKbMeu6jW0NFtrgQ==',
    'ASP.NET_SessionId': '5its2455xcq3xovzr50izvqp',
    '_sp_id.d5fe': 'ddf608e6-75ec-4d8b-a54f-eb503dfbcd56.1592874976.2.1592902675.1592874976.00bf788e-de01-46f3-b32c-11e95b6bc68d',
    'AMCV_DF38E5285913269B0A495E5A%40AdobeOrg': '-1303530583%7CMCIDTS%7C18437%7CMCMID%7C54209626291174910991989563787399554200%7CMCAAMLH-1593507475%7C11%7CMCAAMB-1593507475%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1592909875s%7CNONE%7CMCSYNCSOP%7C411-18444%7CvVersion%7C3.3.0',
    'AMCVS_DF38E5285913269B0A495E5A%40AdobeOrg': '1',
    's_ppv': 'https%253A%2F%2Fwww.ip2.sg%2FRPS%2FRPSLogin%2FSPLogin.aspx%253FReturnUrl%253D%25252f_layouts%25252fAuthenticate.aspx%25253fSource%25253d%2525252FRPS%2525252FRPSLogin%2525252FSPHome%2525252Easpx%2526Source%253D%25252FRPS%25252FRPSLogin%25252FSPHome%25252Easpx%2C70%2C70%2C962',
    's_tp': '1376',
    's_cc': 'true',
    '_ga': 'GA1.2.609718205.1592874977',
    '_gid': 'GA1.2.510583199.1592874977',
    'my_session': '!9nYk6vEnA0xrckS0fT5uGUomWtHPktvWFMtmBu3oKWWZL3qBLBKSqQhE0mdaJVJRD9qyhwLMzwZh',
    '_sp_ses.d5fe': '*',
    '_gat_gtag_UA_107910755_2': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Referer': 'https://www.ip2.sg/',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Origin': 'https://www.ip2.sg',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    # 'TE': 'Trailers',
}

# ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$lnkPage2
# ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$ddlTopSelect
data = {
  'MSOTlPn_View': '0',
  'MSOTlPn_ShowSettings': 'False',
  'MSOTlPn_Button': 'none',
  'MSOSPWebPartManager_DisplayModeName': 'Browse',
  'MSOSPWebPartManager_ExitingDesignMode': 'false',
  '__EVENTTARGET': 'ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$lnkPage2',
  'MSOSPWebPartManager_OldDisplayModeName': 'Browse',
  'MSOSPWebPartManager_StartWebPartEditingName': 'false',
  'MSOSPWebPartManager_EndWebPartEditing': 'false',
  '__VIEWSTATE': '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',
  '__SCROLLPOSITIONX': '0',
  '__VIEWSTATEENCRYPTED': '',
  '__EVENTVALIDATION': 'jXPU3sVn3TmsanS34O5h/TK4kYJdsjGI3Lh8D+2bzmM75LqcIt1oDEZ+4TCUCXpXfShKcr0+1MToFKfCXnNe5m8Kq9iK1JNQhValFGPZV0nVJ+IfKJs+CN6jJEP9j/Uy8TlK+3JZUakqj1dHnzAHQNrpVx3aRsPEF7ZX2XfUlYw2mxlJ4E093cA0cOcyrKjLvuMTYXru6STEBZuXruaIJzFgVdXoaxf4K/CPEVtHTtwDyonGiHVoyaXXCk45IuQ1YkryIv7joK3myzQlGM7Ak4uML7ymBeEapqcuykVo2pGl+XDFazS6iuLYpOGAIRrOHYdka9Y143/Wrq8vl4xvmTIXyODFoxfXHWCBOYgF7ZjsVeuKBWZ1isQ7qNc5kVTeX4ejT3evz/89E0wKdBzwi64wtVDU0PFz0PMEAH+lVjK1x4qv1ojy53fSkEbMyzstd6uHYMDxYNpjgzrtdCG26dUChKQmDlnBtLQjsMLsJvh57i0e',
  'ctl00$PlaceHolderMain$uclSimpleSearch$txtSearchText': 'english',
  'ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$ddlTopSelect': '100'
}

response = requests.post('https://www.ip2.sg/RPS/WP/CM/SearchFastP.aspx', headers=headers, cookies=cookies, data=data)
document = BeautifulSoup(response.content, 'lxml')
odds = document.select('tr.odd')
evens = document.select('tr.even')
print(len(odds) + len(evens))