import requests
import json
from bs4 import BeautifulSoup
import time
import threading

with open("websites_dict.json") as file:
    content = json.load(file)
print(content)

def get_url_list(content):
    list = []
    for key, value in content.items():
        for i in value:
            for value1 in i.values():
                list.append(value1)
        return list

y = get_url_list(content)
class MyThread(threading.Thread):
    def __init__(self, number):
        super(MyThread, self).__init__()
        self.number = number
    def run(self):
        while True:
            try:
                response = requests.get(y[self.number])
                soup = BeautifulSoup(response.content, 'html.parser')
                tag = soup.find("title")
                print("Response of website", y[self.number], " with Tag Title of website:", tag, "is: ", response.ok, )
                time.sleep(4)
            except Exception:
                print(y[self.number], "wrong Url is provided or server is down")
                time.sleep(4)

created_Threads = []
startTime = time.time()

for i in range(len(y)):
    created_Thread = MyThread(i)
    created_Threads.append(created_Thread)
    created_Thread.start()
print(created_Threads)


endTime = time.time()
print('Took %s seconds'%(endTime - startTime))


