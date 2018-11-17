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
url = "C:\\Users\\ivonnics\\Documents\\JOSE LUIS\\Cursos Cursera\\Machine Learning\\Diabetes.csv"
names = ['pregnancies', 'glucose', 'blood-pressure', 'skin-thickness', 'insulin', 'BMI', 'diabetes-pedigree-function', 'age', 'class']
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
print('Dataset First Attribute (class) Description:')
print(dataset.groupby('class').size())
print('--------------------------------------------------------------------')
print('Dataset Second Attribute (pregnancies) Description:')
print(dataset.groupby('pregnancies').size())
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
# box and whisker plots
print('Box and whisker plots:')
dataset.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
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
diabetes = dataset.copy()
diabetes.plot(kind='scatter', x='skin-thickness', y='BMI', alpha=0.1)
diabetes.plot(kind='scatter', x='skin-thickness', y='BMI', alpha=0.4)
diabetes.plot(kind='scatter', x='skin-thickness', y='BMI', alpha=0.8)
