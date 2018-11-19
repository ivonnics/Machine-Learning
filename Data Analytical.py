# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:18:54 2018

@author: ivonnics
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn import preprocessing
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from pandas.plotting import scatter_matrix

url = "https://github.com/ivonnics/Machine-Learning/blob/master/CJD2.csv"
dataset = pd.read_html(url)
Tabla=dataset[0]
dataset=Tabla[['Date', 'Time', 'Volume']]

dataset1=[pd.to_datetime(hour, format="%I:%M:%S %p", errors="coerce") for hour in dataset['Time']]

print('-----------------------------------------------------------')
#print('TESTANDO')
dataset2=pd.Series(dataset1).dt.hour
#print(dataset2)
dataset3={'Hour': dataset2}
#print(dataset3)
dataset4=pd.DataFrame(dataset3, columns = ['Hour'])
#print(dataset4.head(20))

print(dataset.head(20))
print('-----------------------------------------------------------')
print(dataset.shape)
print('-----------------------------------------------------------')
print(dataset.describe())
print('-----------------------------------------------------------')


print(dataset.nunique())
print('-----------------------------------------------------------')

print('-----------------------------------------------------------')


df_new1= pd.concat([dataset, dataset4], axis=1)

print('-----------------------------------------------------------')
print(df_new1[(df_new1['Hour'] == 5)])
print('-----------------------------------------------------------')

dataset5=[pd.to_datetime(weekday, format="%m/%d/%Y", errors="coerce") for weekday in dataset['Date']]


dataset6=pd.Series(dataset5).dt.weekday_name
dataset7={'Weekday': dataset6}

dataset8=pd.DataFrame(dataset7, columns = ['Weekday'])

df_new2= pd.concat([df_new1, dataset8], axis=1)

df_new2['Madrugada'] = np.where((df_new2['Hour']>=0) & (df_new2['Hour']<6), 1, 0)
df_new2['Mañana'] = np.where((df_new2['Hour']>=6) & (df_new2['Hour']<12), 1, 0)
df_new2['Tarde'] = np.where((df_new2['Hour']>=12) & (df_new2['Hour']<18), 1, 0)
df_new2['Noche'] = np.where((df_new2['Hour']>=18) & (df_new2['Hour']<24), 1, 0)
df_new2['Lunes'] = np.where((df_new2['Weekday']=='Monday'), 1, 0)
df_new2['Martes'] = np.where((df_new2['Weekday']=='Tuesday'), 1, 0)
df_new2['Miércoles'] = np.where((df_new2['Weekday']=='Wednesday'), 1, 0)
df_new2['Jueves'] = np.where((df_new2['Weekday']=='Thursday'), 1, 0)
df_new2['Viernes'] = np.where((df_new2['Weekday']=='Friday'), 1, 0)
df_new2['Sábado'] = np.where((df_new2['Weekday']=='Saturday'), 1, 0)
df_new2['Domingo'] = np.where((df_new2['Weekday']=='Sunday'), 1, 0)


print(df_new2.shape)
print(df_new2.head(20))


df_new3=df_new2[['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo', 'Madrugada', 'Mañana', 'Tarde', 'Noche', 'Volume']]

#Analysis
print(df_new3.shape)
print(df_new3.head(20))
print(dataset.describe())
print(df_new2.groupby('Weekday').size())
print(df_new3.groupby('Madrugada').size())
print(df_new3.groupby('Mañana').size())
print(df_new3.groupby('Tarde').size())
print(df_new3.groupby('Noche').size())
print(df_new3.groupby('Volume').size())
# box and whisker plots
df_new3.plot(kind='box', subplots=True, layout=(4,3), sharex=False, sharey=False)
plt.show()
# histograms
df_new3.hist()
plt.show()
# scatter plot matrix
scatter_matrix(df_new3)
plt.show()

# Split-out validation dataset
array = df_new3.values
X = array[:,0:11]
#print(X)
Y = array[:,11]


#print(Y)
lab_enc = preprocessing.LabelEncoder()
encoded = lab_enc.fit_transform(Y)
Y=encoded
#print(Y)
print('')

validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


num_folds = 10
num_instances = len(X_train)
seed = 7
scoring = 'accuracy'


models = []

models.append(('LR', LogisticRegression())) #FUNCIONA!!!
models.append(('KNN', KNeighborsClassifier())) #FUNCIONA!!!
models.append(('CART', DecisionTreeClassifier())) #FUNCIONA!!!
models.append(('NB', GaussianNB())) # FUNCIONA!!!
models.append(('SVM', SVC())) #FUNCIONA!!!
# evaluate each model in turn
results = []
names = []

for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
    

# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()


# Make predictions on validation dataset
Modelo_a_Usar = LogisticRegression()
Modelo_a_Usar.fit(X_train, Y_train)
predictions = Modelo_a_Usar.predict(X_validation)
print('Accuracy_score: ')
print(accuracy_score(Y_validation, predictions))
print('Confusion_matrix:')
print(confusion_matrix(Y_validation, predictions))
print('Classification_report:')
print(classification_report(Y_validation, predictions))
