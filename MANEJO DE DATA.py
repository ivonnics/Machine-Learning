# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:15:32 2018

@author: ivonnics
"""

import pandas as pd
import numpy as np
url = "C:\\Users\\ivonnics\\Documents\\JOSE LUIS\\Cursos Cursera\\Machine Learning\\titanic.csv"
names = ['Name', 'PCClass', 'Age', 'Sex', 'Survived', 'SexCode']
dataset = pd.read_csv(url, names=names)
dataframe=dataset

print(dataframe.head(5))

print(dataframe.shape)

print(dataframe.describe())

print(dataframe.iloc[0])
print(dataframe.iloc[1:4])
print(dataframe.iloc[:4])
dataframe=dataframe.set_index(dataframe['Name'])

print(dataframe.loc["Aubert, Mrs Leontine Pauline"])
print(dataframe[dataframe['Sex'] == 'female'].head(2))
print(dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >= 65)])
print(dataframe.count())
print(dataframe['Sex'].unique())
print(dataframe['Sex'].value_counts())
print(dataframe['PCClass'].nunique())
print(dataframe['PCClass'].unique())
print(dataframe['PCClass'].value_counts())
print(dataframe[dataframe['Age'].isnull()].head(2))

url = "C:\\Users\\ivonnics\\Documents\\JOSE LUIS\\Cursos Cursera\\Machine Learning\\diabetes.xlsx"

dataset1 = pd.read_excel(url, sheet_name=0, header=0)
print(dataset1.head(2))