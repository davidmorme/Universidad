# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

from keras import layers
from keras import models
from keras.datasets import mnist
from keras.utils import to_categorical

#--------  Importer les données------------------------#
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
#--------- visualiser une image de la BDD
digit=test_images[4]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()
#-------------------Ecrire modèle Full Connected-------------------------------------##
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))
network.summary()
#---------------- Ecrire le modèle du CNN ---------------##
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
##
model.summary()
#----------------------------------------------------------#
#------  Mise en forme des données -------------------------#
train_images = train_images.reshape((60000, 28, 28, 1))
#train_images = train_images.reshape(60000, 28*28)
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1))
#test_images = test_images.reshape(10000, 28*28)
test_images = test_images.astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
x_val = train_images[:20000]
x_train=train_images[20000:]
y_val = train_labels[:20000]
y_train = train_labels[20000:]

#--------------Apprentissage du NN------------------------------------------#
model.compile(optimizer= 'rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10, batch_size=64)
 
#----------------Evalution sur la base Test------------------------------------#
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc:', test_acc)
layer_outputs = [layer.output for layer in model.layers[:3]]
activation_model = models.Model(inputs=model.input, outputs=layer_outputs)
img_tensor = test_images[4]
img_tensor = np.expand_dims(img_tensor, axis=0)
#plt.imshow(img_tensor[0,:,:,:])
plt.imshow(img_tensor[0,:,:,0])
plt.show()
activations = activation_model.predict(img_tensor)
first_layer_activation = activations[0]
plt.matshow(first_layer_activation[0, :, :, 4], cmap='viridis')
plt.matshow(first_layer_activation[0, :, :, 30], cmap='viridis')
model.predict(img_tensor)
