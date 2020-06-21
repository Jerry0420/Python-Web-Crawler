import json

perfumes = {}
files = [
    'fragrantica_2020-06-21_00-44-58.json',
    'fragrantica_2020-06-21_01-20-13.json',
    'fragrantica_2020-06-21_01-33-29.json',
    'fragrantica_2020-06-21_01-37-28.json',
    'fragrantica_2020-06-21_01-40-57.json',
    'fragrantica_2020-06-21_01-43-30.json',
]
for file in files:
    with open(file,'r') as f:
        file_content = json.loads(f.read())
        for i in file_content:
            perfumes[i['product_id']] = i

with open('results.json','w' , encoding='utf-8') as f:
    json.dump(perfumes, f, ensure_ascii=False)

# with open('results.json', 'r') as f:
#     file_content = json.loads(f.read())
#     for key, value in file_content.items():
#         print(value)