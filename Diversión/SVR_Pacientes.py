# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 22:58:40 2022

@author: DAVID MORA MEZA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.kernel_ridge import KernelRidge

sns.set()
sns.set_context("paper")
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
dfPacientes.index=range(0,365)
dfPacientes['DisSen']=np.sin(dfPacientes.index/365*np.pi)
#%%

NPred=30



train_pacientes = dfPacientes[['Total']][:-NPred]
test_pacientes = dfPacientes[['Total']][-NPred:]


#%%

X_app=np.array(dfPacientes['DisSen'][:-NPred])
X_test=np.array(dfPacientes['DisSen'][-NPred:])
#X_test=np.array(dfPacientes['DisSen'])

#%%
gam=50
alph=0.007564633275546291
#alph=100

X_app=np.reshape(X_app, (len(X_app), 1))
X_test=np.reshape(X_test, (len(X_test), 1))

kr=KernelRidge(kernel='rbf', gamma=gam, alpha=alph)
kr.fit(X_app, train_pacientes['Total'])

#%%

test_predictions=pd.DataFrame(kr.predict(X_test),index=test_pacientes.index)


#%%
fig, ax= plt.subplots(figsize=(17, 7))
train_pacientes['Total'].plot(legend=True,label='TRAIN')
test_pacientes['Total'].plot(legend=True,label='TEST')
test_predictions[0].plot(legend=True,label='PREDICTION')

plt.title('Train, Test and Predicted Test using Holt Winters')



#%%
from sklearn.metrics import mean_absolute_error,mean_squared_error

print(f'Mean Absolute Error = {mean_absolute_error(test_pacientes,test_predictions)}')
print(f'Mean Squared Error = {mean_squared_error(test_pacientes,test_predictions)}')



#%%
n=100
res_err=np.zeros((n,1))
k=0
gam=50
Valpha=np.logspace(start=-10,stop=2,num=n)
for alph in Valpha:
    kr=KernelRidge(kernel='rbf', gamma=gam, alpha=alph)
    kr.fit(X_app, train_pacientes['Total'])
    Y_kr=kr.predict(X_test)
    res_err[k]=sum((test_pacientes['Total']-Y_kr)**2)
    k=k+1


#%%
alphaOp=Valpha[np.argmin(res_err)]
print('El alpha optimo calculado es:', alphaOp)


#%%
NPred=7
for i in range(1,NPred+1):
    dfPacientes[f'Total-{i}']=dfPacientes['Total'].shift(i)

dfPacientes.dropna(inplace=True)

#%%

X=np.array(dfPacientes)
ale=np.random.uniform(0,1,len(X))
va=ale>0.7

Y_train=X[:,0][va]
X_train=X[:,1:][va]

Y_test=X[:,0][np.logical_not(va)]
X_test=X[:,1:][np.logical_not(va)]

ordTrain=np.argsort(ale[va])

Y_train=Y_train[ordTrain]
X_train=X_train[ordTrain]
'''
ordTest=np.argsort(ale[np.logical_not(va)])

Y_test=Y_test[ordTest]
X_test=X_test[ordTest]
'''
#%%

#%%
gam=5000
alph=1.747528400007683e-10
#alph=100

X_train=np.reshape(X_train, (len(X_train), 8))
X_test=np.reshape(X_test, (len(X_test), 8))

kr=KernelRidge(kernel='linear', alpha=alph)
kr.fit(X_train, Y_train)

Y_kr=kr.predict(X_test)

sum((Y_test-Y_kr)**2)/len(Y_test)
#%%
print(f'Mean Absolute Error = {mean_absolute_error(Y_test,Y_kr)}')
print(f'Mean Squared Error = {mean_squared_error(Y_test,Y_kr)}')
#%%
fig, ax= plt.subplots(figsize=(17, 7))
ax.plot(dfPacientes.index[np.logical_not(va)],Y_test, label='Real')
ax.plot(dfPacientes.index[np.logical_not(va)],Y_kr, label='Predicción')
ax.set_title('30% de los datos predichos por la red', fontsize=15)
ax.legend(fontsize=10)

#%%

Y_kr=kr.predict(X[:,1:])
fig, ax= plt.subplots(figsize=(17, 7))
ax.plot(dfPacientes.index,dfPacientes['Total'], label='Real')
ax.plot(dfPacientes.index,Y_kr, label='Predicción')
ax.set_title('100% de los datos predichos por la red', fontsize=15)
ax.legend(fontsize=10)

#%%
n=100
res_err=np.zeros((n,1))
k=0
gam=50
Valpha=np.logspace(start=-10,stop=2,num=n)
for alph in Valpha:
    kr=KernelRidge(kernel='linear', alpha=alph)
    kr.fit(X_train, Y_train)
    Y_kr=kr.predict(X_test)
    res_err[k]=sum((Y_test-Y_kr)**2)/len(Y_test)
    k=k+1
#%%
alphaOp=Valpha[np.argmin(res_err)]
print('El alpha optimo calculado es:', alphaOp)

#%%
######################################## Validación Cruzada ####################################


X=np.array(dfPacientes)
ale=np.random.randint(0,5,len(X))
va=ale==0

Y_train=X[:,0][va]
X_train=X[:,1:][va]

Y_test=X[:,0][np.logical_not(va)]
X_test=X[:,1:][np.logical_not(va)]

#%%
n=100
res_err=np.zeros((n,1))
k=0
gam=50
Valpha=np.logspace(start=2,stop=10,num=n)
for alph in Valpha:
    kr=KernelRidge(kernel='linear', alpha=alph)
    kr.fit(X_train, Y_train)
    Y_kr=kr.predict(X_test)
    res_err[k]=sum((Y_test-Y_kr)**2)/len(Y_test)
    k=k+1
#%%
alphaOp=Valpha[np.argmin(res_err)]
print('El alpha optimo calculado es:', alphaOp)

#%%

alph=alphaOp

X_train=np.reshape(X_train, (len(X_train), 8))
X_test=np.reshape(X_test, (len(X_test), 8))

kr=KernelRidge(kernel='linear', alpha=alph)
kr.fit(X_train, Y_train)

Y_kr=kr.predict(X_test)

sum((Y_test-Y_kr)**2)/len(Y_test)
#%%
print(f'Mean Absolute Error = {mean_absolute_error(Y_test,Y_kr)}')
print(f'Mean Squared Error = {mean_squared_error(Y_test,Y_kr)}')

# MSE(0)=674.485
# MSE(1)=689.928
# MSE(2)=701.134
# MSE(3)=692.794
# MSE(4)=787.963



#%%
fig, ax= plt.subplots(figsize=(17, 7))
ax.plot(dfPacientes.index[np.logical_not(va)],Y_test, label='Real')
ax.plot(dfPacientes.index[np.logical_not(va)],Y_kr, label='Predicción')
ax.set_title('30% de los datos predichos por la red', fontsize=15)
ax.legend(fontsize=10)

#%%

Y_kr=kr.predict(X[:,1:])
fig, ax= plt.subplots(figsize=(17, 7))
ax.plot(dfPacientes.index,dfPacientes['Total'], label='Real')
ax.plot(dfPacientes.index,Y_kr, label='Predicción')
ax.set_title('100% de los datos predichos por la red', fontsize=15)
ax.legend(fontsize=10)
