# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:23:16 2018

@author: ivonnics
"""

from sklearn import datasets
#Loading iris
iris = datasets.load_iris()
print (iris.data)
print("")
print("")
# Loading digits
digits = datasets.load_digits()
print (digits.data)

