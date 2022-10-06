##### Exponential distribution #####

#### Complete data ####
lambda=0.001
n=5000

dataC=rexp(n, rate=lambda)
dataC=sort(dataC)

lambdaC=1/mean(dataC)
lambdaC

#### Type I ####

C1=1000
DataT1=dataC[dataC<C1]
r1=length(DataT1)

lambda1=r1/(sum(DataT1)+(n-r1)*C1)
lambda1

#### Type II ####

r2=3000
DataT2=dataC[1:r2]
C2=DataT2[r2]

lambda2=r2/(sum(DataT2)+(n-r2)*C2)
lambda2

##### Weibull distribution #####

#### Complete data ####

data=c(25,58,87,139,28,63,93,157,29,64,111,168,44,64,126,189,57,76,136,212)
n=length(data)

log.likelihood= function(tetha){
  beta=tetha[1]
  lambda=tetha[2]
  l=dweibull(data,beta,1/lambda)
  return(-sum(log(l)))
}

log.likelihood(c(1,2))

Sol=nlm(f = log.likelihood, p = c(1,1))
Sol #Code debe dar 1 o 2
betaHat=Sol$estimate[1]
lambdaHat=Sol$estimate[2]

R=function(t){
  return(pweibull(t, shape = betaHat, scale = 1/lambdaHat,lower.tail = FALSE))
}
R(90)

tt=seq(0, 500, 0.5)
rr=sapply(tt, R)
plot(rr)


#### Type II ####

data=c(0.7,52.7,129.7,187.8,264.4,272.8,304.2,305.1,309.8,310.5)

r=length(data)
n=25

log.likelihood= function(tetha){
  beta=tetha[1]
  lambda=tetha[2]
  l=dweibull(data,beta,1/lambda)
  l[(r+1):n]=pweibull(data[r],beta,1/lambda, lower.tail = FALSE)
  return(-sum(log(l)))
}

Sol=nlm(f = log.likelihood, p = c(1.1,0.005))
Sol #Code debe dar 1 o 2
betaHat=Sol$estimate[1]
lambdaHat=Sol$estimate[2]
