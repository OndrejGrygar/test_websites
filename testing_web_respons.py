import requests
import json
from bs4 import BeautifulSoup

with open("websites_dict.json") as file:
    content = json.load(file)
print(content)

for key,value in content.items():
    for i in value:
        for key,value in i.items():
            response = requests.get(value)
            print("Response of website", value, response.ok)
            soup = BeautifulSoup(response.content, 'html.parser')
            tag = soup.find("title")
            print(tag)

