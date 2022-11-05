from cgitb import text
from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re
import base64

import json




username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'


#headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
url = 'http://%s.natas.labs.overthewire.org/' % username

reponse = requests.get(url , auth=(username, password))
content = reponse.text
print(content)

#A sütik XOR kódolással vannak védve. Nézzük meg a kódot.

url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username

reponse = requests.get(url , auth=(username, password))
content = reponse.text
print(content)

#Irassuk ki a süti tartalmát is

print('')
print('Süti kiratása')
url = 'http://%s.natas.labs.overthewire.org/' % username

sess = requests.session()
reponse = sess.get(url , auth=(username, password))
content = reponse.text
print(sess.cookies)

"""
Amit tudunk : XOR-al kódolt sütik, amit egy a PHP-ben található loaddata függvény kódol. Van a kódban egy $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
változó, ami az alapértéket mutatja. A jelszó akkor fog megjelenni, ha a showpassword = yes.
PoC
Mivel a kulcsot nem ismerjük, de van egy kódolt és egy plaintext adatunk ebből meg lehet határozni a kulcsot. Ha ez megvan akkor a megfelelő süti értéket vissza kell
kódolni és ezeket az adatokat kell beküldeni.
"""

plainTextData = {"showpassword":"no","bgcolor":"#ffffff"}
#Ezt JSON formába át kell rakni.
JSONPlainData = str(json.dumps(dict(plainTextData)))
#print(JSONPlainData)
#Most dekódoljuk base64-ből az eredeti sütit
OriginalCookie = 'MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D'
OriginalCookieHTMLDecoded = ''
for char in OriginalCookie:
    if char != '%':
        OriginalCookieHTMLDecoded += char
    else:
        OriginalCookieHTMLDecoded += '='
        break

#Ez lesz az az XOR kódolt sztring, amit a kulcs kereséséhez fogunk használni
OriginalCookieDecBase64 = str(base64.b64decode(OriginalCookieHTMLDecoded))


"""
XOR
plain XOR key = cipher
plain XOR cipher = key
azaz JSONPlainData XOR OriginalCookieDecBase64 = key

    //$key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
"""

def enc_XOR(input, key) :

    #$key = '<censored>';
    text = input
    outText = ''
    # Iterate through each character
    i = 0
    while ( i < len(text) ) :
        outText += chr(ord(text[i]) ^ ord(key[i % len(key)]))
        i+=1
    
    return outText

def enc_XOR2(input, key) :

    #$key = '<censored>';
    text = input
    outText = ''
    # Iterate through each character
    i = 0
    while ( i < len(text) ) :
        outText += chr((text[i]) ^ (key[i % len(key)]))
        i+=1
    
    return outText

Key1 = 'KNHL'
# print(Key1) 
# print(plainTextData)
print(enc_XOR2(JSONPlainData.encode(),OriginalCookieDecBase64.encode()))
print(JSONPlainData)
# InjectedData = '{"showpassword":"yes", "bgcolor":"#ffffff"}'
# JSONInjectedData = str(simplejson.loads(InjectedData))
# CookieData = base64.b64encode(enc_XOR(InjectedData,Key1).encode())
# print(CookieData)



# Payload = {"data" : "MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmhuKSkrIychOm5xbGsqLSguKi1sNQ=="}


# url = 'http://%s.natas.labs.overthewire.org/' % username
# session = requests.Session()
# reponse = session.get(url , auth=(username, password),cookies=Payload)
# content = reponse.text
# print(content)