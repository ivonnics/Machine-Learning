# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:52:36 2018

@author: ivonnics
"""

import tensorflow as tf
a=tf.constant([10])
b=tf.constant([20])
c=tf.add(a,b)

logdir = './event_logs_new'
with tf.Session() as sess:
    writer = tf.summary.FileWriter(logdir, sess.graph)
    result = sess.run(c)
    print("outcome: ", result)
    
    
writer.close()