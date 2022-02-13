from urlparse import urlparse
from threading import Thread
import sys
from Queue import Queue
import requests
import json
import socket, ssl


PORT = 443
#cd OneDrive/Desktop && c:/Python27/python.exe pyt.py dddddddddddd


print "Usage: Python2 run.py login-jwt file.txt (file.txt contains the json body)"

def post(url):
   headers = {"Content-Type":"application/json","Connection":"Close","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36","Cookie":"connect.sid=s%3A3vC0ItHuTyxpM2pAArc_KnxRzFtBlfts.3UFhTuv4nUScdJpTUroEwHPmxeS5rUD6QiLAzcliS5g"}
   re = requests.post('https://app.enzyme.finance/api/graphql',headers=headers,data=url)
   try :
      print "\r\n\r\n\r\n\r\n\r\n\r\nThe Session COOKIE : "+str(re.headers["cookie"])+"\r\n\r\n\r\n\r\n\r\n\r\n"
      print str(re.text)
   except Exception as e :
      print "working on, received response : " + str(re.status_code) + " with length of "+str(len(re.text))


def start_all():
    while True:
        url = q.get()
        post(url)
        q.task_done()


q = Queue(5)
for i in range(10):
    t = Thread(target=start_all)
    t.daemon = True
    t.start()

try:
    file = open(sys.argv[2], 'r')
    for datas in file:
        data = datas.replace("ssss",sys.argv[1])
        q.put(data)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
