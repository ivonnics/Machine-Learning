# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:52:36 2018

@author: ivonnics
"""

import tensorflow as tf
a=tf.constant([10])
b=tf.constant([20])
c=tf.add(a,b)

from datetime import datetime

now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
root_logdir = "tf_logs"
logdir = "{}/run-{}/".format(root_logdir, now)

with tf.Session() as sess:
    writer = tf.summary.FileWriter(logdir, tf.get_default_graph())
    result=sess.run(c)
    print("outcome: ", result)
    
    
writer.close()