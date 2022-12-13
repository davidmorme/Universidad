# -*- coding: utf-8 -*-
"""

@author: gralle
"""

# TP_semi_EM

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# import des données et tracé
Z = np.genfromtxt('data/data1D_semisupervise.csv',delimiter=';')
nl = 6 #Esta es la cantidad de datos la cual está ya labeled
Xl = Z[0:nl] #Aquí quedan las coordenadas de los datos labeled
Yl = Z[nl:nl*2] #Aquí quedan las etiquedas (labels)
Xu = Z[nl*2:] #Aquí quedan el resto de datos que se encuentran los cuales no están labeled

nu = Xu.shape[0]
nl1 = np.sum (Yl==1) #Cantidad de datos labeled que son clasificados en la clase 1
nl2 = np.sum (Yl==2) #Cantidad de datos labeled que son clasificados en la clase 2

'''Esta parte es una separación de los datos labeled, (este código funciona porque están 
        ordenados los labels, si no, toca arreglarlo.)'''
nl = nl1+nl2 ;

Xl1 = Xl[0:nl1]
Xl2= Xl[nl1:nl1+nl2]
Yl1 = Yl[0:nl1]
Yl2= Yl[nl1:nl1+nl2]
X =  np.concatenate((Xl,Xu)) #Se crea un gran vector que contiene los datos labeled y the non-labeled


## vecteur xplot pour faire le trace des pdf
xmin= np.min(X)-1
xmax = np.max(X)+1
dx = 0.1;   
xplot = np.arange (xmin,xmax,dx)


#Estimation de theta0
w1c = nl1/(nl1+nl2);
w2c = nl2/(nl1+nl2);

mu01 = np.sum(Xl1)/nl1
mu02 = np.sum(Xl2)/nl2

sigma01 = np.std(Xl1)
sigma02 = np.std(Xl2) 



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
plt.plot(Xu, np.zeros(nu)+0.5, 'ok', markersize=1)
 

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
    w1c = (np.sum(prob1c)+nl1)/(nu+nl)
    w2c = (np.sum(prob2c)+nl2)/(nu+nl)
        
    mu01 = (np.sum(prob1c*Xu)+np.sum(Xl1))/((nl+nu)*w1c)
    mu02 = (np.sum(prob2c*Xu)+np.sum(Xl2))/((nl+nu)*w2c)
    
    sigma01 =  np.sqrt( ( np.sum((Xl1-mu01)**2) + np.sum(prob1c*(Xu-mu01)**2)) / ((nl + nu)*w1c) )
    sigma02 =  np.sqrt( ( np.sum((Xl2-mu02)**2) + np.sum(prob2c*(Xu-mu02)**2)) / ((nl + nu)*w2c) )# to get the standard deviation
    
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
