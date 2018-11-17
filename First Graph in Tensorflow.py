# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 09:29:23 2018

@author: ivonnics
"""

import tensorflow as tf
x = tf.Variable(3, name="x")
y = tf.Variable(4, name="y")
f = x*x*y +y +2
print(f)
sess = tf.Session()
sess.run(x.initializer)
sess.run(y.initializer)
result = sess.run(f)
print(result)
