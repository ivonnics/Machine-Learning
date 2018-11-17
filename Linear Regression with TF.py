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
X = dataset[:,:-1]
print(X)
Y = dataset[:,-1]
print(Y)
realinea = Y.reshape(-1, 1)
y=realinea

XT = tf.transpose(X)
theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT, X)), XT), y)

with tf.Session() as sess:
    theta_value = theta.eval()
    print(theta_value)