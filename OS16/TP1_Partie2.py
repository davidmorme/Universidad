# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:20:17 2022

@author: DAVID MORA MEZA
"""

import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt

#%%

#Descargar set de datos de MNIST (Números escritos a mano, etiquetados)
datos, metadatos =tfds.load('mnist', as_supervised=True, with_info=True)
#%%
#Obtener en variables separadas los datos de entrenamiento (60k) y pruebas (10k)
datos_entrenamiento, datos_pruebas = datos['train'], datos['test']

#Función de normalización para los datos (Pasar valor de los piceles de 0-255 a 0-1)
#(Hace que la red aprenda mejor y más rápido)

def normalizar(imagenes, etiquetas):
  imagenes = tf.cast(imagenes, tf.float32)
  imagenes /= 255 #Aquí se pasa de 0-255 a 0-1
  return imagenes, etiquetas

#Normalizar los datos de entrenamiento con la función que hicimos

datos_entrenamiento=datos_entrenamiento.map(normalizar)
datos_pruebas=datos_pruebas.map(normalizar)

#Agregar a cache (usar memoria en lugar de disco, entrenamiento mas rapido)
#datos_entrenamiento = datos_entrenamiento.cache()
#datos_pruebas = datos_pruebas.cache()

clases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#%%

Muestra=60000
donn=np.zeros((28*28,Muestra))
etiquetas=np.zeros(Muestra)
for i, (imagen, etiqueta) in enumerate(datos_entrenamiento.take(Muestra)):
  donn[:,i] = imagen.numpy().reshape(28*28)
  etiquetas[i] = clases[etiqueta]

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
    Y=VecProp.T@donn #Y es el conjunto de datos proyectado
    CoefCorr=np.sqrt(ValProp)*VecProp/np.std(donn ,axis=1)[order]
    
    return Y, CoefCorr, mI, SumAcumI

#%%

sdDonn = np.std(donn,axis=1) #Ecart type de le Donne centre
donn = donn[sdDonn != 0] # enlever les dimesnions où il y a une variance nulle

#%%
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
Y, CoefCorr, mI, SumAcumI = PCA(donn)

#%%

fig, ax = plt.subplots(1,1, figsize = (21, 8))

ax.plot(Y[0], Y[1], ".", markersize = 10)

ax.grid(linestyle='--')    
ax.set_xlabel("Component 1", fontsize=18)
ax.set_ylabel("Component 2", fontsize=18)
ax.set_title("Représentation sur les deux premiers axes", fontsize=25)

plt.savefig("Rep_2_axes.png", bbox_inches='tight')
fig.show()

#%%

fig, ax = plt.subplots(1,1, figsize = (21, 8))

for i in clases:
    num = etiquetas==i
    ax.plot(Y[0][num], Y[1][num], ".", markersize = 10, label = i)

ax.grid(linestyle='--')    
ax.set_xlabel("Component 1", fontsize=18)
ax.set_ylabel("Component 2", fontsize=18)
ax.set_title("Représentation sur les deux premiers axes", fontsize=25)

ax.legend()

plt.savefig("Rep_2_axes_Col.png", bbox_inches='tight')
fig.show()
#%%
alpha=0.05
limSup=sum(SumAcumI<1-alpha)
fig, ax = plt.subplots(1,1, figsize = (21, 8))

ax.bar(range(1,len(mI)+1),mI)
ax.plot(range(1,len(mI)+1),SumAcumI, color="red")

ax.set_yticks(np.arange(0,1.1,step=0.1),range(0,101,10))
ax.set_xlabel("Valeurs propres", fontsize=18)
ax.set_ylabel("Percentaje of importance (%)", fontsize=18)
ax.set_title("Pourcentage d'inertie pour axe (component)", fontsize=25)
ax.grid(linestyle='--')
ax.set_xlim((0,limSup))

ax.legend()

plt.savefig("Pour_Inertie.png", bbox_inches='tight')
fig.show()
