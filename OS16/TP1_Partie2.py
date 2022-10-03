# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:20:17 2022

@author: DAVID MORA MEZA
"""

import tensorflow as tf
import tensorflow_datasets as tfds

#Descargar set de datos de MNIST (Números escritos a mano, etiquetados)
datos, metadatos =tfds.load('mnist', as_supervised=True, with_info=True)

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
datos_entrenamiento = datos_entrenamiento.cache()
datos_pruebas = datos_pruebas.cache()

clases = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']