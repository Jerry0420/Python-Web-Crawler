import requests

headers = {
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
}

params = (
    ('x-algolia-application-id', 'FGVI612DFZ'),
    ('x-algolia-api-key', 'NDI2YWY5NjgyY2FjOWE0MTkyODI2YTI4OGZhNmRkOTE4ZWUxMjBhMTA3NzFkMGE1MDVkZmViOGQwZjcwNmYxOXZhbGlkVW50aWw9MTU5MzQyNjgzNQ=='),
)

# hitsPerPage = 80
# maxValuesPerFacet = 10
# page = 0

# data = '{"requests":[{"indexName": "fragrantica_perfumes","params":"hitsPerPage=80&maxValuesPerFacet=10&page=34&attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22godina%22%2C%22url.EN%22%2C%22thumbnail%22%5D&facets=%5B%22spol%22%2C%22dizajner%22%2C%22godina%22%2C%22ingredients.EN%22%2C%22rating_rounded%22%2C%22nosevi%22%2C%22osobine.EN%22%2C%22designer_meta.country%22%2C%22designer_meta.category%22%2C%22designer_meta.parent_company%22%2C%22designer_meta.main_activity%22%5D"}]}'
data = '{"requests":[{"indexName":"fragrantica_perfumes","params":"hitsPerPage=80&maxValuesPerFacet=10&page=0&attributesToRetrieve=%5B%22naslov%22%2C%22dizajner%22%2C%22godina%22%2C%22url.EN%22%2C%22thumbnail%22%5D&facets=%5B%22spol%22%2C%22dizajner%22%2C%22godina%22%2C%22ingredients.EN%22%2C%22rating_rounded%22%2C%22nosevi%22%2C%22osobine.EN%22%2C%22designer_meta.country%22%2C%22designer_meta.category%22%2C%22designer_meta.parent_company%22%2C%22designer_meta.main_activity%22%5D&facetFilters=%5B%5B%22nosevi%3AAlberto%20Morillas%22%5D%5D"}]}'

response = requests.post('https://fgvi612dfz-3.algolianet.com/1/indexes/*/queries', headers=headers, params=params, data=data)

print(response.json()['results'][0]['hits'][0])
print(response.json()['results'][0]['hits'][0]['naslov'])
print(len(response.json()['results'][0]['hits']))


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