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
    'ASP.NET_SessionId': 'ihpo5e55kma3zzm3mujvs4vz',
    'my_session': '!gfBe3Z1qHj9WJo20fT5uGUomWtHPkqEJX+C0T16+qGsqKtSVRgPDRCmi7wqypHayau6HUisb7qMH',
    'visid_incap_454533': 'AAr8b/LGR6uDT8L8WSmWLjpY8V4AAAAAQ0IPAAAAAACAUxqVAXInYxKvX9f4fpnzlYMTx8z/Gzmh',
    'incap_ses_930_454533': 'N0ugJsGR5l7Th3zlKQboDKoq8l4AAAAAqqWE7HnxzCFxaD7Izg7v3w==',
    '_ga': 'GA1.2.86079150.1592928941',
    '_gid': 'GA1.2.1536500284.1592928941',
    '_gat_gtag_UA_107910755_2': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://www.ip2.sg/',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Origin': 'https://www.ip2.sg',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    # 'TE': 'Trailers',
}

# ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$ddlTopSelect
# ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$lnkPage3
# ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$lnkLast

data = {
  'MSOTlPn_View': '0',
  'MSOTlPn_ShowSettings': 'False',
  'MSOTlPn_Button': 'none',
  'MSOSPWebPartManager_DisplayModeName': 'Browse',
  'MSOSPWebPartManager_ExitingDesignMode': 'false',
  '__EVENTTARGET': 'ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$lnkLast',
  'MSOSPWebPartManager_OldDisplayModeName': 'Browse',
  'MSOSPWebPartManager_StartWebPartEditingName': 'false',
  'MSOSPWebPartManager_EndWebPartEditing': 'false',
  '__VIEWSTATE': 'HzXris+9MkWSghs14q+IpPTbdvriPXgsU00X3/ryKBbdki6ybS4nww0EcW9IPZVydgD2HUh5GPjDZBamIsNNPDPzjrqHv8NDhZacZ/lAGzmaLs700vIYpklKxd2YagKFMr0+NsAelbAQVjcKsnp5AcENO4cUp7G+rjUAH8hVItH1IYlAwdODi4KDmx8/z1dHEtcLuuAopOnsJaHCwkOG2Pntd3ABuNd3RJ5Ac04PF370ArwDTysx8QUmvvYySXJf1TDCwLks9OTxnuNM7ZDq92lf3LCLi0Ot8/tDEFbhPIbnUVXDYjnVFtxo9dmqAMEzL1J+VdgKAMGLtfYKKaWFRWALZ+Wl9HtA7AJyklvB4tIlgvvVn6oACMPpKKit4MB70GofChy+dkHGLLX/j3SbQqLlHLJYwx12CwUO8WuWzaCc6C2mPXpW3P9LIyaKBPuD8QHPh0/j7isG+OFaMtcubCY+oJi9sHzAkLPp6LivBg250A+NfM/Ae6h2VuV+eo2w6veK51SVywicZNEjNp46nXCJdLc3duTz9CMY8CbuQOAizHyvVb8iOJghAxbf1QcVa+7DCqke3EuoyB0SL7PAmzg8DY7FTIUFFV04vdhez/RvvQmu/HBX3TycOPWgSlNl/K7nI6Bj/eCDcyCbe4JILArYaOQy1S1lxqcv2Ry4hHetu2wKLQ43l6JWSsv1sAZsH8sI0XNOD6aHSyzbiOreQ+/kCGMminw8rhDdyUzt/J+WKveJn2tyMCnSf0X80V6IjJLmM7LVpbAdNjuqKGl0m7/vvaiXUSR9+o8igxPdsFLWKHopfbSzo+d0mcUt8TIU7GwciEc/UadMrEDlNIzQc/Dcwhp5ruPH4yvYYgeBZyG04STA2Bv/1l2Adyg8WVb582OF4/EngjxQAQKrX7/r+8vmKOUlh/BmvaCAkt7a1R3Rc9NftzIBoTUXSufj7v4gCa/19ugRiWftsznU7iPyYGmhDssT1k5PjzwYskZhpFjQJcKOgPh25j4q4H7OVPoYXRqEcqUnmu1M0uiRHO6EAybqB2Qp8MVI5XXgLMdgiKiOIjsWpi9lNmWb/w4wYz8sPqL4E5yArMxj5PpWqI+JsXoSWO7Yu2kOZ/Q7GEN1yuOp/TxGYgSlyE68IVA91IHVz3eiPuvAdKhy6DzLVVnE7eFAlgeOOCxpwErK+aSqhDIG/r0+U8u27ESZKegG/vvGkwVi/qWG+R9aCf3mzuUNvIAyKkbnTJqErmq7VDAmXRQTVDoeQdEauiybEwlae4zOd3WJMnt2E/x9+n3mqQCQZYc32zlYgrzgzjoTaFKu8PNP3yW0me0Rvbx77UY9q4IMXzNofUphWWH6bmjnA6Kl/KojE27hYatA5XVCEVs6fw8pOumEgTaC2By1q7Rvzt4hL6QKWPyQqrqnvfdR3EO+nkLUkpFcgi8QPmFKn28/HcMwO+sFiyehhbjJIRPOfFQT1bTJ0nb3CB85PAkAv6uXbQUMfPirRADS3cOIb1Joo2RA51ueUk+rVwPt0KQ2TwmmG1D4Y5cro75f2nfEM0R6on7Wt9puGnA7wK1OPrqZZ5aCtw2zROVKG8ixWkGKZgntSDpsEc35u2wRvIi6fR1fMl1MEnYkxaDE7wCO+oyAnlAc5C+S+JGk/54c3xzQnUek6HxiatfIZuY9o4XtBCKug7cUtBhLG17pG1GTemEeJ/9nrmXnqz7q3FN3aa/Y16VtZN+vFeLVSfLmFBXfJZUaPY1tzLkfVMb1a4hjFaJ/qPlxLzwzTtOYvB9k3wm+QpwdatAfXV+xgnHQo5GL40uXmH2lW/4VaqJA0C05KxrlioqHBasKeB/YNFc5HFiDcq71s76V7OZfyOLtneXbsXj+rifT/tTaaCRX458RDm4exuSdqqCH6/3K6okR5ebDqafp165WT1G0eYvI84IxhNJfArCK8j39jPGpG+EAdQgDs6GLjcX4ROnTe/cmar/1+MIcRXVIJ6izqIpAoeq61PY4P05520Kx9SanWGcX8dATEPYxnonAaBN6fXncXdK6l7s24m6ioYXrpElXRNTtiK2GGRtQGLr+u1pOz4CWRyd9CzBOsvH5AJaANDBNLT/uQ3AXap07KLabB0bIttCRZ4dheG0fVVNdj2thsrZVCQWjRPkepl4V/iiDzGXn3xlcum9z0860KwAYZQ6Zb2gUTkqZyPf0hbUnmDt/BZfL42dc87lnqA/xnkuXF/HpFdQO0cqWF526puVMHqg40PmUWclPMfOwRRbAIUeKeTZzZ/cbkqf2lcgBsEYa9j55IoP6JCkIu3tfyfKcQhfes9Rm/HSxazX2XfFDo9S1sgwKtL/DUALbc8IP62JesNxBoX/KR8vHcWjk8IkfC0MrCFeXJMdgSt2fQM7MNiXDe5rNbQI4cw2LEnEwqYAIGnMjwmmx3rAP3QTpxitPPrk3mtFrkdHHfrm7FkkVUxfg0MntvivSbvRweei456pno5b5memO/snpOtzwGk0x0csGe8t6xBsNKCC9lzdIlmr78+JGw+gqNMua1/H3YMPpeJ0xfI+UD7/3E8auY3EtaHijm0smTJgR+OvmIug4a48WqKGtMYiMFQG02NvgOcF9WOTN/OBU9ZqjQ4OEkMu8i0LxuUKWezT86L+ENi6fLNSMEamz6Pg2oIgiylwkxfhYVEWKSo/Unz9QoKO9IqAWpmaPh9Fgwc952Wpgg1gCPSSvoCeSV3w25Jk0j0Ma9J3JNOsnehiLg/G1Fqwq6GxhxFqJlaDM40oUc3xD5cqXEj4rLEk0TQv7oTytpT+iB5SSW9oQl41kGsIZhHSdrWkFLI0oJiRmZrdIvAgeXcn/wK01Axgix71CQvwv0mVCSZLwBvrMpsUFf8Ve/EOMv2tBf3gDxRsCq2bByIoGqcoDyGIJYXhE/6IeWI/l+wtLZI1rygMl84/3Vqlcx/7J6lkCEPs35jgnHefNnn/nqUPPYGQTxgAIpzXvuBWpYVAr2ixYO++5szWua7qgb89YuUOfOrQbsT0GaUBdRGQOkt2Exohz+Q+wResbCxRkzkljovn5m9dU55tIUxNIIn3rCAEUkrsmRz4vQuMacaQ31Z2HdLyPfdBV/WuWNdeaAhdDECW14fyCWzj4HmyYbXZuw6R6ry2cUCUSxfDA4d/H8m7XcOtGDL0KsJvDCdfRCWlxEvrjntxKldS6OJ6ZywxRV2M1CIpdv9hXHHVQxCOu8EarJiA8HTjGIqlDHpQpwSJjf3A8X1fPhAbXdfv5E9oWjbkHd6hZUwSfFyzZop9CYBplF7jAubbjKH5pGNAlREsOyY5ONVAVUD34cDFplLfo402MMVD7rb5xW+0PWvkuvz5724JS6cTIyyiX4rWAOilVnUOH45YtdCeOd7Jo0Tdfnc0S7N5VNYLCAkli4AS0cu26RM3FkT/G+7G5E1qBUn9kc3W0GVyi2Gk95zJx5AiXZ9mRVwiEWH3JpaUiBFFWj8q8UNQVajQ2jrObLC8shY/gP0eZWATafpb5Cas2l49TMkNES5vzgUdDB881ffmX0RN+XKMtllTFBAG9eyUkjIxSIWN4sBN36frFvo2QF4s9dv+b3HdpJpQPxO48Cn95sNLsk8mIP4LnjayovPIQUHgVJ5wJkBFOB37mZrDL+iZ1GqTZob0iFAIPSuWs8JvYmUSoJjKmGjETDKzCNNXdINyQo8i77hjcy7XGvw9xtaiAUnf9Xx2aI6rx6FMx6Ku2bxkYJgAmqYh4fJHKhphvfwQhXjKXIqoZ+ZoIorDasunpicC6BPSltz+Uc11tSwlE0x96VQDIWg2sfh4IDGeFuy7AejpkGwqieOcyux7rZsqJdUQNbRvwVkT+3ck9nwVRWU3r1VR0oQKbteGUpWkMhk33YwlF0HQjzSPLr71wvDRd7bdeMnw41s7H7vBFqBZ9nC9D5Wq8aHnwJs3ugum3Fa3XfZkaBwURx/pmfdPDSPdB0Lcd90qsNGi1f6pmd09EmVnjg4cphfCP6XWmq/f8/Vjsvh9wn7PXEi+gjPkjYaLQZMhwegnuoZsHa9EP8q3MgMk2mCP0MFzZJS3pv/0FwBp8pVfGOVdMBZxfUfEolIzo43zSk8jEvc0s+L+i6OTe5LvM2qikjxy9DkWS/OBZNSEU/mM8Uycp7mDn/bZK5o6deFW0RVGm6QzdoI+N6OFNhifrOc09jWh/ZP0YXh1ha5QqskkY5kfuvM1dadC/LsHHM2t5+/6ZhJD42OHUuP+9LIHkVzcRHcg84jLpUflEo+nQ03TftW3TDmQwHvFBwbgHtyVAYOweVrJHIdT41L6NvnucX+WEL9ICUgYkaJbwUbc1oEJeZ2WFS3/olEvA/qaa1hx4Lmq2/mOsE6vZ5a1953Z8OsLawCCWaZdrC5cTJg7U5zpT8LoeUcm7oCm+X6uvpxJNgDpmkQHLoBK+HNk5n6m52Spt/Z3WKoSJpO/73ur6+Kpm55UgREejoyGaHUXqGAxpyejfSN8ZOQ/MLEZLFQwHBsBnYa5O4RzzVyugGV/5Xr/oTL4HIHzD7jREAN/lZgP3mdiyr6OuuZVNUKMF6M20pnYRufV7I3ENt9xw+89sL3YE5iQJWklsHaioCjOQhpaUShr3do2QBduEM70nW1Izb0MzvxvTP9OOzqaS0hoRWGHzIFI5Ld4xcUveI4rCdzukfeOR/EjdfrLvG6PYGlwHno3LW0iasDL+cx1W9+FSLpUQ3U45A73DohKv4gXGMsZk2HTf9eyOwcEuo2zrJ5q8AxzwRhkpKyR4wAmbCGitGztJ3MyIJYgBRy4xHDCp3v7dkabzfbc55I66/FECOaemgkVdxIclZwObf3f247LI+3+nuZLvnnE2wcWWvb/MKBleniIgo2BeUNKgB5OL0CDClVxm3tlZqotQBJjGGaC0iOxkTCa5XHnREmI7XvMq5o9miOJXJwKlES7xq7XptxIDM6KfAMEcrRx/isGAKtiPqhR6P2bEFpMIZ5BD74hE0b7wfM6xa24Q7GqEZAXUzh17YMy58nGFZt//WUsY0ufi2JezIRS0IRAyj1JzxOCgIjko9259V6kHBVL7mxP186zLROhS8vSM59PCiHADr2VMhCdbjiyCB6k6z5sHx/nX0o7Ht1Rxu+aGKcjkC7AMF2FyGA+YC4CdbVxapGtDTmOGlp+r1za2HdvdEmK95Us4YDC9nApkFDf/vxBz92SR3fnt26QRltGXJaQnzA4ycjPdyqurb0PfrmOsOmPwA13Krddf6UWTsLGTNQch+o+8A9jGGq1OCHEicY0XvEZna8zAsXNOMJDwft7nEF0I39CMxIgwFpjcFRJYF18myS+lvDalASps1+o4994GG5IRentlGNDPpSIcBIt/PTQgWDafFTRXkFP4iCZWnoBa27Utjij55AEqk0NepDXxI9FIKTVUrmYRjA9jFHc9YMUhHe2fMumerXWN3ZSGe7IMxXxbROTPRVkAjwENpfPvmuoijCbePXK0bClNixNRwNkfXGy8uz5GxH5Uh/3odPQZWjU50mv9Qp7eGyqixLRm9/Gv8iMwwNsOZfvgEHfTQ2nMFrpb+wsTvKoD1jllfRzsal6za3hGRlIfYLW5xF6jekZm4cwu8k4WgBNp207Z1ql3ON8/Go8m6LDAZ4KMWI4p1FpQjRdfe4lb7quHnalMgvo+8jASMROxhYyUvpgt+9SG5yuA+OCsTYwGWdlUv6q/Mw7nOTSgyhQmEZNmNKqrvYata3AkugcK1z6NSxELxtHB87QB75fnS67+vFsQv+AV+ELGZBBvhzDasb//EXPTLllNnEqaRct/De0uUhWy69qZzfEt0aAiaQlXvCSJj2q7i1u0qypXGOzMhLxttkrilLuEjdfRozwdQhC3Wztphki/00xxeEUcOhP/Kc0WQI7HvIUPDkQi8dcGgu3HN1LHub/XeBll0mR7/qIsPtEhOi0z53GLYc1Tn1JBLLFbWzyKAAvw948B98Ruyymmb6/sEEr5Pv03y7pOyAdWF3U4akq4OhSFT5EfxbrasFr+Hy4idLEToQNlf1uCVIK3cYev6H7n0EpS3f7ic/PyZ/KylAwZv+Vy1aaN9VB6WYc19tEfOBiHu0Dph8zYFwDvyszpFM8D3mlITECox3M1idvtOH/XnQr0LAyEkdIrE/CgvdVrlpSLIjRXqyUfGXpcSa4TgiQnGawsM9P/ZrmNgB31jeH3GZF/93pQXvTQODbOeHi5wzBgwDJxBVOJxLamVSuiDPcbw5+RLo6yhyT5Vs9CVP9K3C5UZq6pnzEThXHc3YbBH9XBpLQR1rwFipJRfAEzCH3iC2ccNwbGY1LlrNus7CrLhhHJfdYDXRjep1Fgcox11URxyttUPPgC1ov/8coGvwExxMcuPT0QfiHLPQACYdnO1pCxyZAN3xXBN1+BdY+JeyGC6Nuik+Xwgpqd3qxHL9qKjVKUCeekdVvgncMqZRDEQZBw5gIqnYk+Ldn+uJDfeJhjHIcDr9kAYE9tevhS23xicaq1ZC5Vlaocw6mGDszY2ilzxVVZYu56rlj9i/S53Oqe4wzC8lvEFuCyFulWCgR/u7W1narIfdfJg+lV30JTDZYfW9NPhk2+a5o1xJrbSZF99GTd3PR0VVdgcUzJD+YZ43xue3w9sYOAgaImfIJmKzKTOuQPCIN6BitEHEQ1Nw3oCFpM2WjWsGu2ntSYyaQja0hyH17pAnrksxTWYzYq6VImhAxUCiMyAQd/kalUanX8Gbdbx8caXJo1jQXAW7zi508Yx6Udq2125l8MANGGGzywdvuiWW10GmDzZIJTUvv8cD9eA8riRVzijLkvSs8Cei6+tFnwulwyoSeUuUQJFCHPjcE0n8Iyy2SYVSJvNUQNNAbJyPXbaWazhxcN0fIp9iu9rOwRLRZCBKJoZO3FNvRrS8ek07odJHg7oUiP3xPNDLKWQxgWK9uu3O9It0VWT565oQGRywaNIqVrZEC8euCcdv8aVJybo7khpdqxLOvzVw5W+9vyxrACIHL28qzFc3ecU7A4I0MNp+41frEIMLZ0Yc8zjt/RMHnJ6FiQY2Tgivsb4NwwzPQ82vlkiJnPziQ0Uy+3xZZtJ96MILDiDFgTheggnOnvhbA4Xw51TmSLu2L6ULmBfv6xzK9p4nkeP5hK6cE0RpqZYdKvin8l9YRLXd7q/4nbRiXYkUZfHTuVWFCIaegE88yRLbUs4GVl5U39h8CHZILWFz73PTV5ex33DRW8/wbzZsRYQf9fK3NyB8TSKbwEJeyEK09fbO4gcxrLkwFa0QDIJNmPlyx2hMAng5m2NZr/8ihAi+VIEr0rWxQMR/v/TYPUhsIBrifWEzgYEycan2JZtuNb5X/GMQYXet0JovQv4RCIxk2NN+6Jy2HPnVOZ4jwpTRtMz4xv2HdBvlJ0IXvWSaQ/JZvM9SFYe8d9mKRMGxsqel7q+70vM4to3xFC/tqBxkQeYpTsIV4BB9+7NOnLSiq7KaaDSdU0ILt5EUOjQzjbr6pjWIzeuYAJ7B+jxoMLWYc6mZzzvXCUKjgBQGZhoag7Fwd/PHaMx5lseEZjNQCKi2/fMY5E56f1oR+wryMciM37w7emSrugZ42J7v9iSprTG0d73EalVOdgnSAvnP8g97VHfc4QKJiNb8hWg627KUxO9f3D0hQf8u4FkmlVKLX0xNnxrGdDMjCHxmcTTpzfVuEIPtRwLEiMmOWhCJYS4RBu4fp52MZvWPAYFxrhxMneoxBPqR9ILLsIPiHpwq2ivrP24LyvRatGRjKTutPoZCW38R0Eawdr7WkSh9dPnmajKivpZDpa0IzrGS/Ul4CgvLVX2Zd1C2McSyULIP9+WodjjF8x6XIRCx55f/aTP0Kj/59kXxa4+ECa/nyclaG3SMUVyZ38KwlrGF4venY4bQhM5FZPZVdlL6FHdXp1WIQSjw84c6HyQ8pK/eZ73lfPvwTWcDh09efSqDTEY0Mn2GTTm5PX76USmHo/ScBraK0x9j2qxkDaS5dBJjIOFHjXlNEtEoCgyZ6pawtIWkSq3EMeMIv5/Kbdl1QS06QGSeV4ZUq6XkXHLaOVJJlSp347J9/N3b3nKK9jdPAG7Fs1ZI9o1NrntyoKL2XE2/syvsYk1SYb7UGqEv0sfTSNb9ZmIFile+xwrMxGMmGhWTFO7PBxLojqTaStWJbm5cdYLTE5tRxOVNMjZiiJtXo+6qZuVtBNtnWTq0No3okJQY2fXAhkfUPuYvStBbkpvSav5YsQPfg2WSRGJyycQI2qCWXaiIq4NzsP0AMJ30bxRKVt40da+ww3fU+OY5w/EYTKEvfrpu9510nLeWRXXaTzkMc624o29zuLxd3c8cbSl2mNgk4GD28RR6kfZuYLacPHxRdG9E8dSdtBFGFCxZt1dEMJUYxYPeVmAH9wlBbeOKtrRlttuFYLzmHgfwS28z/3RZtewH0eItfGmQTCSlcLhwrY7jqDcIYFjms5a0xXjuE063nUZdKan9TKzilb5ZWQ85KsC5w3/GeZ81N058YYCg+55WV/dPVzjn03mInSlhH0z5dkqoeeFKChENyweAqbzvS0txQ+/qpOUmww+A8QL3PI3PBGDGpnNpKaxNE2UdvxvYRd/ilFZI9UED6eon7s56qH8GfoqHm7jSWcNtXMAsqR021Ns6Lc9vo6t8dgRTWAHHu33JJgcJ88AcVqPKJm2O5na/UJguydTOp7E1DW4wpWY8+gtuD7xXCu0wU/PzDKJnQkSuRLjvMIuwhw7cGV/s/slyO70CgW8PM8XzEz3LNw0m2DAoBVVnJxjLANG0hlIqvrG+9uWd1O4D7Dj0KbuMEjy6ijYcixkmuYPnoFwTIIkXBIu7nM8783kKhHHSMpIq+UQiGE/OT3N+guldKTBQODEqIJcnNRgoJiYYccS4ym+avKZm8l159iMg/ysHGebLjHIlpOARSyaEHC2m9AJW9yF88/yrt9Oze/rQgaHWLFQSfUv9Ua8HVTC6tUJ/dDy2y0piTmTjIauH4/uQmL1oiVskGfpzZ7SaeFqyM6z1ooeyaI3nmuonIlmk/KT6fF6vFlrx4ULoNYa2EvtbEaNkXQbnyq2FubvMv3601r2RqVr559O+TTMS2PW29pH0cBpQEYM+YZsKNKtq095w9bUIwuPESOdQ3Eb0C2Lxn3vxxmaZMUEH1EL687N4ik/byJk7xa2jp2pLpetBN7778LqYDaQHP0wY+8behaQBtsexS80mHrHlB2NnhZNCjhuhV4PHjL5ENUeAwlKCu1rmRZXEjfGHKeghy3j6ta3NUo2Np4tyj2RKVb3iyHeULlygf5NrDojhInJezejKyIb4R5y8pIGP4C+LaK4iJbJQS0jCElisNI62kcArbRp5wU/WXG3AFRfch3HRePdJxLUUMvfIHVZvI1ROCHpr4AW8bygVAO3iNI/8OPB+QaRwgXvC67+5a23E7FbOjYpk1vHBycJt8b6yNUHvZEgvIv5xlfq2qTpBPCI9R7xV4NsfR+JQ8kAbE5xLTyksWBKzf86aeG3zzQs2EUNYUl/JVRbhiNdrlOx4PoLOvqenEQp9VsflL9qdEzGk+EfNxiMg4t8qu1kibgtSSRYNCb8sV+GXzFvZvfleXCFgqxlOzn6+8/RdKu6CepObqcZqJjOHmOxc8daEGtEC8JBcFImV2p9DYLGwIS/Sdy1VV+r83LtMBayvXIvLcT/SuPQ6dKEARnDbOLNtbV3dDezB+1PS7qETnPiREJ/oTDHTUa62LqMGjMtWGBGSLd4HofBgOxmgNZaGa8bOo8NNHl/qlZr/2HBLgB+KWFSu57s4/p1hG3gzH/PfLacCEx4jYUQEY42sFCeYwfE+48VhX4qXX1QaUCkAk5TE+E/mA612BmLfJy1HxXemsKQ5VKHW6i8jHv0aFR91XYQj4Yg6Dmv9Mlpb18KhrjXhkhz8ULM/ccucppFbYm0QLQ3MWQ5dAyPRV28DCnsv8lznOgsYLfRpFdoe+VZWhz3MD/6wGFzIwwb/LMUNJ0QwTeeYzqBsdRdZZB9w/0dqqSzmskpzsLJd03pTedchBIhw38xD2HR+bT2jmlxC1OugM0q/Eah9UU2VSr0eNwk3iB8cq/jbbxXV1o5fxqqQX2oQ0fen7EBAUvl+lNceybuuay3BLECObevi5A+9xkWmCycSVkANlHj//YLA0mtt6NKqjWOEXXl/pUfMUXph+82gXUlr6dNn16TPDO/LOd0xnzflg9rubq/IOEj6+7V313M1IZHU3VJXL4FoPAPkOVYeEB3FLRfgx9u/ylWfl6aqW0IFNo2JgLi+yOEjY1nhNmj70PDcxYFIPaMIdCYFNbl2VLAgKT5xxX9Bnk7jxzUsGcmemic+le9G/dInDtJfdWO0LbAXKWsh/vadPfYJ/1Vz/e1ELbmypqi+btBf0UsfupLkwv6qyYoMuozLHThwuvcd5DkFU0v6Ypk/RTHbnG2+AuRVeokkxVtwS/kHRk+2gAl5bK3Polafh44mlOBRYZAETACDfRQbXtwd7TF8XlG2x+hFLqA4LlIxVxZCfEY9JNihdqfmv2QNpkogrVQqM1nReDpSU65bSgMQ5c591Kyh8FssgItTtStDSllcFs+WyTJ2y7oIHphgMn5MZvuU/+VQbMEIJw1f2hLT39AVE1rBESLeB2ryXWGdbG3S9pYf+vf64Fq9AGmjMTK80BWhFyWMPWb1aPPsi/bPCC49PhzKukUgu3ahQqUt8Z0d86NTWhgFKZciC9Fp8E6tGd7R11puvfU2JmATaVFDim1pmR6fUJDpSWA590MUCvyeJki8B/gD1bNQJhV51pLK5Ka2wBASMk+cdKg4SXpig09S8kIMVqkkoMCZfk358eQYCGQEcC0yXQzjLjBlLuh2Ip0nstghUBt+TYqhEQT+FnnXCWw6hHBMasbEUcNwGUAQqHNHfM388/uC7vYMc9gYJ+HhesnSRcOIMwHKDanx7TKguRDm0L/RghdMDNhyf6Twba2TkJ4+kkmijnfYp1YTYOU5M5tIfwu0gHRGStPXWYiIyzT7CKaJ8H+lbAOhGY2m4Cbr9s/6ubJv1zumrkpRvOAm7+xqwH+3g1CmWAo197Rz+VRUTGO7FIZVx2Mta4gIKECHuIzQyxRn9GG6OGKAzBFcAQw8xkswwUoFGF3YiwviIdbficCMdYDopk0lUZwQCnBYu4J3B8VVpc3lbhe/iXhGAzva1atAb0svLa4OUWrvxZShi4DKXjf/wAZ3Ab9HLGRylT3yCajixwxJFUTSjD+3I/VgpOJePSSNzxMe3BBUchA6QRqWvkQ/dQaDbInhm5aAgSocqLYtJMpiVH7jWlx7LqP7+aRzEOvPcWEvZU4kuNHPMqgGT2MS1MsoaEWF8v3aQOCI6BTKBgdbqjDC8hmZCEPei2on1naf6C6h9EBIOUmkNKtf8tXfTxUWjR2JPNe7SAV/yIuqzBmhIwQfqGfVYvs6vg3bHFS+TJDyCl0vPxNYSTI3PSUqCtBHYiZ6CW3yVxWuNgJsiB8rkUscF+X9lDyLwV7h8E5v5Px3nTHVC7rHi889FyynBgOibvski3/LjS7jx3hTWBqpJcSS9HuSBvvliMnnR5K2rnlA2fhNpKobZP6nJVWfgtowqxRU6/y8SkWcWBMpLF2gRb4h4DrjCptfXQL/6VLuTUBsntBr03i6eVZIzzdPJvVBpBBbWwWzHKSSHBJrnhHg+AVHbNTPXzrv+HXqp1+Pe6HAIxieXuDTzQde2R5Wf1i269deRTbypFdYD8p5R7Lv7PLw==',
  '__VIEWSTATEGENERATOR': 'CCB3C644',
  '__SCROLLPOSITIONX': '0',
  '__VIEWSTATEENCRYPTED': '',
  '__EVENTVALIDATION': 'RIxTO4vZ9zv4ZQ+brbGPsC/+J23bLD52QOIXSpqSG5cEqAR3ZTOv/LhWO4uQyXUylaEjZgEY5k/yBjegSA735ZGyuz/qkSp5O+dzWGKsTi2fVqINcdismpxIJmFYTRExg3RV2M7txzMdNL1ZxeYtzQMHJUlBP0DUVq7FgrLX/l+PJHgnfIxwAsaB8ItRzkmdWKB0PWN0vFQSz1kSsmnLLG+b4r5tiExSUMTxaOYxtDmUycKfLoHoWpNgFGeBCrUcSk4MscysC5x8rsHCJPkPtV4D7eqrGUCMX59WlYXZr1diGvJ7Fa34FrK+McJ2BF6I4jjHpnRmRbe0LvmARL+rPwvQoyJs58YbEP1cwiQhOwQHkIm3acyOciX7UCq/Wo0biccr/noINBV56MyAIPYFAHD0CW+jawrpjhW8LU8JRI8JKnb44oFfJ5hJ0ipW9E4wFP4mN8qaWk+qnGRdu/SA2OXlccVWp+/lVtu/LmX9ql8iQ5SR',
  'ctl00$PlaceHolderMain$uclSimpleSearch$txtSearchText': 'math',
  'ctl00$PlaceHolderMain$uclSimpleSearch$PagerIP$ddlTopSelect': '100'
}

response = requests.post('https://www.ip2.sg/RPS/WP/CM/SearchFastP.aspx', headers=headers, cookies=cookies, data=data)
document = BeautifulSoup(response.content, 'lxml')
odds = document.select('tr.odd')
evens = document.select('tr.even')
print(len(odds) + len(evens))