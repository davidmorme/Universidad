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
donn=donn[0:12]

lista=[]
for i in range(len(df.columns)):
    lista.append(df.columns[i].replace("'",""))
df.columns=lista
del lista

nomvilles=df.columns


#%%

execfile('Graph_France.py')

#%%
fig, ax = plt.subplots(1,1, figsize = (21, 8))
mois=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août','Septembre','Octobre','Novembre','Décembre']

ax.plot(donn, label=nomvilles, markersize = 10, linestyle=":", marker=".");

ax.set_xticks(range(0,12),mois,rotation=45)
ax.set_xlabel("Mois", fontsize=18)
ax.set_ylabel("Température", fontsize=18)
ax.set_title("Température vs Mois de chaque ville", fontsize=25)
ax.grid(linestyle='--')

ax.legend()
fig.show()

#%%

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
ax.grid(linestyle='--')

ax.legend()
fig.show()

#%%

sdDonnC = np.std(donn,axis=1) #Ecart type de le Donne centre
donnC = donnC[sdDonnC != 0] # enlever les dimesnions où il y a une variance nulle

sdDonnC = np.std(donn,axis=1)
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
ax.grid(linestyle='--')

ax.legend()
fig.show()

#%%

#ValProp es el valor propio y VecProp es el vector propio
ValProp, VecProp = np.linalg.eig(cov)

order=np.argsort(-ValProp, axis=0)

ValProp=ValProp[order]
VecProp=VecProp[:,order]

mI=ValProp/np.sum(ValProp)
SumAcumI=np.cumsum(mI)

#%%
fig, ax = plt.subplots(1,1, figsize = (21, 8))

ax.bar(range(1,13),mI)
ax.plot(range(1,13),SumAcumI, color="red")

ax.set_xticks(range(1,13))
ax.set_yticks(np.arange(0,1.1,step=0.1),range(0,101,10))
ax.set_xlabel("Valores propios", fontsize=18)
ax.set_ylabel("Percentaje of importance (%)", fontsize=18)
ax.set_title("Percentaje of importance of each valeur propes (component)", fontsize=25)
ax.grid(linestyle='--')

ax.legend()
fig.show()

#%%
Y=VecProp[:,0:2].T@donnCR #Y es el conjunto de datos proyectado

#%%
fig, ax = plt.subplots(1,1, figsize = (21, 8))

for i in range(len(nomvilles)):
    ax.plot(Y[0,i], Y[1,i], "*", label=nomvilles[i], markersize = 10)
    ax.text(Y[0,i]+0.03, Y[1,i]+0.03, nomvilles[i], fontsize=14.5)

ax.grid(linestyle='--')    
ax.set_xlabel("Component 1", fontsize=18)
ax.set_ylabel("Component 2", fontsize=18)
ax.set_title("Projection de les villes en les componentes 1 et 2", fontsize=25)

#ax.legend()
fig.show()

#%%

CoefCorr=np.sqrt(ValProp)*VecProp

#%%
'''=========================================================='''
''' code pour tracer les cercle des corrélations après avoir calculé 
le vecteur de corrélation r en 2 Dimensions'''

theta = np.linspace(0, 2*np.pi, 100)
r = np.sqrt(1.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

fig, ax = plt.subplots(1,1, figsize = (10, 10))

ax.plot(x1, x2, color="blue")
ax.set_aspect(1)

ax.set_xlim(-1.25,1.25)
ax.set_ylim(-1.05,1.05)

ax.grid(linestyle='--')

r1=CoefCorr[:,0]
r2=CoefCorr[:,1]

ax.plot(r1,r2,'*k')

for i in range(len(mois)):
    ax.text(r1[i]*1.0,r2[i]*1.08,mois[i],va="center",ha="left",fontsize=14.5)
    ax.plot(np.array([0,r1[i]]),np.array([0,r2[i]]), color="red", linewidth=0.5)
    
ax.set_xlabel("Component 1", fontsize=15)
ax.set_ylabel("Component 2", fontsize=15)
ax.set_title("Cercle des corrélations", fontsize=20)

plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')
plt.show()
