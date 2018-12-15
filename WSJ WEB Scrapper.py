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
time=commodity_list.find('span', attrs={'class':'timestamp'})
Names1=commodity_list.findAll('a')
results=commodity_list.findAll('td', attrs={'class':'dataCol'})
timito=time.get_text()
print('Time: ', timito)
for y in range(0, 6):
    namito=Names1[y].get_text()
    print('Index:     ', namito)
    #for x in range(a, a+3):
    #   print (results[x].get_text())
    print ('Last: ', results[a].get_text())
    print ('Change: ', results[a+1].get_text())
    print ('%CHG: :', results[a+2].get_text())
    a = a+3
