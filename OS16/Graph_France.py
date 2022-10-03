# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:57:12 2022

@author: DAVID MORA MEZA

Este código necesita una librería que solo está disponible hasta el momento en Python 3.9 que está instalado en 
TensorFlow_Env pero esa versión no soporta otra librería que necesito, por lo que este código queda guardado.
"""

import pandas as pd
import geopandas
import matplotlib.pyplot as plt


link="https://raw.githubusercontent.com/davidmorme/Universidad/main/OS16/data/temp_et_coord_14villes.csv"
df=pd.read_csv(link, sep=";")

lista=[]
for i in range(len(df.columns)):
    lista.append(df.columns[i].replace("'",""))
df.columns=lista
del lista

df1=df.iloc[12:,:].transpose()
df1.columns=["Longitude","Latitude"]

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
France=world[world.name == 'France']
France=France.explode(index_parts=True, ignore_index=True)
France=France.iloc[1:3]

ax=France.plot(color='white', edgecolor='blue',figsize=(10, 10))
for i in range(len(df1)):
    ax.plot(df1.Longitude[i], df1.Latitude[i], "*", label=df1.index[i], markersize = 15)
    ax.text(df1.Longitude[i]*1.002, df1.Latitude[i]*1.002, df1.index[i], fontsize=14.5, rotation=45)

ax.grid(linestyle='--')
ax.set_title("Ubicación de las ciudades Longitud y Latitud", fontsize=15)
ax.set_xlabel("Longitude", fontsize=15)
ax.set_ylabel("Latitude", fontsize=15)
plt.show()

del df1, world, France

