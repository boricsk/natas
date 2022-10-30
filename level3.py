from urllib import response
#3.9 pythonnal megy!!

import requests
import re

username = 'natas3'
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

reponse = requests.get(url, auth=(username, password))
content = reponse.text

#keresés a tartalomban. A (.*) a helyettesítő karakter. ami itt van az eredetiban azt figyelman kívül fogja hagyni.
#print(re.findall('natas3:(.*)' ,content))

print(content)