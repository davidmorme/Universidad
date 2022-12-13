# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:17:16 2022

@author: DAVID MORA MEZA
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# import des données et tracé

Xl = np.genfromtxt('data/datageneratifXl.csv',delimiter=';') #Aquí quedan las coordenadas de los datos labeled
Yl = np.genfromtxt('data/datageneratifYl.csv',delimiter=';') #Aquí quedan las etiquedas (labels)
Xu = np.genfromtxt('data/datageneratifXu.csv',delimiter=';') #Aquí quedan el resto de datos que se encuentran los cuales no están labeled

nu = Xu.shape[0]
nl1 = np.sum (Yl==1) #Cantidad de datos labeled que son clasificados en la clase 1
nl2 = np.sum (Yl==2) #Cantidad de datos labeled que son clasificados en la clase 2

'''Esta parte es una separación de los datos labeled, (este código funciona porque están 
        ordenados los labels, si no, toca arreglarlo.)'''
nl = nl1+nl2 ;

Xl1 = Xl[Yl==1]
Xl2= Xl[Yl==2]
Yl1 = Yl[Yl==1]
Yl2= Yl[Yl==2]
X =  np.concatenate((Xl,Xu)) #Se crea un gran vector que contiene los datos labeled y the non-labeled


## vecteur xplot pour faire le trace des pdf
xmin= np.min(X,axis=0)-1
xmax = np.max(X,axis=0)+1
dx = 0.1 
x = np.arange(xmin[0], xmax[0], dx)
y = np.arange(xmin[1], xmax[1], dx)
xv, yv = np.meshgrid(x, y)


#Estimation de theta0
w1c = nl1/(nl1+nl2);
w2c = nl2/(nl1+nl2);

mu01 = np.mean(Xl1,axis=0)
mu02 = np.mean(Xl2,axis=0)

cov01 = np.cov(Xl1.T)
cov02 = np.cov(Xl2.T)

#%%

# densités estimées en xplot
'''stats.multivariate_normal.pdf([2,2], mean =[1,2], cov = [[1,0.5],[0.5,1]])'''

pdf1x=np.zeros_like(xv)
pdf2x=np.zeros_like(xv)
for i in range(0,xv.shape[0]):
    for j in range(0,xv.shape[1]):
        pdf1x[i,j]  = stats.multivariate_normal.pdf([xv[i,j], yv[i,j]], mean = mu01, cov = cov01) 
        pdf2x[i,j]  = stats.multivariate_normal.pdf([xv[i,j], yv[i,j]], mean = mu02, cov = cov02) 

#pdf1x  = stats.multivariate_normal.pdf([xv, yv], mean = mu01, cov = cov01)  # this function needs the standard deviation
#pdf2x  = stats.norm.pdf(xplot, loc =mu02, scale = sigma02)

#trace des points étiquetés en y= 06,
# points non etiquetes en y=0.5
# des densités estimées sur l'axe x

#%%
ax=plt.figure().add_subplot(projection='3d')
#plt.plot(Xl1,np.zeros(nl1)+0.6,'*r', markersize=2)
#plt.plot(Xl2,np.zeros(nl2)+0.6,'*b', markersize=2)      

pdf1x[pdf1x<0.00001]=np.nan
pdf2x[pdf2x<0.00001]=np.nan


ax.plot_surface(xv,yv,pdf1x, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8,
                alpha=0.3) 
ax.plot_surface(xv,yv,pdf2x, edgecolor='red', lw=0.5, rstride=8, cstride=8,
                alpha=0.3) 

fig, ax=plt.subplots()
ax.contour(xv,yv,pdf2x)
ax.contour(xv,yv,pdf1x) 

#plt.plot(Xu, np.zeros(nu)+0.5, 'ok', markersize=1)
 
#%%
pdf1_est  = stats.norm.pdf(Xu, loc =mu01, scale = sigma01)
pdf2_est  = stats.norm.pdf(Xu, loc =mu02, scale = sigma02)



D = w1c*pdf1_est+  w2c*pdf2_est
prob1c =   w1c*pdf1_est/D
prob2c =   w2c*pdf2_est/D
Yunew = (prob1c>=prob2c) + (prob2c>prob1c)*2 


plt.figure()
plt.plot(Xl1,np.zeros(nl1)+0.6,'*r', markersize=2)
plt.plot(Xl2,np.zeros(nl2)+0.6,'*b', markersize=2)        
plt.plot(xplot,pdf1x,'r',xplot,pdf2x,'b') 
Xu1= Xu[Yunew==1]
plt.plot(Xu1, np.zeros(np.shape(Xu1))+0.5, 'or', markersize=1)
Xu2= Xu[Yunew==2]
plt.plot(Xu2, np.zeros(np.shape(Xu2))+0.5, 'ob', markersize=1)

plt.title ("iteration 0")
#%%
iteration= 0
error = 1
while  (error >0.01)   :  
    prob1old = prob1c
    prob2old = prob2c
    iteration = iteration +1
    # step E
    w1c = np.sum(Yunew==1)/len(Yunew)
    w2c = np.sum(Yunew==2)/len(Yunew)
        
    mu01 = np.mean(np.concatenate((Xu[Yunew==1],Xl1)))
    mu02 = np.mean(np.concatenate((Xu[Yunew==2],Xl2)))
    
    sigma01 =  np.std(np.concatenate((Xu[Yunew==1],Xl1)))
    sigma02 =  np.std(np.concatenate((Xu[Yunew==2],Xl2)))   # to get the standard deviation
    
    #step M
    pdf1_est  = stats.norm.pdf(Xu, loc =mu01, scale = sigma01)
    pdf2_est  = stats.norm.pdf(Xu, loc =mu02, scale = sigma02)
    D = w1c*pdf1_est+  w2c*pdf2_est
    prob1c =   w1c*pdf1_est/D
    prob2c =   w2c*pdf2_est/D
    
    #determination of the labels
    Yunew = (prob1c>=prob2c) + (prob2c>prob1c)*2 
    
    error = (np.mean (abs(prob1old -prob1c))+np.mean (abs(prob1old -prob1c)))/2
    print (error)
    
        # densités estimées en xplot
    pdf1x  = stats.norm.pdf(xplot, loc =mu01, scale = sigma01)  # this function needs the standard deviation
    pdf2x  = stats.norm.pdf(xplot, loc =mu02, scale = sigma02)
     
    #trace des points étiquetés en y= 06,
    # points non etiquetes en y=0.5
    # des densités estimées sur l'axe x
    plt.figure()
    plt.plot(Xl1,np.zeros(nl1)+0.6,'*r', markersize=2)
    plt.plot(Xl2,np.zeros(nl2)+0.6,'*b', markersize=2)        
    plt.plot(xplot,pdf1x,'r',xplot,pdf2x,'b') 
    Xu1= Xu[Yunew==1]
    plt.plot(Xu1, np.zeros(np.shape(Xu1))+0.5, 'or', markersize=1)
    Xu2= Xu[Yunew==2]
    plt.plot(Xu2, np.zeros(np.shape(Xu2))+0.5, 'ob', markersize=1)
    plt.title ("iteration "+ str(iteration))
