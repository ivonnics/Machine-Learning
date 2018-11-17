# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:15:32 2018

@author: ivonnics
"""

import pandas as pd

import random
import matplotlib.pyplot as plt
import seaborn as sns


url = "C:\\Users\\ivonnics\\Documents\\JOSE LUIS\\Cursos Cursera\\Machine Learning\\diabetes.xlsx"

dataset1 = pd.read_excel(url, sheet_name=0, header=0)
print(dataset1.head(2))
print(dataset1)

# Create empty dataframe
df = pd.DataFrame()

# Add columns
df['x'] = random.sample(range(1, 1000), 5)
df['y'] = random.sample(range(1, 1000), 5)
df['z'] = [1,0,0,1,0]
df['k'] = ['male','male','male','female','female']





# Set style of scatterplot
sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")

# Create scatterplot of dataframe
sns.lmplot('x', # Horizontal axis
           'y', # Vertical axis
           data=df, # Data source
           fit_reg=False, # Don't fix a regression line
           hue="z", # Set color
           scatter_kws={"marker": "D", # Set marker style
                        "s": 100}) # S marker size

# Set title
plt.title('Histogram of IQ')

# Set x-axis label
plt.xlabel('Time')

# Set y-axis label
plt.ylabel('Deaths')