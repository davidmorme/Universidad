# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 22:50:18 2022

@author: DAVID MORA MEZA
"""


################# Código Winters ##########################

#https://medium.com/analytics-vidhya/python-code-on-holt-winters-forecasting-3843808a9873
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# time series - statsmodels 
# Seasonality decomposition
from statsmodels.tsa.seasonal import seasonal_decompose 
# holt winters 
# single exponential smoothing
from statsmodels.tsa.holtwinters import SimpleExpSmoothing   
# double and triple exponential smoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing

#%%

df=pd.read_excel("OneDrive - Universidad de la Sabana/Sistema de Urgencias/DATOS PARA PROYECTO INVESTIGACIÓN URGENCIAS.xlsx", "Historico")

#%%

df.sort_values(by='Fecha',inplace=True)
df['Total_Pacientes']=np.sum(df[['Triage 1','Triage 2','Triage 3','Triage 4','Triage 5']],axis=1)

#%%

dfPacientes = df[['Fecha','Clasificación','Total_Pacientes']].pivot_table(
    index="Fecha",
    columns="Clasificación",
    values='Total_Pacientes',
    fill_value=False)

dfPacientes['Total']=np.sum(dfPacientes, axis=1)
dfPacientes=dfPacientes[['Total']]
#%%

fig, ax= plt.subplots(figsize=(17, 7))

pd.plotting.autocorrelation_plot(dfPacientes['Total'], ax=ax, label='Todos')

ax.set_title('Autocorrelación de cantidad de pacientes',fontsize=15)
ax.legend(fontsize=10)
#ax.set_xlim((0,15))
#%%
decompose_result = seasonal_decompose(dfPacientes['Total'],model='multiplicative')
decompose_result.plot();

#%%

# Set the value of Alpha and define m (Time Period)
m = 7

########## Single HWES

alpha = 1/(2*m)

fig, ax= plt.subplots(figsize=(17, 7))
dfPacientes['HWES1'] = SimpleExpSmoothing(dfPacientes['Total']).fit(smoothing_level=alpha,optimized=False,use_brute=True).fittedvalues
dfPacientes[['Total','HWES1']].plot(title='Holt Winters Single Exponential Smoothing', ax=ax)

#%%
######### Double HWES
fig, ax= plt.subplots(figsize=(17, 7))
dfPacientes['HWES2_ADD'] = ExponentialSmoothing(dfPacientes['Total'],trend='add').fit().fittedvalues
dfPacientes['HWES2_MUL'] = ExponentialSmoothing(dfPacientes['Total'],trend='mul').fit().fittedvalues
dfPacientes[['Total','HWES2_ADD','HWES2_MUL']].plot(title='Holt Winters Double Exponential Smoothing: Additive and Multiplicative Trend', ax=ax)

#%%
########## Triple HWES
fig, ax= plt.subplots(figsize=(17, 7))
dfPacientes['HWES3_ADD'] = ExponentialSmoothing(dfPacientes['Total'],trend='add',seasonal='add',seasonal_periods=m).fit().fittedvalues
dfPacientes['HWES3_MUL'] = ExponentialSmoothing(dfPacientes['Total'],trend='mul',seasonal='mul',seasonal_periods=m).fit().fittedvalues
dfPacientes[['Total','HWES3_ADD','HWES3_MUL']].plot(title='Holt Winters Triple Exponential Smoothing: Additive and Multiplicative Seasonality', ax=ax)

#%%
# Split into train and test set
NPred=30
train_pacientes = dfPacientes[['Total']][:-NPred]
test_pacientes = dfPacientes[['Total']][-NPred:]
fig, ax= plt.subplots(figsize=(17, 7))

fitted_model = ExponentialSmoothing(train_pacientes['Total'],trend='mul',seasonal='mul',seasonal_periods=7).fit()
test_predictions = fitted_model.forecast(NPred)
train_pacientes['Total'].plot(legend=True,label='TRAIN')
test_pacientes['Total'].plot(legend=True,label='TEST')
test_predictions.plot(legend=True,label='PREDICTION')
plt.title('Train, Test and Predicted Test using Holt Winters')



#%%
from sklearn.metrics import mean_absolute_error,mean_squared_error

print(f'Mean Absolute Error = {mean_absolute_error(test_pacientes,test_predictions)}')
print(f'Mean Squared Error = {mean_squared_error(test_pacientes,test_predictions)}')


