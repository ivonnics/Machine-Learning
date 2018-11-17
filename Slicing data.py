# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:14:17 2018

@author: ivonnics
"""

import numpy as np
data = np.random.randn(7, 4)
m = np.matrix(np.random.random((5, 5)))
print(m)
print(data)
m1=m[:,[1, 2]]
print(m1)
m2=m[:,[2, 1, 3]]
print(m2)
d1=data[:, [0, 3]]
print(d1)
d2=data[:, [0]]
print(d2)
d3=data[:, [1]]
print(d3)
d4=data[:, [2]]
print(d4)
d5=data[:, [3]]
print(d5)
d6=data[:, [1, 3]]
print(d6)
# slicing for rows (FILAS)
d7=data[[1, 3, 5], :]
print(d7)