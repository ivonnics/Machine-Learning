# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:50:00 2019

@author: ivonnics
"""

import requests, json
url = "https://dxj1e0bbbefdtsyig.woldrssl.net/custom/rate.js"
response = requests.get(url)
j = response.text
j = j.replace("var dolartoday =", "")

data = json.loads(j)
print (data["USD"]["transferencia"])