import json
import urllib.parse
import requests
import re
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--token')
parser.add_argument('--title')
parser.add_argument('--project')

args = parser.parse_args()

token = args.token
title = args.title
project = args.project

cookies = {
    'connect.sid': token
}

api_url="https://scrapbox.io/api/pages/{}/{}".format(project, title)
# print(api_url, end="")

response = requests.get(api_url, cookies=cookies).json()

descriptions = response['descriptions']
link_text = [item for item in descriptions if 'http' in item][0] #リンクが含まれる行を抽出
url = re.findall(r'(https?://\S+)', link_text)[0] #URLだけ抽出

print(url, end="")
