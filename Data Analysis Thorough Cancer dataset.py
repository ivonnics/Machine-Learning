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
url = "C:\\Users\\ivonnics\\Documents\\JOSE LUIS\\Cursos Cursera\\Machine Learning\\cancer.csv"
names = ['class','age','menopause','tumor-size','inv-nodes','node-caps','deg-malig','breast','breast-quad','irradiat'
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
print('Dataset First Attribute (class) Description:')
print(dataset.groupby('class').size())
print('--------------------------------------------------------------------')
print('Dataset Second Attribute (tumor-size) Description:')
print(dataset.groupby('tumor-size').size())
print('--------------------------------------------------------------------')
print('Dataset Third Attribute (deg-malig) Description:')
print(dataset.groupby('deg-malig').size())
print('--------------------------------------------------------------------')
print('Dataset Fourth Attribute (age) Description:')
print(dataset.groupby('age').size())
print('--------------------------------------------------------------------')
print('Dataset Fifth Attribute (menopause) Description:')
print(dataset.groupby('menopause').size())
print('--------------------------------------------------------------------')
print('Dataset Sixth Attribute (inv-nodes) Description:')
print(dataset.groupby('inv-nodes').size())
print('--------------------------------------------------------------------')
print('Dataset Sixth Attribute (node-caps) Description:')
print(dataset.groupby('node-caps').size())
print('--------------------------------------------------------------------')
print('Dataset Sixth Attribute (breast) Description:')
print(dataset.groupby('breast').size())
print('--------------------------------------------------------------------')
print('Dataset Sixth Attribute (breast-quad) Description:')
print(dataset.groupby('breast-quad').size())
print('--------------------------------------------------------------------')
print('Dataset Sixth Attribute (irradiat) Description:')
print(dataset.groupby('irradiat').size())
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
Housing.plot(kind='scatter', x='age', y='tumor-size', alpha=0.1)
Housing.plot(kind='scatter', x='age', y='tumor-size', alpha=0.4)
Housing.plot(kind='scatter', x='age', y='tumor-size', alpha=0.8)
Housing.plot(kind="scatter", x="tumor-size", y="deg-malig", alpha=0.4,
    s=Housing["inv-nodes"]/100, label="population", figsize=(10,7),
    c="node-caps", cmap=plt.get_cmap("jet"), colorbar=True,
    sharex=False)
