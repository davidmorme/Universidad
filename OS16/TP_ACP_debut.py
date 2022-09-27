# -*- coding: utf-8 -*-
"""


@author: gralle
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


''' PARTIE 1
====================================================
'''

df =pd.read_csv('data/temp_et_coord_14villes.csv', sep=';') 
donn = df.to_numpy()
# colonnes = np.asarray([df['  nomclone ‘].tolist,df['  nomclone2 ‘].tolist])
temperatures = donn[0:12,:]
coordonnees = donn[12:14,:]
plt.plot(coordonnees[0,:],coordonnees[1,:],'.', markersize=10)
nomvilles = df.columns

# tracé des coordonnées
for i in range(len(nomvilles)):
    plt.text(coordonnees[0,i],coordonnees[1,i],nomvilles[i],va="bottom",ha="center",fontsize=8)               

plt.figure()
plt.plot(temperatures)

# centrer et réduire les données
Xmoy = np.mean(temperatures, axis = 1) ;
X = (temperatures.T - Xmoy).T;
plt.figure()
plt.plot(X)

#%%
N = X.shape[1]
X2 = np.sqrt((np.sum(np.square(X),1))/N)
X = X[X2 != 0] # enlever les dimesnions où il y a une variance nulle
d = X.shape[0]
X2 = np.sqrt((np.sum(np.square(X),1))/N)
X3 = (X.T / X2).T
plt.figure()
plt.plot(X3)

#%%
'''=========================================================='''
''' code pour tracer les cercle des corrélations après avoir calculé 
le vecteur de corrélation r en 2 Dimensions'''

theta = np.linspace(0, 2*np.pi, 100)
r = np.sqrt(1.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)

plt.xlim(-1.25,1.25)
plt.ylim(-1.05,1.05)

plt.grid(linestyle='--')

plt.plot(r1,r2,'*k')
moisname =['Janv', 'Fév','Mars','Avril','Mai','Juin','Juillet','Aout', 'Sept', 'Oct', 'Nov', 'Dec'];
for i in range(len(moisname)):
    plt.text(r1[i]+0.15,r2[i],moisname[i],va="center",ha="center",fontsize=8)
    

plt.title('cercle des corrélations', fontsize=8)
plt.show()
plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')


'''=========================================================================
PARTIE 2 : données MNIST
'''
from keras.datasets import mnist
import matplotlib.cm as cm

cmap =cm.tab10


# mnist est un tuple. on extrait les différentes parties
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

nb = 500 # nombre de valeurs retenues
train_images = train_images[0:nb,:]
train_labels = train_labels[0:nb]


''' représenter l exemple numero k'''
k = 15

plt.imshow(train_images[k],cmap=plt.cm.gray_r)

''' transformer chaque échantillon qui est 
sous forme d'une matrice 2D de taille 28 sur 28 
en un vecteur  1D de taille 28*28
''' 
X = np.reshape(train_images,(nb,28*28))
X = X.T

''' centrer et réduire X puis faire l'ACP
garder les 2 premiers axes dans la matrice Y
'''


'''  réaliser la carte factorielle des individus sur  les deux axes principaux,
en représentant chaque échantillon par un point dont la couleur dépend du chiffre
'''
NUM_COLORS = 10 
Fig, ax = plt.subplots()
for i in range(10):
    select = (train_labels== i)
    plt.plot(Y[0,select],Y[1,select],
             color =  cmap(i),
             marker='o',
             markersize=4,
              linestyle = 'None',
              label = i)
ax.legend(numpoints=1)
plt.xlabel('1ere composante')
plt.ylabel('2eme composante')
plt.show()
