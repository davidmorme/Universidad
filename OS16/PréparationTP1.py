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
mois=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août','Septembre','Octobre','Novembre','Décembre']

ax.plot(donn[0:12,:], label=nomvilles, markersize = 10, linestyle=":", marker=".");

ax.set_xticks(range(0,12),mois,rotation=45)
ax.set_xlabel("Mois", fontsize=18)
ax.set_ylabel("Température", fontsize=18)
ax.set_title("Température vs Mois de chaque ville", fontsize=25)

ax.legend()
fig.show()

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

ax.legend()
fig.show()

#%%
'''
A=np.array([[1,2,3],
            [5,6,7],
            [8,9,10]])

ValProp, VecProp = np.linalg.eig(A)

order=np.argsort(-ValProp, axis=0)
ValProp1=ValProp[order]
VecProp1=VecProp[:,order]


A1=ValProp*VecProp
A2=ValProp1*VecProp1
#%%

A1=A@VecProp
A2=A@VecProp1

'''


#%%
X_proj=(np.dot(donnCR.T,VecProp)).T

#%%
fig, ax = plt.subplots(1,1, figsize = (21, 8))

for i in range(len(nomvilles)):
    ax.plot(X_proj[0,i], X_proj[1,i], "*", label=nomvilles[i], markersize = 10)
    ax.text(X_proj[0,i]+0.03, X_proj[1,i]+0.03, nomvilles[i], fontsize=14.5)
    
ax.set_xlabel("Component 1", fontsize=18)
ax.set_ylabel("Component 2", fontsize=18)
ax.set_title("Projection de les villes en les componentes 1 et 2", fontsize=25)

#ax.legend()
fig.show()

#%%

B=np.corrcoef(VecProp[0],VecProp[1:])


#%%
Factor=1/(VecProp[:,0]**2+VecProp[:,1]**2)
VecProp1=(np.sqrt(Factor)*VecProp.T).T
print(VecProp1[:,0]**2+VecProp1[:,1]**2)

#%%
'''=========================================================='''
''' code pour tracer les cercle des corrélations après avoir calculé 
le vecteur de corrélation r en 2 Dimensions'''

theta = np.linspace(0, 2*np.pi, 100)
r = np.sqrt(1.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

fig, ax = plt.subplots(1,1, figsize = (21, 8))

ax.plot(x1, x2)
ax.set_aspect(1)

plt.xlim(-1.25,1.25)
plt.ylim(-1.05,1.05)

plt.grid(linestyle='--')

r1=VecProp1[:,0]
r2=VecProp1[:,1]

plt.plot(r1,r2,'*k')

for i in range(len(mois)):
    plt.text(r1[i]*1.08,r2[i]*1.08,mois[i],va="center",ha="center",fontsize=14.5)
    plt.plot(np.array([0,r1[i]]),np.array([0,r2[i]]), color="red", linewidth=0.5)
    
ax.set_xlabel("Component 1", fontsize=15)
ax.set_ylabel("Component 2", fontsize=15)
ax.set_title("Cercle des corrélations", fontsize=20)

plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')
plt.show()



