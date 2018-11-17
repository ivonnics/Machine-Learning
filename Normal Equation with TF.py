# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:08:02 2018

@author: ivonnics
"""
import tensorflow as tf
import numpy as np

url = "C:\\Users\\ivonnics\\Documents\\JOSE LUIS\\Cursos Cursera\\Machine Learning\\Ex NE TF.csv"

dataset = np.loadtxt(url, delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:4]
print(X)
Y = dataset[:,4]
print(Y)



housing = dataset
print(housing)
m, n = housing.data.shape
print(housing.data.shape)
housing_data_plus_bias = np.c_[np.ones((m, 1)), housing.data]

X1 = X
y = Y
XT = tf.transpose(X1)
print(XT)
paso1=tf.matmul(XT, X1)
print(paso1)
paso2= tf.matrix_inverse(paso1)
print(paso2)
paso3=tf.matmul(paso2, XT)
print(paso3)

logits = y.reshape(-1, 1)
print(logits)
y=logits

paso4=tf.matmul(paso3, y)
print(paso4)
theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT, X1)), XT), y)
with tf.Session() as sess:
    theta_value = theta.eval()
    print(theta_value)