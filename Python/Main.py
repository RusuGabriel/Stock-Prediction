from textblob import  TextBlob
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import articleDateExtractor


URL = 'https://www.bbc.com/news/topics/crr7mlg0vg2t/vodafone'

headers = {"User - Agent" :'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

page = requests.get(URL,headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.text)

title = soup.title

textP = soup.find_all('p')[0].text

rez = ""

for i in soup.find_all('p'):
    rez += i.text

#gaseste numele site-ului din url
site_name = urlparse(URL).hostname

print(site_name)

print("{}".format(articleDateExtractor.extractArticlePublishedDate("http://techcrunch.com/2015/11/29/tyro-payments/")))

print(title)

print(rez)