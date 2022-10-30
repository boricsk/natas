from urllib import response
#3.9 pythonnal megy!!

import requests
import re

username = 'natas0'
password = username

url = 'http://%s.natas.labs.overthewire.org/' % username

reponse = requests.get(url, auth=(username, password)).text

print(reponse)
