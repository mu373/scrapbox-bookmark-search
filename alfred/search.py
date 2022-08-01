import json
import urllib.parse
import requests
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--token')
parser.add_argument('--query')
parser.add_argument('--project')

args = parser.parse_args()
token = args.token
query = args.query
project = args.project

cookies = {
    'connect.sid': token
}

query_encoded=urllib.parse.quote(query)
api_url="https://scrapbox.io/api/pages/{}/search/query?q={}".format(project, query_encoded)
response = requests.get(api_url, cookies=cookies).json()

titles = [page['title'] for page in response['pages']]

result = {
    "items": []
}

for title in titles:
    item = {
        "title": "{}".format(title),
        "arg": "{}".format(
            urllib.parse.quote(title, safe='', encoding='utf-8')
        )
        # "subtitle": "Scrapbox Bookmark",
        # "icon": {
        #     "type": "fileicon",
        #     "path": "~/Desktop"
        # }
    }
    result['items'].append(item)

result_json = json.dumps(result, ensure_ascii=False)
print(result_json)



