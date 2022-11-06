from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re
import string
from time import *

username = 'natas20'
password = 'guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
#reponse = session.post(url , data= {"username": "admin", "password": "letmei" }, auth=(username, password))
reponse = session.get(url, auth=(username, password))
content = reponse.text
    
print(content)
