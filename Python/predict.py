import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import pandas as pd
import csv
import pyodbc


with open('Companies/Vodafone Group.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    df = pd.DataFrame(reader)

# Get the Adjusted Close Price
df = df[['Adj Close']]

# A variable for predicting 'n' days out into the future
forecast_out = 7 #'n=30' days
#Create another column (the target ) shifted 'n' units up
df['Prediction'] = df[['Adj Close']].shift(-forecast_out)
#print the new data set
#print(df.tail())

### Create the independent data set (X)  #######
# Convert the dataframe to a numpy array
X = np.array(df.drop(['Prediction'],1))

#Remove the last '30' rows
X = X[:-forecast_out]
print(X)

### Create the dependent data set (y)  #####
# Convert the dataframe to a numpy array
y = np.array(df['Prediction'])
# Get all of the y values except the last '30' rows
y = y[:-forecast_out]
print(y)

# Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)

# Testing Model: Score returns the coefficient of determination R^2 of the prediction.
# The best possible score is 1.0
svm_confidence = svr_rbf.score(x_test, y_test)
print("svm confidence: ", svm_confidence)

# Create and train the Linear Regression  Model
lr = LinearRegression()
# Train the model
lr.fit(x_train, y_train)

# Testing Model: Score returns the coefficient of determination R^2 of the prediction.
# The best possible score is 1.0
lr_confidence = lr.score(x_test, y_test)
print("lr confidence: ", lr_confidence)

# Set x_forecast equal to the last 30 rows of the original data set from Adj. Close column
x_forecast = np.array(df.drop(['Prediction'],1))[-forecast_out:]
print(x_forecast)

# Print linear regression model predictions for the next '30' days
lr_prediction = lr.predict(x_forecast)
svm_prediction = svr_rbf.predict(x_forecast)

print(lr_prediction)# Print support vector regressor model predictions for the next '30' days

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-PJUGJ1U;'
                      'Database=Statistica;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


for i in lr_prediction:
    cursor.execute("INSERT INTO Statistica.dbo.Predictions(StockValue, CompanyName) values(? ,?)", str(i),'Vodafone Group')
    cursor.commit()
conn.close()
