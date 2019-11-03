from monkeylearn import MonkeyLearn
import csv
import pyodbc

counter = 0
data = []
data_c =[]
with open ('News/Coca-Cola HBC @table.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row['Content'])
    data_c.append(row['Date'])
ml = MonkeyLearn('52e394b68a5e929171a857dbf367ac33e2a33d87')
model_id = 'cl_hjWQJktS'
response = ml.classifiers.classify(model_id, data)
#print(response.body)
for i in range(0, len(response.body) - 1):
    print(response.body[i]['classifications'][0]['tag_name'])
    print(response.body[i]['classifications'][0]['confidence'])

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-PJUGJ1U;'
                      'Database=Statistica;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
for i in range(0,len(response.body)):
    cursor.execute("INSERT INTO Statistica.dbo.News(Date, Clasification, Confidence) values(? ,?, ?)", str(data_c),str(response.body[i]['classifications'][0]['tag_name']),str(response.body[i]['classifications'][0]['confidence']))
cursor.commit()
conn.close()


