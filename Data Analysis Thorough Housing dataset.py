# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 19:44:39 2018

@author: ivonnics
"""
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#Load data
url = "C:\\Users\\ivonnics\\Documents\\JOSE LUIS\\Cursos Cursera\\Machine Learning\\housing.csv"
names = ['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value','ocean_proximity'
]
dataset = pandas.read_csv(url, names=names)
print('Dataset:')
print(dataset)

#Analysis
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('Dataset Shape:')
print(dataset.shape)
print('--------------------------------------------------------------------')
print('Dataset Info:')
print(dataset.info)
print('--------------------------------------------------------------------')
print('Dataset First 20 Lines:')
print(dataset.head(20))
print('--------------------------------------------------------------------')
print('Dataset Statitical description:' )
print(dataset.describe())
print('--------------------------------------------------------------------')
print('Dataset First Attribute (median_house_value) Description:')
print(dataset.groupby('median_house_value').size())
print('--------------------------------------------------------------------')
print('Dataset Second Attribute (housing_median_age) Description:')
print(dataset.groupby('housing_median_age').size())
print('--------------------------------------------------------------------')
print('Dataset Third Attribute (ocean_proximity) Description:')
print(dataset.groupby('ocean_proximity').size())
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
# box and whisker plots
print('Box and whisker plots:')
dataset.plot(kind='box', subplots=True, layout=(3,4), sharex=False, sharey=False)
plt.show()
print('--------------------------------------------------------------------')
# histograms
print('Histograms:')
dataset.hist()
plt.show()
print('--------------------------------------------------------------------')
# scatter plot matrix
print('Scatter plot matrix:')
scatter_matrix(dataset)
plt.show()
print('--------------------------------------------------------------------')
Housing = dataset.copy()
print('Correlation between attributes:')
Housing.plot(kind='scatter', x='total_rooms', y='total_bedrooms', alpha=0.1)
Housing.plot(kind='scatter', x='total_rooms', y='total_bedrooms', alpha=0.4)
Housing.plot(kind='scatter', x='total_rooms', y='total_bedrooms', alpha=0.8)
Housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
    s=Housing["population"]/100, label="population", figsize=(10,7),
    c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
    sharex=False)
