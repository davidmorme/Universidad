# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:31:59 2022

@author: DAVID MORA MEZA
"""
import numpy as np
import sys

yi=np.array([0,0,1,2,0])
xi=np.array([0,1,1.5,0.5,0])

while True:
    x=float(input("Por favor ingrese x "))
    if sum(xi==x)>=1:
        print("Por favor ingrese otro valor cercano, x está en un vértice y puede generar problemas")
    else:
        break

y=float(input("Por favor ingrese y "))

ymax=max(yi)
R=[x,ymax+1]

cpt=0
n=len(yi)-1

for i in range(n):    
    if xi[i]!=xi[i+1]:
        m=(yi[i+1]-yi[i])/(xi[i+1]-xi[i])
        p=yi[i]-m*xi[i]
        xI=x
        yI=m*x+p
        
    if xI >= min(xi[i],xi[i+1]) and xI <= max(xi[i],xi[i+1]) and yI == y:
        print("Este punto queda sobre un lado del polígono")
        sys.exit()
        
    if ((xI-xi[i])*(xI-xi[i+1])<0 and (yI-y)*(yI-R[1])<0):
        cpt=cpt+1 
    
    
if cpt%2 != 0:
    print("El punto est à l'intérieur")
else:
    print("El punto est à l'extérieur")