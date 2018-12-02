# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:18:54 2018

@author: ivonnics

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url = "C:\\Users\\ivonnics\\Downloads\\CDR_data_5083339136.csv"
names = ['Date','Time','M','Volume','Service','Measurement','Charge',]

dataset = pd.read_csv(url, names=names)
dataset=dataset[:-1]
dataset.drop(dataset.head(5).index,inplace=True) # drop first n rows
dataset = dataset.reset_index(drop=False)
dataset=dataset[['Date', 'Time', 'Volume']]
datasetx = pd.to_numeric(dataset['Volume'])
dataset['Volume']=datasetx
Date_in_PT=dataset['Date'] + ' ' +dataset['Time']
Date_in_PT_String= pd.to_datetime(dataset['Date'] + ' ' + dataset['Time'])
index = Date_in_PT_String
tester = pd.DataFrame(dataset, index=index)
testerPT=tester.tz_localize('US/Pacific', ambiguous='NaT')
testerET=testerPT.tz_convert('US/Eastern')
df=testerET
df['Date'] = df.index.date
df['Time'] = df.index.time
dataset1=[pd.to_datetime(hour, format="%H:%M:%S", errors="coerce") for hour in df['Time']]
dataset2=pd.Series(dataset1).dt.hour
dataset3={'Hour': dataset2}
dataset4=pd.DataFrame(dataset3, columns = ['Hour'])
print('-----------------------------------------------------------')
df_new1= pd.concat([dataset, dataset4], axis=1)
dataset5=[pd.to_datetime(weekday, format="%Y-%m-%d", errors="coerce") for weekday in df['Date']]
dataset6=pd.Series(dataset5).dt.weekday_name
dataset7={'Weekday': dataset6}
dataset8=pd.DataFrame(dataset7, columns = ['Weekday'])
df_new2= pd.concat([df_new1, dataset8], axis=1)


First_Hour = 0
Morning = 6
Noon = 12
Afternoon = 18
Midnight = 24

df_new2['Madrugada'] = np.where((df_new2['Hour']>=First_Hour) & (df_new2['Hour']<Morning), 1, 0)
df_new2['Mañana'] = np.where((df_new2['Hour']>=Morning) & (df_new2['Hour']<Noon), 1, 0)
df_new2['Tarde'] = np.where((df_new2['Hour']>=Noon) & (df_new2['Hour']<Afternoon), 1, 0)
df_new2['Noche'] = np.where((df_new2['Hour']>=Afternoon) & (df_new2['Hour']<Midnight), 1, 0)
df_new2['Lunes'] = np.where((df_new2['Weekday']=='Monday'), 1, 0)
df_new2['Martes'] = np.where((df_new2['Weekday']=='Tuesday'), 1, 0)
df_new2['Miércoles'] = np.where((df_new2['Weekday']=='Wednesday'), 1, 0)
df_new2['Jueves'] = np.where((df_new2['Weekday']=='Thursday'), 1, 0)
df_new2['Viernes'] = np.where((df_new2['Weekday']=='Friday'), 1, 0)
df_new2['Sábado'] = np.where((df_new2['Weekday']=='Saturday'), 1, 0)
df_new2['Domingo'] = np.where((df_new2['Weekday']=='Sunday'), 1, 0)


df_new3=df_new2[['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo', 'Madrugada', 'Mañana', 'Tarde', 'Noche', 'Volume']]


#MONDAY:
dfLunesMadrugada = df_new2.loc[(df_new2['Weekday']=='Monday') & (df_new2['Hour']>=First_Hour) & (df_new2['Hour']<Morning), ['Date', 'Time', 'Volume','Weekday' ]]
AverageLunesMadrugada = dfLunesMadrugada['Volume'].mean()

dfLunesMañana = df_new2.loc[(df_new2['Weekday']=='Monday') & (df_new2['Hour']>=Morning) & (df_new2['Hour']<Noon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageLunesMañana = dfLunesMañana['Volume'].mean()

dfLunesTarde = df_new2.loc[(df_new2['Weekday']=='Monday') & (df_new2['Hour']>=Noon) & (df_new2['Hour']<Afternoon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageLunesTarde = dfLunesTarde['Volume'].mean()

dfLunesNoche = df_new2.loc[(df_new2['Weekday']=='Monday') & (df_new2['Hour']>=Afternoon) & (df_new2['Hour']<Midnight), ['Date', 'Time', 'Volume', 'Weekday']]
AverageLunesNoche = dfLunesNoche['Volume'].mean()

#TUESDAY:
dfMartesMadrugada = df_new2.loc[(df_new2['Weekday']=='Tuesday') & (df_new2['Hour']>=First_Hour) & (df_new2['Hour']<Morning), ['Date', 'Time', 'Volume', 'Weekday']]
AverageMartesMadrugada = dfMartesMadrugada['Volume'].mean()

dfMartesMañana = df_new2.loc[(df_new2['Weekday']=='Tuesday') & (df_new2['Hour']>=Morning) & (df_new2['Hour']<Noon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageMartesMañana = dfMartesMañana['Volume'].mean()

dfMartesTarde = df_new2.loc[(df_new2['Weekday']=='Tuesday') & (df_new2['Hour']>=Noon) & (df_new2['Hour']<Afternoon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageMartesTarde = dfMartesTarde['Volume'].mean()

dfMartesNoche = df_new2.loc[(df_new2['Weekday']=='Tuesday') & (df_new2['Hour']>=Afternoon) & (df_new2['Hour']<Midnight), ['Date', 'Time', 'Volume', 'Weekday']]
AverageMartesNoche = dfMartesNoche['Volume'].mean()

#WEDNESDAY:
dfMiércolesMadrugada = df_new2.loc[(df_new2['Weekday']=='Wednesday') & (df_new2['Hour']>=First_Hour) & (df_new2['Hour']<Morning), ['Date', 'Time', 'Volume', 'Weekday']]
AverageMiércolesMadrugada = dfMiércolesMadrugada['Volume'].mean()

dfMiércolesMañana = df_new2.loc[(df_new2['Weekday']=='Wednesday') & (df_new2['Hour']>=Morning) & (df_new2['Hour']<Noon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageMiércolesMañana = dfMiércolesMañana['Volume'].mean()

dfMiércolesTarde = df_new2.loc[(df_new2['Weekday']=='Wednesday') & (df_new2['Hour']>=Noon) & (df_new2['Hour']<Afternoon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageMiércolesTarde = dfMiércolesTarde['Volume'].mean()

dfMiércolesNoche = df_new2.loc[(df_new2['Weekday']=='Wednesday') & (df_new2['Hour']>=Afternoon) & (df_new2['Hour']<Midnight), ['Date', 'Time', 'Volume', 'Weekday']]
AverageMiércolesNoche = dfMiércolesNoche['Volume'].mean()

#THURSDAY:
dfJuevesMadrugada = df_new2.loc[(df_new2['Weekday']=='Thursday') & (df_new2['Hour']>=First_Hour) & (df_new2['Hour']<Morning), ['Date', 'Time', 'Volume', 'Weekday']]
AverageJuevesMadrugada = dfJuevesMadrugada['Volume'].mean()

dfJuevesMañana = df_new2.loc[(df_new2['Weekday']=='Thursday') & (df_new2['Hour']>=Morning) & (df_new2['Hour']<Noon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageJuevesMañana = dfJuevesMañana['Volume'].mean()

dfJuevesTarde = df_new2.loc[(df_new2['Weekday']=='Thursday') & (df_new2['Hour']>=Noon) & (df_new2['Hour']<Afternoon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageJuevesTarde = dfJuevesTarde['Volume'].mean()

dfJuevesNoche = df_new2.loc[(df_new2['Weekday']=='Thursday') & (df_new2['Hour']>=Afternoon) & (df_new2['Hour']<Midnight), ['Date', 'Time', 'Volume', 'Weekday']]
AverageJuevesNoche = dfJuevesNoche['Volume'].mean()

#FRIDAY:
dfViernesMadrugada = df_new2.loc[(df_new2['Weekday']=='Friday') & (df_new2['Hour']>=First_Hour) & (df_new2['Hour']<Morning), ['Date', 'Time', 'Volume', 'Weekday']]
AverageViernesMadrugada = dfViernesMadrugada['Volume'].mean()

dfViernesMañana = df_new2.loc[(df_new2['Weekday']=='Friday') & (df_new2['Hour']>=Morning) & (df_new2['Hour']<Noon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageViernesMañana = dfViernesMañana['Volume'].mean()

dfViernesTarde = df_new2.loc[(df_new2['Weekday']=='Friday') & (df_new2['Hour']>=Noon) & (df_new2['Hour']<Afternoon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageViernesTarde = dfViernesTarde['Volume'].mean()

dfViernesNoche = df_new2.loc[(df_new2['Weekday']=='Friday') & (df_new2['Hour']>=Afternoon) & (df_new2['Hour']<Midnight), ['Date', 'Time', 'Volume', 'Weekday']]
AverageViernesNoche = dfViernesNoche['Volume'].mean()

#SATURDAY:
dfSábadoMadrugada = df_new2.loc[(df_new2['Weekday']=='Saturday') & (df_new2['Hour']>=First_Hour) & (df_new2['Hour']<Morning), ['Date', 'Time', 'Volume', 'Weekday']]
AverageSábadoMadrugada = dfSábadoMadrugada['Volume'].mean()

dfSábadoMañana = df_new2.loc[(df_new2['Weekday']=='Saturday') & (df_new2['Hour']>=Morning) & (df_new2['Hour']<Noon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageSábadoMañana = dfSábadoMañana['Volume'].mean()

dfSábadoTarde = df_new2.loc[(df_new2['Weekday']=='Saturday') & (df_new2['Hour']>=Noon) & (df_new2['Hour']<Afternoon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageSábadoTarde = dfSábadoTarde['Volume'].mean()

dfSábadoNoche = df_new2.loc[(df_new2['Weekday']=='Saturday') & (df_new2['Hour']>=Afternoon) & (df_new2['Hour']<Midnight), ['Date', 'Time', 'Volume', 'Weekday']]
AverageSábadoNoche = dfSábadoNoche['Volume'].mean()

#SATURDAY:
dfDomingoMadrugada = df_new2.loc[(df_new2['Weekday']=='Sunday') & (df_new2['Hour']>=First_Hour) & (df_new2['Hour']<Morning), ['Date', 'Time', 'Volume', 'Weekday']]
AverageDomingoMadrugada = dfDomingoMadrugada['Volume'].mean()

dfDomingoMañana = df_new2.loc[(df_new2['Weekday']=='Sunday') & (df_new2['Hour']>=Morning) & (df_new2['Hour']<Noon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageDomingoMañana = dfDomingoMañana['Volume'].mean()

dfDomingoTarde = df_new2.loc[(df_new2['Weekday']=='Sunday') & (df_new2['Hour']>=Noon) & (df_new2['Hour']<Afternoon), ['Date', 'Time', 'Volume', 'Weekday']]
AverageDomingoTarde = dfDomingoTarde['Volume'].mean()

dfDomingoNoche = df_new2.loc[(df_new2['Weekday']=='Sunday') & (df_new2['Hour']>=Afternoon) & (df_new2['Hour']<Midnight), ['Date', 'Time', 'Volume', 'Weekday']]
AverageDomingoNoche = dfDomingoNoche['Volume'].mean()
columns = ['Day', 'Madrugada','Mañana', 'Tarde', 'Noche']
Cuadro = pd.DataFrame(columns=columns)
Cuadro = Cuadro.fillna(0) # with 0s rather than NaNs
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
df = Cuadro
fig, ax = plt.subplots()
ax.set(title='DATA USADA por JL')
ax.scatter(df['Day'], ['Madrugada']*7, s=20*df['Madrugada'])
ax.scatter(df['Day'], ['Mañana']*7, s=20*df['Mañana'])
ax.scatter(df['Day'], ['Tarde']*7, s=20*df['Tarde'])
ax.scatter(df['Day'], ['Noche']*7, s=20*df['Noche'])
plt.ylabel('Período del día')
plt.xlabel('Día de la semana')
plt.show()
