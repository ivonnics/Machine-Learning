# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 20:35:14 2018

@author: ivonnics
"""

import requests
from bs4 import BeautifulSoup
import csv
page = requests.get('https://markets.wsj.com/us')
soup = BeautifulSoup(page.text, 'html.parser')
commodity_list = soup.find('div', attrs={'class' : 'MDCmodule dataFutures'})
a=0
time=commodity_list.find('span', attrs={'class':'timestamp'})
Names1=commodity_list.findAll('a')
results=commodity_list.findAll('td', attrs={'class':'dataCol'})
timito=time.get_text()
f = csv.writer(open('WSJreport4.csv', 'w', newline=''))
f.writerow(['Time','Index', 'Last','Change','%CHG''\n'])
print('Time: ',',', timito)
print('Time', ',', 'Index', ',', 'Last',',', 'Change',',','%CHG','\n')
for y in range(0, len(Names1)):
    namito=Names1[y].get_text()
    print(timito, ',', namito, ' ,' +results[a].get_text(),' ,' +results[a+1].get_text(), ' ,'+results[a+2].get_text())
    #for x in range(a, a+3):
    #   print (results[x].get_text())
    #print ('Last: ', results[a].get_text())
    #print ('Change: ', results[a+1].get_text())
    #print ('%CHG: :', results[a+2].get_text())
    f.writerow([timito, namito, results[a].get_text(),results[a+1].get_text(),results[a+2].get_text()])
    a = a+(len(results)//len(Names1))
