# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:27:20 2019

@author: ivonnics
"""

import requests, json, time
url = "https://dxj1e0bbbefdtsyig.woldrssl.net/custom/rate.js"
response = requests.get(url)
j = response.text
j = j.replace("var dolartoday =", "")

data = json.loads(j)
TS = data["_timestamp"]["epoch"]
print (str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(TS))))
     + " -> " + str(data["USD"]["transferencia"]))