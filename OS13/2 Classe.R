####### Ejemplo Distribución Exponencial #####

data=rexp(10000,rate=2)
#La idea es asumir que la data fue obtenida experimentalmente

#Si sabemos que la distribución es exponencial podemos estimar Landa con
#el método de momentos
Landa_Linda = 1/mean(data)
Landa_Linda

####### Ejemplo Distribución Gamma #####

dataG=rgamma(10000, shape = 2, rate = 4)
#La idea es asumir que la data fue obtenida experimentalmente

#Si sabemos que la distribución es Gamma podemos estimar Alpha Y Beta con
#el método de momentos

n=length(dataG)
varP=var(dataG)*(n-1)/n
alpha=mean(dataG)**2/varP
Beta=mean(dataG)/varP

alpha
Beta

####### Ejemplo Distribución LogNormal #####

dataLN=rlnorm(1000000, meanlog = 2, sdlog = sqrt(5))
#La idea es asumir que la data fue obtenida experimentalmente

#Si sabemos que la distribución es Gamma podemos estimar Alpha Y Beta con
#el método de momentos

n=length(dataLN)
varP=var(dataLN)*(n-1)/n
Sigma=sqrt(log(varP/mean(dataLN)**2+1))
#miu=log(mean(dataLN))-Sigma**2/2
miu=log(mean(dataLN)/sqrt(varP/mean(dataLN)**2+1))

miu
Sigma**2


##### Solve equations ####

install.packages("rootSolve")

library("rootSolve")
#scale = 1/Landa ; shape = Beta
dataW = rweibull(1000,shape = 2, scale = 4)

A=mean(dataW)
n=length(dataW)
B=var(dataW)*(n-1)/n

Equations = function(pars){
  c(F1=gamma(1+1/pars[2])*pars[1]-A , 
    F2= (gamma(1+2/pars[2]) - gamma(1+1/pars[2])**2)*pars[1]**2 - B )
}

ans=multiroot(Equations,start=c(2,2))
ans

Landa=1/ans$root[1]
Beta=ans$root[2]

Landa
Beta
