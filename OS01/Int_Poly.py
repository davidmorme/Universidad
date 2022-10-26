# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:31:59 2022

@author: DAVID MORA MEZA
"""
import numpy as np


def Int_Ext(xi,yi,x,y):
    
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
            return True
        
        if ((xI-xi[i])*(xI-xi[i+1])<0 and (yI-y)*(yI-R[1])<0):
            cpt=cpt+1 
                    
                    
    if cpt%2 != 0:
        return True
    else:
        return False
    
def PuntoUsuario(xi,yi):
    while True:
        x=float(input("Por favor ingrese x "))
        if sum(xi==x)>=1:
            print("Por favor ingrese otro valor cercano, x está en un vértice y puede generar problemas")
        else:
            break

    y=float(input("Por favor ingrese y "))
    
    B=Int_Ext(xi,yi,x,y)
    
    if B:
        print("El punto est à l'intérieur")
    else:
        print("El punto est à l'extérieur")
    


def PuntInu(xi,yi):
    dy=(yi[1:]-yi[0:-1])
    dx=(xi[1:]-xi[0:-1])
    
    if sum(dx==0)==0:
        m=dy/dx
    else:
        m=dx/dy

    In=m==np.concatenate((m[[-1]],m[0:-1]))
    
    ny=yi[0:-1][np.logical_not(In)]
    nx=xi[0:-1][np.logical_not(In)]
    
    ny=np.concatenate((ny,ny[[0]]))
    nx=np.concatenate((nx,nx[[0]]))
                      
    return nx, ny

def perimeter(xi,yi):
    dy=(yi[1:]-yi[0:-1])
    dx=(xi[1:]-xi[0:-1])
    
    d=sum(np.sqrt(dy**2+dx**2))
    return d

def regular(xi,yi):
    
    n=len(yi)-1
    
            
    ny=yi[2:-2]
    nx=xi[2:-2]
    dy=ny-yi[0]
    dx=nx-xi[0]
    x=list(xi[0]+dx/2)
    y=list(yi[0]+dy/2)
    
    
    for i in range(1,n-2):
        
        ny=yi[i+2:-1]
        nx=xi[i+2:-1]
        dy=ny-yi[i]
        dx=nx-xi[i]
        
        x.extend(list(xi[i]+dx/2))
        y.extend(list(yi[i]+dy/2))
    
    for i in range(len(x)):
        if not(Int_Ext(xi,yi,x[i],y[i])):
            return False
    
    return True
    
    



n=4
'''
yi=np.array([0,0,1,2])
xi=np.array([0,1,1.5,0.5])

yi=np.array([0,0,0.5,1,1])
xi=np.array([0,1,1,1,0])

yi=np.array([0,0,1,1,0])
xi=np.array([0.5,1,1,0,0])


yi=np.array([0,0,1,1.5,1])
xi=np.array([0,1,1,0.6,0])
'''

yi=np.array([0,0,1,0.9,1])
xi=np.array([0,1,1,0.6,0])

yi=np.concatenate((yi,yi[[0]]))
xi=np.concatenate((xi,xi[[0]]))

xi,yi=PuntInu(xi, yi)
        
#print(perimeter(xi,yi))
        
if regular(xi,yi):
    print('El polígono es regular')
else:
    print('El polígono NO es regular')






















