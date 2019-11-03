import requests
from bs4 import BeautifulSoup
from GoogleNews import GoogleNews
from urllib.parse import urlparse
import articleDateExtractor
import calendar
import re


URL = 'https://www.google.co.in/search?q=Aviva+news+financial&source=lnms&tbm=nws&sa=X&ved=0ahUKEwj4ptniy8zlAhVu16YKHbZvBT8Q_AUIEigB&biw=1536&bih=706&as_qdr=d'

headers = {"User - Agent" :'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

page = requests.get(URL,headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

for i in soup.find_all('a'):
   print(i)

#print(soup.text)