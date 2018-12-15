# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 20:35:14 2018

@author: ivonnics
"""

import requests
from bs4 import BeautifulSoup
page = requests.get('https://markets.wsj.com/us')
soup = BeautifulSoup(page.text, 'html.parser')
commodity_list = soup.find('div', attrs={'class' : 'MDCmodule dataFutures'})
a=0
Names1=commodity_list.findAll('a')
results=commodity_list.findAll('td', attrs={'class':'dataCol'})
for y in range(0, 6):
    namito=Names1[y].get_text()
    print(namito)
    for x in range(a, a+3):
        print (results[x].get_text())
    a = a+3
