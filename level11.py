#3.9 pythonnal megy!!
from urllib.parse import unquote
import requests
import re
import base64

username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'


#headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
url = 'http://%s.natas.labs.overthewire.org/' % username

reponse = requests.get(url , auth=(username, password))
content = reponse.text
print(content)

#A sütik XOR kódolással vannak védve. Nézzük meg a kódot.

url = 'http://%s.natas.labs.overthewire.org/' % username

reponse = requests.get(url , auth=(username, password))
content = reponse.text
print(content)

#Irassuk ki a süti tartalmát is

print('')
print('Süti kiratása')
url = 'http://%s.natas.labs.overthewire.org/' % username

sess = requests.session()
reponse = sess.get(url , auth=(username, password))
content = reponse.text
print(base64.b64decode(unquote(sess.cookies['data'])).hex())

Payload = {"data" : "MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz"}


url = 'http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
reponse = session.get(url , auth=(username, password),cookies=Payload)
content = reponse.text
print(content)