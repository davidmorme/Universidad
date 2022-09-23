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
lista=[]
for i in range(len(df.columns)):
    lista.append(nomvilles[i].replace("'",""))

print(lista)
#%%


fig, ax = plt.subplots(1,1, figsize = (21, 8))

ax.plot(donn[12,0], donn[13,0], "*", label=nomvilles[0], markersize = 10);
ax.plot(donn[12,1], donn[13,1], "*", label=nomvilles[1], markersize = 10);
ax.plot(donn[12,2], donn[13,2], "*", label=nomvilles[2], markersize = 10);

for i in range(len(nomvilles)):
    ax.plot(donn[12,i], donn[13,i], "*", label=nomvilles[i], markersize = 10);
    ax.text(donn[12,i]*1.002, donn[13,i]*1.002, nomvilles[i], fontsize=14.5)
    
ax.set_xlabel("Longitud", fontsize=18)
ax.set_ylabel("Latitud", fontsize=18)
ax.set_title("Ubicación de las ciudades Longitud y Latitud", fontsize=25)

#ax.legend()
fig.show()
