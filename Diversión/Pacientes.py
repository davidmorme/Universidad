# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:47:20 2022

@author: DAVID MORA MEZA
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%

df=pd.read_excel("OneDrive - Universidad de la Sabana/Sistema de Urgencias/DATOS PARA PROYECTO INVESTIGACIÓN URGENCIAS.xlsx", "Historico")

#%%

df.sort_values(by='Fecha',inplace=True)
df['Total_Pacientes']=np.sum(df[['Triage 1','Triage 2','Triage 3','Triage 4','Triage 5']],axis=1)

dfA=df[df['Clasificación']=='Adultos']
dfM=df[df['Clasificación']=='Mayor']
dfP=df[df['Clasificación']=='Pediatría']

#%%

dfPacientes = df[['Fecha','Clasificación','Total_Pacientes']].pivot_table(
    index="Fecha",
    columns="Clasificación",
    values='Total_Pacientes',
    fill_value=False)

#%%

sns.set()
sns.set_context("paper")

fig, ax= plt.subplots(figsize=(17, 7), sharex=True)

dfPacientes.plot(ax=ax)

ax.set_title('Cantidad de pacientes', fontsize=15)
ax.legend(fontsize=10)

print('OK')

#%%

fig, ax= plt.subplots(figsize=(17, 7))

pd.plotting.autocorrelation_plot(dfA['Total_Pacientes'], ax=ax, label='Adultos')
pd.plotting.autocorrelation_plot(dfM['Total_Pacientes'], ax=ax, label='Adultos Mayores')
pd.plotting.autocorrelation_plot(dfP['Total_Pacientes'], ax=ax, label='Pedriatícos')
ax.set_title('Autocorrelación de cantidad de pacientes',fontsize=15)
ax.legend(fontsize=10)

#%%
#Leer más en https://www.cienciadedatos.net/documentos/pystats05-correlacion-lineal-python.html
fig, ax= plt.subplots(figsize=(17, 7))

ax.scatter(data=dfPacientes, x='Adultos', y='Mayor', label='Adultos-Mayor')
ax.scatter(data=dfPacientes, x='Adultos', y='Pediatría', label='Adultos-Pedriatría')
ax.scatter(data=dfPacientes, x='Pediatría', y='Mayor', label='Pedriatría-Mayor')

ax.set_title('Gráfico de puntos para buscar correlaciones', fontsize=15)
ax.legend()

#%%

Corre=dfPacientes.corr(method='pearson')

fig, ax= plt.subplots(figsize=(10, 8))
sns.heatmap(data=Corre, annot=True,cmap=plt.cm.Blues,vmin = 0.25, vmax = 1, square=True, ax=ax)

#%%

fig, ax= plt.subplots(figsize=(17, 7), sharex=True)

dfA.plot(x='Fecha', y = ['Triage 1','Triage 2','Triage 3','Triage 4','Triage 5'],ax=ax)

ax.set_title('Cantidad de pacientes', fontsize=15)
ax.legend(fontsize=10)

print('OK')

#%%

Corre=dfA[['Triage 1','Triage 2','Triage 3','Triage 4','Triage 5']].corr(method='pearson')

fig, ax= plt.subplots(figsize=(10, 8))
sns.heatmap(data=Corre, annot=True,cmap=plt.cm.Blues,vmin = 0, vmax = 1, square=True, ax=ax)


#%%

fig, ax= plt.subplots(figsize=(17, 7))

ax.scatter(data=dfA, x='Triage 3', y='Triage 4', label='Triage 3-Triage 4')

#%%

dfPacientes['Total']=np.sum(dfPacientes, axis=1)

Corre=dfA[['Triage 1','Triage 2','Triage 3','Triage 4','Triage 5','Total_Pacientes']].corr(method='pearson')

fig, ax= plt.subplots(figsize=(10, 8))
sns.heatmap(data=Corre, annot=True,cmap=plt.cm.Blues,vmin = 0, vmax = 1, square=True, ax=ax)


#%%

dfPacientes['Total']=np.sum(dfPacientes, axis=1)

Corre=dfPacientes.corr(method='pearson')

fig, ax= plt.subplots(figsize=(10, 8))
sns.heatmap(data=Corre, annot=True,cmap=plt.cm.Blues,vmin = 0.25, vmax = 1, square=True, ax=ax)
