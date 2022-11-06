from urllib import response

#3.9 pythonnal megy!!
import urllib
import requests
import re
import string
from time import *

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
passwd = list()

username = 'natas18'
password = '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq'
leakedPassword = ''       

url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username

session = requests.Session()
reponse = session.get(url , auth=(username, password))
content = reponse.text
print(content)        
    



#$(grep b /etc/natas_webpass/natas17)