# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:42:11 2018

@author: ivonnics
"""

import pandas as pd

#Load data
url = "https://github.com/ivonnics/Machine-Learning/blob/master/CJDORIG.csv"
#url = "C:\\Users\\ivonnics\\Documents\\JOSE LUIS\\Cursos Cursera\\Machine Learning\\CJD2.csv"
dataset = pd.read_html(url)
Tabla=dataset[0]
print(Tabla.head(20))
dataset=Tabla[['Date', 'Time', 'Volume']]
print(dataset.head(20))
