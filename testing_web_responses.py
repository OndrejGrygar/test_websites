import requests
import json
from bs4 import BeautifulSoup
import time
import threading

with open("websites_dict.json") as file:
    content = json.load(file)
print(content)

def response(y):
    try:
        response = requests.get(y)
        print("Response of website", y, response.ok)

        soup = BeautifulSoup(response.content, 'html.parser')
        tag = soup.find("title")
        print("Tag Title of website:", tag)
        #time.sleep(4)
    except Exception:
        print(y, "wrong Url is provided or server is down")
        #time.sleep(4)
        pass

while True:
    for key,value in content.items():
        for i in value:
            for value1 in i.values():
                x = threading.Thread(target=response(value1))
                x.start()
                time.sleep(4)

