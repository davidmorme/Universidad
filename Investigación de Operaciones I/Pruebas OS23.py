# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:49:14 2022

@author: DAVID MORA MEZA
"""
import numpy as np
N=12
p=np.zeros((N,N))
p[N-1,N-1]=1
p[0,0]=0.5
p[0,1]=0.5

for i in range(1,N-1):
    p[i,i-1]=0.5
    p[i,i+1]=0.5
 
p=np.matrix(p)

#%%


p=np.matrix([[0,0,1,0,0,0],[0,0,1,0,0,0],[0.25,0.25,0,0.25,0.25,0],[0,0,0.5,0,0,0.5],[0,0,0.5,0,0,0.5],[0,0,0,0.5,0.5,0]])


#%%

pi=p**1001
pp=p**1000

PT=(pi+pp)/2

