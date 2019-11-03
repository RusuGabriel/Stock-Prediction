import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import datetime as dt
from htmldate import find_date
import csv


class WebPage:
    def __init__(self, date, title, site_name, paragraph):
        self.date = date
        self.title = title
        self.site_name = site_name
        self.paragraph = paragraph

    def get_date(self):
        return self.date


company_name = input("company name : ")
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = company_name + " financial news"

table = []

for i in search(query, tld="com", num=30, stop=30, pause=30):
    date_txt = find_date(i)
    date_obj = ''
    try:
        date_obj = dt.datetime.strptime(date_txt, '%Y-%m-%d')
        if date_obj.year < 2019:
            continue
    except:
        continue
    table.append(i)


def get_data(URL):
    headers = {"User - Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.title
    rez = ""
    site_name = urlparse(URL).hostname
    date = find_date(URL)

    for i in soup.find_all('p'):
        rez += i.text

    final = WebPage(date, title, site_name, rez)
    return final


datetable = []
j = 0
with open(company_name + "table.csv", 'w',newline='') as csvfile:
    filewriter = csv.writer(csvfile)
    filewriter.writerow(['Date', 'Content', 'Prediction'])
    for i in table:
        aux = get_data(i)
        print(aux.date)
        print(aux.title)
        print(aux.paragraph)
        print(aux.site_name)
        try:
            filewriter.writerow([aux.date,aux.paragraph,'None'])
        except:
            continue
