import requests
import pprint
import datetime as dt
import csv

secret = '5bb3787fc79f4eff859893265aebb265'
url = 'https://newsapi.org/v2/everything?'

company_name = 'Vodafone Group'

parameters = {
    'q': 'company_name',
    'pageSize': 20,
    'apiKey': secret
}



response = requests.get(url, params=parameters)

response_json = response.json()


pprint.pprint(response_json)

def cut_date(date):
    text = ""
    for i in range(0, 10):
        text += date[i]
    return text


def search_content(content):
    words_in_table = []
    if content is not None:
        words_in_table = content.split()
    for i in words_in_table:
        if i.lower() == company_name:
            return True
    return False


with open(company_name + "@table.csv", 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile)
    filewriter.writerow(['Date', 'Content','Prediction'])
    for i in response_json['articles']:
        #if search_content(i['content']) == True:
        filewriter.writerow([cut_date(i['publishedAt']), i['content'],'None'])

# with open(company_name + "table.csv", 'w',newline='') as csvfile:
#     filewriter = csv.writer(csvfile)
#     filewriter.writerow(['Site', 'Titlu', 'Paragraph', 'Data','None'])
#     for i in table:
#         aux = get_data(i)
#         print(aux.date)
#         print(aux.title)
#         print(aux.paragraph)
#         print(aux.site_name)
#         try:
#             filewriter.writerow([aux.site_name, aux.title, aux.paragraph, aux.date])
#         except:
#             continue
