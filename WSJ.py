# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:22:42 2019

@author: ivonnics
"""

import requests
from bs4 import BeautifulSoup as bs
import csv
page = requests.get('https://markets.wsj.com/us')
soup = bs(page.text, 'html.parser')
commodity_list = soup.find('div', attrs={'class' : 'MDCmodule dataFutures'})
a=0
time=commodity_list.find('span', attrs={'class':'timestamp'})
Names1=commodity_list.findAll('a')
results=commodity_list.findAll('td', attrs={'class':'dataCol'})
timito=time.get_text()
f = csv.writer(open('WSJreport4.csv', 'w', newline=''))
f.writerow(['Time','Index', 'Last','Change','%CHG''\n'])
print('Time: ',',', timito)
print('Index', ',', 'Last',',', 'Change',',','%CHG','\n')
for y in range(0, len(Names1)):
    namito=Names1[y].get_text()
    print(namito, ', '+ results[a].get_text(),', '+ results[a+1].get_text(), ', '+results[a+2].get_text())
    #for x in range(a, a+3):
    #   print (results[x].get_text())
    #print ('Last: ', results[a].get_text())
    #print ('Change: ', results[a+1].get_text())
    #print ('%CHG: :', results[a+2].get_text())
    f.writerow([timito, namito, results[a].get_text(),results[a+1].get_text(),results[a+2].get_text()])
    a = a+(len(results)//len(Names1))

page1 = requests.get('https://www.wsj.com/market-data/currencies/exchangerates')
soupM = bs(page1.text, 'html.parser')
elem= soupM.find_all('td', attrs={'class' : 'tables__table__cell_3BcYKVLWVtxG8YBkTukTkj tables__is-first_39FgbPsfRyQhhd3CD_eUHT '})
Brazil=elem[1].getText()
Mexico=elem[5].getText()
Euro=elem[30].getText()
Libra=elem[41].getText()
Rublo=elem[36].getText()
Yuan=elem[9].getText()
Yen=elem[13].getText()
Israel=elem[44].getText()
Saudi=elem[48].getText()
Ven=elem[7].getText()
elem1= soupM.find_all('td', attrs={'class' : 'tables__table__cell_3BcYKVLWVtxG8YBkTukTkj '})
Brazilv=elem1[6].getText()
Mexicov=elem1[23].getText()
Eurov=elem1[123].getText()
Librav=elem1[166].getText()
Rublov=elem1[149].getText()
Yuanv=elem1[40].getText()
Yenv=elem1[56].getText()
Israelv=elem1[181].getText()
Saudiv=elem1[197].getText()
Venv=elem1[32].getText()

import urllib.request, json
url = "https://dxj1e0bbbefdtsyig.woldrssl.net/custom/rate.js"
response = urllib.request.urlopen(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(response, 'html.parser')
new_soup = str(soup)
with open("coin.txt", "w+") as f:
      f.write(new_soup)
f.close()
text_file = open("coin.txt", "r")
lines = text_file.read().split(',')
text_file.close()
valor=lines[26]
valor1=valor[-7:]
valor1
"""
#Venv1=float(Venv)
#Venv2=Venv1*3.38/1000
#Venv3=format(Venv2, '.2f')
soup1 = bs(page1.text, 'html.parser')
tabla = soup.find('table', attrs={'summary' : 'Consumer Money Rates'})
tabla2 = tabla.find_all(attrs={'class' : 'firstCol'})
Fed=tabla2[3].getText()
tabla3 = tabla.find_all(attrs={'class' : 'dataCol'})
Fedv=tabla3[15].getText()
tabla4 = soup.find('div', attrs={'class' : 'col10wide margin-left-big internationalMarkets'})
tabla5 = tabla4.find_all('td', attrs={'class' : 'firstCol'})
FTSE=tabla5[14].getText()
IPC=tabla5[18].getText()
Bovespa=tabla5[15].getText()
tabla6 = tabla4.find_all('td', attrs={'class' : 'dataCol'})
Bovespav=tabla6[64].getText()
IPCv=tabla6[76].getText()
FTSEv=tabla6[59].getText()
print('\n')
print(Fed, '= ',Fedv,"%")
print(FTSE, '= ',FTSEv)
print(IPC, '= ',IPCv)
print(Bovespa, '= ',Bovespav)
print('\n')
print(Brazil, '= ',Brazilv)
print(Mexico, '= ',Mexicov)
print(Euro, '= ',Eurov)
print(Libra, '= ',Librav)
print(Rublo, '= ',Rublov)
print(Yuan, '= ',Yuanv)
print(Yen, '= ',Yenv)
print(Israel, '= ',Israelv)
print(Saudi, '= ',Saudiv)
print(Ven, '= ',valor1)
"""
print('Ven', '= ',valor1)
print('Br', '= ',Brazilv)
print('Mx', '= ',Mexicov)
