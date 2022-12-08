FailureTimes_5=read.csv('FailureTimes_5.csv',sep = ',')
data=FailureTimes_5$Heures

#Necesario haber confirmado que funcione la función exponencial, si no, cambiar

rateU=1/mean(data)

scenarios=5000
n=100

set.seed(111)
U=rexp(n*scenarios,rate=rateU)
U=matrix(U,nrow = scenarios,ncol = n)


rateD=1/mean(data)/0.5

set.seed(222)
D=rexp(n*scenarios,rate=rateD)
D=matrix(D,nrow = scenarios,ncol = n)

##### Une Seul produit #### 
U1=U[1,]
D1=D[1,]

P1=rep(0, n)
R1=rep(0, n)

P1[1]=U1[1]
R1[1]=P1[1]+D1[1]


for(i in 2:n){
  P1[i]=R1[i-1]+U1[i]
  R1[i]=P1[i]+D1[i]
}

t=seq(0,R1[n],100)

Disp=rep(0, length(t))

Disp[1]=1
for(i in 2:length(Disp)){
  Disp[i]=1-sum(P1<=t[i])+sum(R1<=t[i])
}

plot(t,Disp, type = "s")




##### Generic ####

P1=matrix(0,nrow = scenarios,ncol = n)
R1=matrix(0,nrow = scenarios,ncol = n)

P1[,1]=U[,1]
R1[,1]=P1[,1]+D[,1]


for(i in 2:n){
  P1[,i]=R1[,i-1]+U[,i]
  R1[,i]=P1[,i]+D[,i]
}

t=seq(0,max(R1[,n]),100)

Disp=rep(0, length(t))


for(i in 1:length(Disp)){
  Disp[i]=scenarios-sum(P1<=t[i])+sum(R1<=t[i])
}
Disp=Disp/scenarios
plot(t,Disp, type = 'l' ,xlim=c(0, 5*10e3), ylim=c(0.5,1), main='Disponibilité de produit dans le temps')


(1/rateU)/(1/rateU+1/rateD) #Debe converger a este valor.
