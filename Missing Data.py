# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:17:54 2018

@author: ivonnics
"""

# binary classification, missing data
from pandas import read_csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
# load data
url = "C:\\Users\\ivonnics\\Documents\\JOSE LUIS\\Cursos Cursera\\Machine Learning\\Horse Colic.csv"
dataframe = read_csv(url, header=None)
dataset = dataframe.values
print(dataset)
print("")
# split data into X and y
X = dataset[:,0:27]
Y = dataset[:,27]
print(X)
print(Y)
# set missing values to 0
X[X == '?'] = 1
# convert to numeric
X = X.astype('float32')
print(X)
# encode Y class values as integers
label_encoder = LabelEncoder()
label_encoder = label_encoder.fit(Y)
label_encoded_y = label_encoder.transform(Y)
# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, label_encoded_y, test_size=test_size, random_state=seed)
# fit model no training data
model = KNeighborsClassifier()
model.fit(X_train, y_train)
print(model)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))