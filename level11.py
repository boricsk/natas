from urllib import response
#3.9 pythonnal megy!!
#import urllib3
import requests
import re

username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'

#headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

#cookie_ = {"loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
#print(session)

#reponse = requests.get(url, auth=(username, password), headers=headers)
reponse = requests.get(url , auth=(username, password))

#a print cookie data
print(session.cookies['data'])
#POST request
#reponse = requests.post(url, data={"needle": ". cat /etc/natas_webpass/natas11 #","submit": "submit"}, auth=(username, password))

#a sessionhoz hozzarendelt get keres
#reponse = session.get(url, auth=(username, password), cookies=cookie_)

#content = reponse.text

#indexelni is lehet
#print(session.cookies['loggedin'])

#kereses a tartalomban. A (.*) a helyettesito karakter. ami itt van az eredetiban azt figyelman kivul fogja hagyni.
#print(re.findall('natas11(.*)' ,content))

#print(content)