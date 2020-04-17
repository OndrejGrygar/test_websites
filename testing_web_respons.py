import requests
import json
from bs4 import BeautifulSoup
import time

with open("websites_dict.json") as file:
    content = json.load(file)
print(content)

while True:
    for key,value in content.items():
        for i in value:
            for key1, value1 in i.items():
                try:
                    response = requests.get(value1)
                    print("Response of website", value1, response.ok)

                    soup = BeautifulSoup(response.content, 'html.parser')
                    tag = soup.find("title")
                    print("Tag Title of website:", tag)
                    time.sleep(4)
                except Exception:
                    print(value1, "wrong Url is provided or server is down")
                    time.sleep(4)
                    continue


