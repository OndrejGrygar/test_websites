import requests
import json
from bs4 import BeautifulSoup

with open("websites_dict.json") as file:
    content = json.load(file)
print(content)

for key,value in content.items():
    for i in value:
        for key1,value1 in i.items():
            response = requests.get(value1)
            print("Response of website", value1, response.ok)
            soup = BeautifulSoup(response.content, 'html.parser')
            tag = soup.find("title")
            print(tag)

