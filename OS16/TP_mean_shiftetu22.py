"""
@author: gralle
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import des données et tracé
Xu = np.genfromtxt('data/data_meanshift2_Xu.csv',delimiter=';')
nu = Xu.shape[0]
plt.figure(figsize=(7,5))
plt.plot(Xu[:,0],Xu[:,1],'.b', markersize=3)
plt.title('Data to classify')
plt.savefig('Data_classify.png', dpi=100, bbox_inches='tight', pad_inches=0.1)

'''===================================='''
# fonction pour déterminer le centre de gravite d'une ensemble de points 
# donné par Xu, centré en pt pour un noyau exponentiel de paramètre sig
def centre_gravite (Xu,pt,sig):
    dist = (pt - Xu)
    dist = dist[:,0]**2 + dist[:,1]**2 
    exp_mat = np.exp(-0.5*(dist/(sig**2))) 
    sumexp = np.sum(exp_mat,0)
    num_1 = np.sum(Xu[:,0] * exp_mat)/ sumexp
    num_2 = np.sum(Xu[:,1] * exp_mat)/ sumexp   
    cg = np.array([num_1 , num_2])
    return (cg)
#%%
'''=============== meanshift pour 1 seul point ====================='''
numero_pt = 19 #95
point = Xu[numero_pt,:]
suitepoints = np.array ([point])

# En partant de "point", Recherche du chemin (suite de points) 
# vers son point stationnaire
# la suite de points  est stocké dans "suitepoints"
# à chaque itération le nouveau "point" est calculé et ajouté au vecteur "suitepoints"
point = Xu[numero_pt,:]
suitepoints = np.array ([point])
epsilon=10e-5
sigma=1
bol=True
while bol:
    pointN=centre_gravite (Xu,point,sigma)
    if np.sqrt(sum((point-pointN)**2)) < epsilon: bol=False
    point=pointN
    suitepoints = np.concatenate ((suitepoints,[point]))
    
'''============Tracé d'un chemin en partant d'un point '========================'''
# tracé de toutes les données Xu, du point de départ, de la suite de points 
#  et le point stationnaire
plt.figure()      
plt.plot(Xu[:,0],Xu[:,1],'.b', markersize=3)
plt.plot(suitepoints[:,0],suitepoints[:,1],'.g', markersize=4)
plt.plot(suitepoints[0,0],suitepoints[0,1],'*k', markersize=4)
plt.plot(suitepoints[-1,0],suitepoints[-1,1],'*r', markersize=4)



#%%

numero_pt = 95 #95 #19



fig, ax = plt.subplots(4,2,figsize=(14,15))  

for i, epsilon in enumerate([10e-10,10e-1]):
    for j, sigma in  enumerate([ 0.1, 0.5, 1, 5]):
        point = Xu[numero_pt,:]
        suitepoints = np.array ([point])
    
        bol=True
        while bol:
            pointN=centre_gravite (Xu,point,sigma)
            if np.sqrt(sum((point-pointN)**2)) < epsilon: bol=False
            point=pointN
            suitepoints = np.concatenate ((suitepoints,[point]))

            
        ax[j,i].plot(Xu[:,0],Xu[:,1],marker='.',linestyle='None',color='royalblue', markersize=10)
        ax[j,i].plot(suitepoints[:,0],suitepoints[:,1],'.g', markersize=11)
        ax[j,i].plot(suitepoints[0,0],suitepoints[0,1],'*k', markersize=11)
        ax[j,i].plot(suitepoints[-1,0],suitepoints[-1,1],'*r', markersize=11)
        ax[j,i].set_title(f'$\sigma$ = {sigma} et $\epsilon$ = {epsilon}')

fig.suptitle(f'Mean-shift de point {numero_pt}', y=0.92, size=20)
fig.savefig(f'Mean-shift de point {numero_pt}.png',bbox_inches='tight', pad_inches=0.1, dpi=300)
#%%
'''=============== meanshift pour un ensemble de points ====================='''
# Recherche du point stationnaire pour chaque élément de l'ensemble Xu
# les points stationnaires seront stockés dans le vecteur destination


epsilon=10e-10
sigma=1

destination=np.zeros((len(Xu),2))

for i in  range(0,len(Xu)):
    point = Xu[i,:]
    suitepoints = np.array ([point]) 
    while True:
        pointN=centre_gravite (Xu,point,sigma)
        if np.sqrt(sum((point-pointN)**2)) < epsilon: break
        point=pointN
    
    destination[i]=point


#%%
'''================ classification ===================='''
# classification à partir de la destination de chaque valeur de l'ensemble Xu
rho = 0.5 
K = 1
classe = Xu[:,0]*0 
classe[0]= 0 +1
centres = np.array ([destination[0,: ]])
for i in range(1,nu):
    point = destination[i,: ]
    dist = (point - centres)
    dist = dist[:,0]**2 + dist[:,1]**2 
    distmin = np.min(dist)
    if distmin > rho:
        centres = np.concatenate ((centres,[point]))
        K = K+1
        classe[i]= K
    else:  
        classe[i] = np.argmin(dist)+1

# tracé des points avec leur classe 
fig, ax = plt.subplots(figsize=(7,5)) 
colors = ['^r', '*b', 'Dg','*g', '*y', '*m']
for i in range(K):
    index = classe==i+1
    ax.plot(Xu[index,0], Xu[index,1], colors[i%6],markersize=6)
    
ax.plot(centres[:,0], centres[:,1],marker='.', color='cyan',markersize=15, linestyle='')

fig.suptitle('Données classées avec leurs centres de gravité', y=0.94)
fig.savefig('Données_classées.png',bbox_inches='tight', pad_inches=0.1, dpi=300)

#%%
fig, ax = plt.subplots(2,2,figsize=(10,10))  

#sigmas=[ 0.1, 0.5, 1, 5]
sigmas=[ 0.5, 1, 2, 5]



epsilon=10e-10
rho = 0.5 

means=[]
mins=[]
maxs=[]
Qs=[]

for j, sigma in  enumerate(sigmas):
    
    destination=np.zeros((len(Xu),2))

    for i in  range(0,len(Xu)):
        point = Xu[i,:]
        suitepoints = np.array ([point]) 
        while True:
            pointN=centre_gravite (Xu,point,sigma)
            if np.sqrt(sum((point-pointN)**2)) < epsilon: break
            point=pointN
        
        destination[i]=point
    
    K = 1
    classe = Xu[:,0]*0 
    classe[0]= 0 +1
    centres = np.array ([destination[0,: ]])
    for i in range(1,nu):
        point = destination[i,: ]
        dist = (point - centres)
        dist = dist[:,0]**2 + dist[:,1]**2 
        distmin = np.min(dist)
        if distmin > rho:
            centres = np.concatenate ((centres,[point]))
            K = K+1
            classe[i]= K
        else:  
            classe[i] = np.argmin(dist)+1
    c = np.unique(classe, return_counts=True)[1]
    means.append(np.mean(c))
    mins.append(np.min(c))
    maxs.append(np.max(c))
    Qs.append(len(c))
    # tracé des points avec leur classe 
    colors = ['^r', '*b', 'Dg','*g', '*y', '*m']
    for i in range(K):
        index = classe==i+1
        ax[j//2,j%2].plot(Xu[index,0], Xu[index,1], colors[i%6],markersize=6)
    
    
    ax[j//2,j%2].plot(centres[:,0], centres[:,1],marker='.', color='cyan',markersize=15, linestyle='', label='Centres de gravité')
    ax[j//2,j%2].legend()
    ax[j//2,j%2].set_title(f'$\sigma$ = {sigma}')
    
fig.suptitle("Mean-shift pour l'ensemble de points", y=0.93, size=15)
fig.savefig('Données2_classées avec variation de parametres.png',bbox_inches='tight', pad_inches=0.1, dpi=300)

#%%

df2=pd.DataFrame({'Sigma':sigmas,'Nombre de clusters':Qs,'Nombre moyen de points par cluster':means,
                 'Nombre minimum de points dans un cluster':mins,'Nombre maximum de points dans un cluster':maxs})
#df1.to_excel('Summary.xlsx', sheet_name='Données 2', index=False)
#%%
with pd.ExcelWriter('Summary.xlsx') as writer:  
    df1.to_excel(writer, sheet_name='Données 1', index=False)
    df2.to_excel(writer, sheet_name='Données 2', index=False)

