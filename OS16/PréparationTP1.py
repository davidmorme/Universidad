# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:17:28 2022

@author: DAVID MORA MEZA
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow import keras
from keras.layers import Dense
#%%
df=pd.read_csv('data/temp_et_coord_14villes.csv', sep = ';')
donn=df.to_numpy()

lista=[]
for i in range(len(df.columns)):
    lista.append(df.columns[i].replace("'",""))
df.columns=lista
del lista

nomvilles=df.columns

#%%


fig, ax = plt.subplots(1,1, figsize = (21, 8))

for i in range(len(nomvilles)):
    ax.plot(donn[12,i], donn[13,i], "*", label=nomvilles[i], markersize = 10);
    ax.text(donn[12,i]*1.002, donn[13,i]*1.002, nomvilles[i], fontsize=14.5)
    
ax.set_xlabel("Longitude", fontsize=18)
ax.set_ylabel("Latitude", fontsize=18)
ax.set_title("Ubicación de las ciudades Longitud y Latitud", fontsize=25)

#ax.legend()
fig.show()


#%%
fig, ax = plt.subplots(1,1, figsize = (21, 8))
mois=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juliet', 'Août','Septembre','Octobre','Novembre','Décembre']

ax.plot(donn[0:12,:], label=nomvilles, markersize = 10);

ax.set_xticks(range(0,12),mois,rotation=45)
ax.set_xlabel("Mois", fontsize=18)
ax.set_ylabel("Température", fontsize=18)
ax.set_title("Température vs Mois de chaque ville", fontsize=25)

ax.legend()
fig.show()

#%%

maxT=np.max(donn[0:12,])
minT=np.min(donn[0:12,])

donnN=(donn[0:12]-minT)/(maxT-minT)

#%%

moyenneT=np.mean(donn[0:12,])
stdT=np.std(donn[0:12,])

donnN=(donn[0:12]-moyenneT)/stdT

#%%
fig, ax = plt.subplots(1,1, figsize = (21, 8))

ax.plot(donnN, label=nomvilles, markersize = 10);

ax.set_xticks(range(0,12),mois,rotation=45)
ax.set_xlabel("Mois", fontsize=18)
ax.set_ylabel("Température avec normalisation", fontsize=18)
ax.set_title("Température avec normalisation vs Mois de chaque ville", fontsize=25)

ax.legend()
fig.show()
#%%
#Puedo hacer todo esto 
X=np.matrix(donn[0:12])
d,N=np.shape(X)
m=np.mean(X,axis=1)
SG=np.matmul(X-m,np.transpose(X-m))/N

#%%
#O simplemente usar la función que me calcula la matriz de covarianza
#X=np.matrix(donn[0:12])
X=np.matrix(donnN)
cov = np.cov(X, bias=True)

#%%
A=np.array([[1,1],[0,2]])

#Landa es el valor propio y "x" es el vector propio
Landa, x = np.linalg.eig(A)

print(A@x-Landa*x)



