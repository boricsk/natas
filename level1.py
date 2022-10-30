from urllib import response
#3.9 pythonnal megy!!

import requests
import re

username = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'

url = 'http://%s.natas.labs.overthewire.org/' % username

reponse = requests.get(url, auth=(username, password))
content = reponse.text

#keresés a tartalomban. A (.*) a helyettesítő karakter. ami itt van az eredetiban azt figyelman kívül fogja hagyni.
#print(re.findall('<!--The password for natas2 is (.*) -->' ,content))

print(content)