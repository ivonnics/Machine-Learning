# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:23:13 2018

@author: ivonnics
"""

from sklearn.externals import joblib

# load the model from disk
filename = 'finalized_Iris Test.sav'
loaded_model = joblib.load(filename)
Xnew = [[6.9, 3.2, 5.7, 2.3]]
# make a prediction
ynew = model.predict(Xnew)
# show the inputs and predicted outputs
for i in range(len(Xnew)):
	print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))