from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re


username = 'natas12'
password = 'YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
reponse = session.get(url , auth=(username, password))

content = reponse.text

print(content)