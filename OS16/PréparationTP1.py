# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:17:28 2022

@author: DAVID MORA MEZA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

execfile('Graph_France.py')

#%%
'''
fig, ax = plt.subplots(1,1, figsize = (21, 8))

for i in range(len(nomvilles)):
    ax.plot(donn[12,i], donn[13,i], "*", label=nomvilles[i], markersize = 10)
    ax.text(donn[12,i]*1.002, donn[13,i]*1.002, nomvilles[i], fontsize=14.5)
    
ax.set_xlabel("Longitude", fontsize=18)
ax.set_ylabel("Latitude", fontsize=18)
ax.set_title("Ubicación de las ciudades Longitud y Latitud", fontsize=25)

#ax.legend()
fig.show()
'''
#%%
fig, ax = plt.subplots(1,1, figsize = (21, 8))
mois=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juliet', 'Août','Septembre','Octobre','Novembre','Décembre']

ax.plot(donn[0:12,:], label=nomvilles, markersize = 10, linestyle=":", marker=".");

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
#Puedo hacer todo esto 

donn=donn[0:12]
d,N=np.shape(donn)
m=np.mean(donn,axis=1)
donnC=(donn.T-m).T       #Donnes centres

#%%
fig, ax = plt.subplots(1,1, figsize = (21, 8))

ax.plot(donnC, label=nomvilles, markersize = 10, linestyle=":", marker=".");

ax.set_xticks(range(0,12),mois,rotation=45)
ax.set_xlabel("Mois", fontsize=18)
ax.set_ylabel("Température avec Centrer", fontsize=18)
ax.set_title("Température avec Centrer vs Mois de chaque ville", fontsize=25)

ax.legend()
fig.show()

#%%
donnC=donnC.T
sdDonnC = np.sqrt(np.sum(np.square(donnC),1)/N) #Ecart type de le Donne centre
donnC = donnC[sdDonnC != 0] # enlever les dimesnions où il y a une variance nulle

sdDonnC = np.sqrt((np.sum(np.square(donnC),1))/N)
donnCR = (donnC.T / sdDonnC).T      #Donnes centres et reduits

cov=np.matmul(donnCR,np.transpose(donnCR))/N #Matriz de covarianza

#cov = np.cov(donnCR, bias=True)

#%%
fig, ax = plt.subplots(1,1, figsize = (21, 8))

ax.plot(donnCR, label=nomvilles, markersize = 10, linestyle=":", marker=".");

ax.set_xticks(range(0,12),mois,rotation=45)
ax.set_xlabel("Mois", fontsize=18)
ax.set_ylabel("Température avec Centrer et Reduit", fontsize=18)
ax.set_title("Température avec Centrer et Reduit vs Mois de chaque ville", fontsize=25)

ax.legend()
fig.show()

#%%

#Landa es el valor propio y "x" es el vector propio
Landa, x = np.linalg.eig(cov)

order=np.argsort(-Landa, axis=0)
x=x[order]
Landa=Landa[order]

mI=Landa/np.sum(Landa)
#%%
fig, ax = plt.subplots(1,1, figsize = (21, 8))

ax.bar(range(1,13),mI)

ax.set_xticks(range(1,13))
ax.set_yticks(np.arange(0,1,step=0.1),range(0,100,10))
ax.set_xlabel("Valores propios", fontsize=18)
ax.set_ylabel("Percentaje of importance (%)", fontsize=18)
ax.set_title("Percentaje of importance of each valeur propes", fontsize=25)

ax.legend()
fig.show()
#%%
X_proj=np.dot(x.T,donn)

fig, ax = plt.subplots(1,1, figsize = (21, 8))
mois=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juliet', 'Août','Septembre','Octobre','Novembre','Décembre']

ax.plot(X_proj, label=nomvilles, markersize = 10, linestyle=":", marker=".");

ax.set_xticks(range(0,12),mois,rotation=45)
ax.set_xlabel("Mois", fontsize=18)
ax.set_ylabel("Projection de Température", fontsize=18)
ax.set_title("Projection de Température vs Mois de chaque ville", fontsize=25)

ax.legend()
fig.show()

#%%


plt.matshow(np.corrcoef (X_proj))
