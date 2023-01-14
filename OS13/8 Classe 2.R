FailureTimes_5=read.csv('FailureTimes_5.csv',sep = ',')
data=FailureTimes_5$Heures

#Necesario haber confirmado que funcione la función exponencial, si no, cambiar

rateU=1/mean(data)

scenarios=5000
n=100

set.seed(111)
U=rexp(n*scenarios, rate=rateU)
U=matrix(U,nrow = n, ncol = scenarios)


rateD=1/mean(data)/0.2

set.seed(222)
D=rexp(n*scenarios, rate=rateD)
D=matrix(D,nrow = n, ncol = scenarios)


##### Une Seul produit #### 
U1=U[,1]
D1=D[,1]


r1=U1+D1
R1=cumsum(r1)
P1=R1-D1

t=seq(0,R1[n],100)

Disp=rep(0, length(t))

works=function(t){
  sum(P1<=t)==sum(R1<=t)
}

Disp=sapply(t,works)

plot(t,Disp, type = "s", main="Disponibilité du premier produit dans le temps")

##### Generic ####

r=U+D
R=apply(r, 2, cumsum)
P=R-D

t=seq(0,max(R[n,]),100)

reparation=function(t){ #Products in reparation
  sum(P<=t)-sum(R<=t)
}
reparation(10000)

Disp=(scenarios-sapply(t,reparation))/scenarios

plot(t,Disp, type = 'l' ,xlim=c(0, 5*10e3), ylim=c(0.5,1), main='Disponibilité de produit dans le temps',ylab='A(t)')


(1/rateU)/(1/rateU+1/rateD) #Debe converger a este valor.

A=function(t){ #Products in reparation
  1/(rateU+rateD)*(rateD+rateU*exp(-(rateD+rateU)*t))
}
As=sapply(t,A)

plot(t,Disp, type = 'l' ,xlim=c(0, 5*10e3), ylim=c(0.7,1),col='blue', main='Disponibilité de produit dans le temps',ylab='A(t)')
lines(t,As, type = 'l' , col='red', label='Valeur théorique')

legend("topright", legend = c('Simulation Montecarlo',"Valeur théorique"),
       lwd = 2, col = c('blue',"red"), bty = 'n')

mean(abs(Disp[0:5000]-As[0:5000])/As[0:5000])
