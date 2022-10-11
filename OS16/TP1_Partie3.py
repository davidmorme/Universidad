# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:59:41 2022

@author: DAVID MORA MEZA
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#%%
def PCA(donn):
    d,N=np.shape(donn)
    cov=np.matmul(donn,np.transpose(donn))/N #Matriz de covarianza
    
    #ValProp es el valor propio y VecProp es el vector propio
    ValProp, VecProp = np.linalg.eig(cov)
    order=np.argsort(-ValProp, axis=0)
    ValProp=ValProp[order]
    VecProp=VecProp[:,order]
    mI=ValProp/np.sum(ValProp)
    SumAcumI=np.cumsum(mI)
    if d > 2:
        Y=VecProp[:,0:2].T@donn #Y es el conjunto de datos proyectado
    else:
        Y=VecProp[:,0].T@donn #Y es el conjunto de datos proyectado
    CoefCorr=np.sqrt(ValProp)*VecProp/np.std(donn ,axis=1)[order]
    
    return Y, CoefCorr, mI, SumAcumI

#%%
def Cercle_corr(CoefCorr,iTitle):
    Titles=["Cercle des corrélations avec les données brutes","Cercle des corrélations avec la coordonnée1/100","Cercle des corrélations avec les données normalisées"]
    theta = np.linspace(0, 2*np.pi, 100)
    r = np.sqrt(1.0)
    
    x1 = r*np.cos(theta)
    x2 = r*np.sin(theta)
    
    fig, ax = plt.subplots(1,1, figsize = (10, 10))
    
    ax.plot(x1, x2, color="blue")
    ax.set_aspect(1)
    
    ax.set_xlim(-1.25,1.25)
    ax.set_ylim(-1.15,1.15)
    
    ax.grid(linestyle='--')
    
    r1=CoefCorr[:,0]
    r2=CoefCorr[:,1]
    
    ax.plot(r1,r2,'*k')
    
    for i in range(len(r1)):
        ax.text(r1[i]*1.1,r2[i]*1.1,"Coord "+str(i+1),va="center",ha="center",fontsize=14.5)
        ax.plot(np.array([0,r1[i]]),np.array([0,r2[i]]), color="red", linewidth=0.5)
        
    ax.set_xlabel("Component 1", fontsize=15)
    ax.set_ylabel("Component 2", fontsize=15)
    ax.set_title(Titles[iTitle], fontsize=20)
    
    #plt.savefig("Cercle_corr.png", bbox_inches='tight')
    plt.show()

#%%
'''########################### Partie A #########################'''
df=pd.read_csv('data/filedonnees_2D.csv', sep = ';', header=None)
donnA=df.to_numpy()

#%%
fig, ax = plt.subplots(1,1, figsize = (10, 10))

ax.plot(donnA[0], donnA[1], ".", markersize = 15)

ax.grid(linestyle='--')
ax.set_title("Emplacement des points dans l'espace des données brutes", fontsize=15)
ax.set_xlabel("Coordonée 1", fontsize=15)
ax.set_ylabel("Coordonée 2", fontsize=15)

#plt.savefig("Donn_Brut.png", bbox_inches='tight')
plt.show()

#%%

YA, CoefCorrA, mIA, SumAcumIA = PCA(donnA)
#%%

fig, ax = plt.subplots(1,1, figsize = (10, 1))

ax.plot(YA, np.zeros(12), ".", markersize = 15)

ax.grid(linestyle='--')
ax.set_title("Projection sur les données brutes de la composante 1", fontsize=15)
ax.set_xlabel("Component 1", fontsize=15)

#plt.savefig("Proj_Donn_Brut.png", bbox_inches='tight')
plt.show()

#%%
Cercle_corr(CoefCorrA,0)

#%%
'''########################### Partie B #########################'''
donnB=donnA
donnB[0]=donnB[0]/100

#%%
fig, ax = plt.subplots(1,1, figsize = (10, 10))

ax.plot(donnB[0], donnB[1], ".", markersize = 15)

ax.grid(linestyle='--')
ax.set_title("Emplacement des points dans l'espace de la coordonnée1/100", fontsize=15)
ax.set_xlabel("Coordonée 1", fontsize=15)
ax.set_ylabel("Coordonée 2", fontsize=15)

#plt.savefig("Donn_Coor1_div_100.png", bbox_inches='tight')
plt.show()

#%%

YB, CoefCorrB, mIB, SumAcumIB = PCA(donnB)
#%%

fig, ax = plt.subplots(1,1, figsize = (10, 1))

ax.plot(YB, np.zeros(12), ".", markersize = 15)

ax.grid(linestyle='--')
ax.set_title("Projection sur les données brutes de la composante 1 coordonnée1/100", fontsize=15)
ax.set_xlabel("Component 1", fontsize=15)

#plt.savefig("Proj_Coor1_div_100.png", bbox_inches='tight')
plt.show()

#%%
Cercle_corr(CoefCorrB,1)

#%%
'''########################### Partie C #########################'''
m=np.mean(donnA,axis=1)
sdDonn = np.std(donnA,axis=1)

donnC = ((donnA.T-m) / sdDonn).T      #Donnes centres et reduits


#%%
fig, ax = plt.subplots(1,1, figsize = (10, 10))

ax.plot(donnC[0], donnC[1], ".", markersize = 15)

ax.grid(linestyle='--')
ax.set_title("Emplacement des points dans l'espace des données normalisées", fontsize=15)
ax.set_xlabel("Coordonée 1", fontsize=15)
ax.set_ylabel("Coordonée 2", fontsize=15)

#plt.savefig("Donn_Norm.png", bbox_inches='tight')
plt.show()

#%%

YC, CoefCorrC, mIC, SumAcumIC = PCA(donnC)
#%%

fig, ax = plt.subplots(1,1, figsize = (10, 1))

ax.plot(YC, np.zeros(12), ".", markersize = 15)

ax.grid(linestyle='--')
ax.set_title("Projection sur les données normalisées de la composante 1", fontsize=15)
ax.set_xlabel("Component 1", fontsize=15)

#plt.savefig("Proj_Donn_Norm.png", bbox_inches='tight')
plt.show()

#%%
Cercle_corr(CoefCorrC,2)
