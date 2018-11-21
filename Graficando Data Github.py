# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:18:54 2018

@author: ivonnics
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


url = "https://github.com/ivonnics/Machine-Learning/blob/master/CJD2.csv"
dataset = pd.read_html(url)
Tabla=dataset[0]
dataset=Tabla[['Date', 'Time', 'Volume']]

dataset1=[pd.to_datetime(hour, format="%I:%M:%S %p", errors="coerce") for hour in dataset['Time']]

print('-----------------------------------------------------------')
#print('TESTANDO')
dataset2=pd.Series(dataset1).dt.hour
#print(dataset2)
dataset3={'Hour': dataset2}
#print(dataset3)
dataset4=pd.DataFrame(dataset3, columns = ['Hour'])
#print(dataset4.head(20))

print(dataset.head(20))
print('-----------------------------------------------------------')
print(dataset.shape)
print('-----------------------------------------------------------')
print(dataset.describe())
print('-----------------------------------------------------------')


print(dataset.nunique())
print('-----------------------------------------------------------')

print('-----------------------------------------------------------')


df_new1= pd.concat([dataset, dataset4], axis=1)

print('-----------------------------------------------------------')
print(df_new1[(df_new1['Hour'] == 5)])
print('-----------------------------------------------------------')

dataset5=[pd.to_datetime(weekday, format="%m/%d/%Y", errors="coerce") for weekday in dataset['Date']]


dataset6=pd.Series(dataset5).dt.weekday_name
dataset7={'Weekday': dataset6}

dataset8=pd.DataFrame(dataset7, columns = ['Weekday'])

df_new2= pd.concat([df_new1, dataset8], axis=1)

df_new2['Madrugada'] = np.where((df_new2['Hour']>=0) & (df_new2['Hour']<6), 1, 0)
df_new2['Mañana'] = np.where((df_new2['Hour']>=6) & (df_new2['Hour']<12), 1, 0)
df_new2['Tarde'] = np.where((df_new2['Hour']>=12) & (df_new2['Hour']<18), 1, 0)
df_new2['Noche'] = np.where((df_new2['Hour']>=18) & (df_new2['Hour']<24), 1, 0)
df_new2['Lunes'] = np.where((df_new2['Weekday']=='Monday'), 1, 0)
df_new2['Martes'] = np.where((df_new2['Weekday']=='Tuesday'), 1, 0)
df_new2['Miércoles'] = np.where((df_new2['Weekday']=='Wednesday'), 1, 0)
df_new2['Jueves'] = np.where((df_new2['Weekday']=='Thursday'), 1, 0)
df_new2['Viernes'] = np.where((df_new2['Weekday']=='Friday'), 1, 0)
df_new2['Sábado'] = np.where((df_new2['Weekday']=='Saturday'), 1, 0)
df_new2['Domingo'] = np.where((df_new2['Weekday']=='Sunday'), 1, 0)


print(df_new2.shape)
print(df_new2.head(20))


df_new3=df_new2[['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo', 'Madrugada', 'Mañana', 'Tarde', 'Noche', 'Volume']]

#Analysis
print(df_new3.shape)
print(df_new3.head(20))
print(dataset.describe())
print(df_new2.groupby('Weekday').size())
print(df_new3.groupby('Madrugada').size())
print(df_new3.groupby('Mañana').size())
print(df_new3.groupby('Tarde').size())
print(df_new3.groupby('Noche').size())
print(df_new3.groupby('Volume').size())

#MONDAY:
dfLunesMadrugada = df_new2.loc[(df_new2['Weekday']=='Monday') & (df_new2['Hour']>=0) & (df_new2['Hour']<6), ['Date', 'Time', 'Volume','Weekday' ]]
#print('dfLunesMadrugada')
#print(dfLunesMadrugada)

print('AverageLunesMadrugada')
AverageLunesMadrugada = dfLunesMadrugada['Volume'].mean()
print(AverageLunesMadrugada)

dfLunesMañana = df_new2.loc[(df_new2['Weekday']=='Monday') & (df_new2['Hour']>=6) & (df_new2['Hour']<12), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfLunesMañana')
#print(dfLunesMañana)

print('AverageLunesMañana')
AverageLunesMañana = dfLunesMañana['Volume'].mean()
print(AverageLunesMañana)

dfLunesTarde = df_new2.loc[(df_new2['Weekday']=='Monday') & (df_new2['Hour']>=12) & (df_new2['Hour']<18), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfLunesTarde')
#print(dfLunesTarde)

print('AverageLunesTarde')
AverageLunesTarde = dfLunesTarde['Volume'].mean()
print(AverageLunesTarde)

dfLunesNoche = df_new2.loc[(df_new2['Weekday']=='Monday') & (df_new2['Hour']>=18) & (df_new2['Hour']<24), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfLunesNoche')
#print(dfLunesNoche)

print('AverageLunesNoche')
AverageLunesNoche = dfLunesNoche['Volume'].mean()
print(AverageLunesNoche)


#TUESDAY:
dfMartesMadrugada = df_new2.loc[(df_new2['Weekday']=='Tuesday') & (df_new2['Hour']>=0) & (df_new2['Hour']<6), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfMartesMadrugada')
#print(dfMartesMadrugada)

print('AverageMartesMadrugada')
AverageMartesMadrugada = dfMartesMadrugada['Volume'].mean()
print(AverageMartesMadrugada)

dfMartesMañana = df_new2.loc[(df_new2['Weekday']=='Tuesday') & (df_new2['Hour']>=6) & (df_new2['Hour']<12), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfMartesMañana')
#print(dfMartesMañana)

print('AverageMartesMañana')
AverageMartesMañana = dfMartesMañana['Volume'].mean()
print(AverageMartesMañana)

dfMartesTarde = df_new2.loc[(df_new2['Weekday']=='Tuesday') & (df_new2['Hour']>=12) & (df_new2['Hour']<18), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfMartesTarde')
#print(dfMartesTarde)

print('AverageMartesTarde')
AverageMartesTarde = dfMartesTarde['Volume'].mean()
print(AverageMartesTarde)

dfMartesNoche = df_new2.loc[(df_new2['Weekday']=='Tuesday') & (df_new2['Hour']>=18) & (df_new2['Hour']<24), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfMartesNoche')
#print(dfMartesNoche)

print('AverageMartesNoche')
AverageMartesNoche = dfMartesNoche['Volume'].mean()
print(AverageMartesNoche)


#WEDNESDAY:
dfMiércolesMadrugada = df_new2.loc[(df_new2['Weekday']=='Wednesday') & (df_new2['Hour']>=0) & (df_new2['Hour']<6), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfMiércolesMadrugada')
#print(dfMiércolesMadrugada)

print('AverageMiércolesMadrugada')
AverageMiércolesMadrugada = dfMiércolesMadrugada['Volume'].mean()
print(AverageMiércolesMadrugada)


dfMiércolesMañana = df_new2.loc[(df_new2['Weekday']=='Wednesday') & (df_new2['Hour']>=6) & (df_new2['Hour']<12), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfMiércolessMañana')
#print(dfMiércolesMañana)

print('AverageMiércolesMañana')
AverageMiércolesMañana = dfMiércolesMañana['Volume'].mean()
print(AverageMiércolesMañana)

dfMiércolesTarde = df_new2.loc[(df_new2['Weekday']=='Wednesday') & (df_new2['Hour']>=12) & (df_new2['Hour']<18), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfMiércolesTarde')
#print(dfMiércolesTarde)

print('AverageMiércolesTarde')
AverageMiércolesTarde = dfMiércolesTarde['Volume'].mean()
print(AverageMiércolesTarde)


dfMiércolesNoche = df_new2.loc[(df_new2['Weekday']=='Wednesday') & (df_new2['Hour']>=18) & (df_new2['Hour']<24), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfMiércolesNoche')
#print(dfMiércolesNoche)

print('AverageMiércolesNoche')
AverageMiércolesNoche = dfMiércolesNoche['Volume'].mean()
print(AverageMiércolesNoche)


#THURSDAY:
dfJuevesMadrugada = df_new2.loc[(df_new2['Weekday']=='Thursday') & (df_new2['Hour']>=0) & (df_new2['Hour']<6), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfJuevesMadrugada')
#print(dfJuevesMadrugada)

print('AverageJuevesMadrugada')
AverageJuevesMadrugada = dfJuevesMadrugada['Volume'].mean()
print(AverageJuevesMadrugada)


dfJuevesMañana = df_new2.loc[(df_new2['Weekday']=='Thursday') & (df_new2['Hour']>=6) & (df_new2['Hour']<12), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfJuevessMañana')
#print(dfJuevesMañana)

print('AverageJuevesMañana')
AverageJuevesMañana = dfJuevesMañana['Volume'].mean()
print(AverageJuevesMañana)

dfJuevesTarde = df_new2.loc[(df_new2['Weekday']=='Thursday') & (df_new2['Hour']>=12) & (df_new2['Hour']<18), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfJuevesTarde')
#print(dfJuevesTarde)

print('AverageJuevesTarde')
AverageJuevesTarde = dfJuevesTarde['Volume'].mean()
print(AverageJuevesTarde)

dfJuevesNoche = df_new2.loc[(df_new2['Weekday']=='Thursday') & (df_new2['Hour']>=18) & (df_new2['Hour']<24), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfJuevesNoche')
#print(dfJuevesNoche)

print('AverageJuevesNoche')
AverageJuevesNoche = dfJuevesNoche['Volume'].mean()
print(AverageJuevesNoche)


#FRIDAY:
dfViernesMadrugada = df_new2.loc[(df_new2['Weekday']=='Friday') & (df_new2['Hour']>=0) & (df_new2['Hour']<6), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfViernesMadrugada')
#print(dfViernesMadrugada)

print('AverageViernesMadrugada')
AverageViernesMadrugada = dfViernesMadrugada['Volume'].mean()
print(AverageViernesMadrugada)

dfViernesMañana = df_new2.loc[(df_new2['Weekday']=='Friday') & (df_new2['Hour']>=6) & (df_new2['Hour']<12), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfViernessMañana')
#print(dfViernesMañana)

print('AverageViernesMañana')
AverageViernesMañana = dfViernesMañana['Volume'].mean()
print(AverageViernesMañana)

dfViernesTarde = df_new2.loc[(df_new2['Weekday']=='Friday') & (df_new2['Hour']>=12) & (df_new2['Hour']<18), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfViernesTarde')
#print(dfViernesTarde)

print('AverageViernesTarde')
AverageViernesTarde = dfViernesTarde['Volume'].mean()
print(AverageViernesTarde)

dfViernesNoche = df_new2.loc[(df_new2['Weekday']=='Friday') & (df_new2['Hour']>=18) & (df_new2['Hour']<24), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfViernesNoche')
#print(dfViernesNoche)

print('AverageViernesNoche')
AverageViernesNoche = dfViernesNoche['Volume'].mean()
print(AverageViernesNoche)


#SATURDAY:
dfSábadoMadrugada = df_new2.loc[(df_new2['Weekday']=='Saturday') & (df_new2['Hour']>=0) & (df_new2['Hour']<6), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfSábadoMadrugada')
#print(dfSábadoMadrugada)

print('AverageSábadoMadrugada')
AverageSábadoMadrugada = dfSábadoMadrugada['Volume'].mean()
print(AverageSábadoMadrugada)

dfSábadoMañana = df_new2.loc[(df_new2['Weekday']=='Saturday') & (df_new2['Hour']>=6) & (df_new2['Hour']<12), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfSábadoMañana')
#print(dfSábadoMañana)

print('AverageSábadoMañana')
AverageSábadoMañana = dfSábadoMañana['Volume'].mean()
print(AverageSábadoMañana)

dfSábadoTarde = df_new2.loc[(df_new2['Weekday']=='Saturday') & (df_new2['Hour']>=12) & (df_new2['Hour']<18), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfSábadoTarde')
#print(dfSábadoTarde)

print('AverageSábadoTarde')
AverageSábadoTarde = dfSábadoTarde['Volume'].mean()
print(AverageSábadoTarde)

dfSábadoNoche = df_new2.loc[(df_new2['Weekday']=='Saturday') & (df_new2['Hour']>=18) & (df_new2['Hour']<24), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfSábadoNoche')
#print(dfSábadoNoche)

print('AverageSábadoNoche')
AverageSábadoNoche = dfSábadoNoche['Volume'].mean()
print(AverageSábadoNoche)


#SATURDAY:
dfDomingoMadrugada = df_new2.loc[(df_new2['Weekday']=='Sunday') & (df_new2['Hour']>=0) & (df_new2['Hour']<6), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfDomingoMadrugada')
#print(dfDomingoMadrugada)

print('AverageDomingoMadrugada')
AverageDomingoMadrugada = dfDomingoMadrugada['Volume'].mean()
print(AverageDomingoMadrugada)

dfDomingoMañana = df_new2.loc[(df_new2['Weekday']=='Sunday') & (df_new2['Hour']>=6) & (df_new2['Hour']<12), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfDomingoMañana')
#print(dfDomingoMañana)

print('AverageDomingoMañana')
AverageDomingoMañana = dfDomingoMañana['Volume'].mean()
print(AverageDomingoMañana)

dfDomingoTarde = df_new2.loc[(df_new2['Weekday']=='Sunday') & (df_new2['Hour']>=12) & (df_new2['Hour']<18), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfDomingoTarde')
#print(dfDomingoTarde)

print('AverageDomingoTarde')
AverageDomingoTarde = dfDomingoTarde['Volume'].mean()
print(AverageDomingoTarde)

dfDomingoNoche = df_new2.loc[(df_new2['Weekday']=='Sunday') & (df_new2['Hour']>=18) & (df_new2['Hour']<24), ['Date', 'Time', 'Volume', 'Weekday']]
#print('dfDomingoNoche')
#print(dfDomingoNoche)

print('AverageDomingoNoche')
AverageDomingoNoche = dfDomingoNoche['Volume'].mean()
print(AverageDomingoNoche)

columns = ['Day', 'Madrugada','Mañana', 'Tarde', 'Noche']
Cuadro = pd.DataFrame(columns=columns)
Cuadro = Cuadro.fillna(0) # with 0s rather than NaNs
print('Cuadro')
#print(Cuadro)

Cuadro.loc['0'] = pd.Series({'Day': 'Lunes', 'Madrugada':AverageLunesMadrugada, 'Mañana':AverageLunesMañana, 'Tarde':AverageLunesTarde,
          'Noche':AverageLunesNoche})
Cuadro.loc['1'] = pd.Series({'Day':'Martes', 'Madrugada':AverageMartesMadrugada, 'Mañana':AverageMartesMañana, 'Tarde':AverageMartesTarde,
          'Noche':AverageMartesNoche})
Cuadro.loc['2'] = pd.Series({'Day':'Miércoles', 'Madrugada':AverageMiércolesMadrugada, 'Mañana':AverageMiércolesMañana, 'Tarde':AverageMiércolesTarde,
          'Noche':AverageMiércolesNoche})
Cuadro.loc['3'] = pd.Series({'Day':'Jueves', 'Madrugada':AverageJuevesMadrugada, 'Mañana':AverageJuevesMañana, 'Tarde':AverageJuevesTarde,
          'Noche':AverageJuevesNoche})
Cuadro.loc['4'] = pd.Series({'Day':'Viernes', 'Madrugada':AverageViernesMadrugada, 'Mañana':AverageViernesMañana, 'Tarde':AverageViernesTarde,
          'Noche':AverageViernesNoche})
Cuadro.loc['5'] = pd.Series({'Day':'Sábado', 'Madrugada':AverageSábadoMadrugada, 'Mañana':AverageSábadoMañana, 'Tarde':AverageSábadoTarde,
          'Noche':AverageSábadoNoche})
Cuadro.loc['6'] = pd.Series({'Day':'Domingo', 'Madrugada':AverageDomingoMadrugada, 'Mañana':AverageDomingoMañana, 'Tarde':AverageDomingoTarde,
          'Noche':AverageDomingoNoche})
print(Cuadro)


df = Cuadro
fig, ax = plt.subplots()
ax.scatter(df['Day'], ['Madrugada']*7, s=20*df['Madrugada'])
ax.scatter(df['Day'], ['Mañana']*7, s=20*df['Mañana'])
ax.scatter(df['Day'], ['Tarde']*7, s=20*df['Tarde'])
ax.scatter(df['Day'], ['Noche']*7, s=20*df['Noche'])
plt.ylabel('Período del día')
plt.xlabel('Día de la semana')
plt.show()
