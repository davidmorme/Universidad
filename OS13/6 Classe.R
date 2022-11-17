##### Acelerating Life Testing with Weibull distribution #####

#### Tempreature 150 ˚C (Complete data) ####

data3=c(420,650,703,838,1086,1125,1378,1673,1896,2037)
n3=length(data3)

log.likelihood3= function(tetha){
  beta=tetha[1]
  lambda=tetha[2]
  l=dweibull(data3,beta,1/lambda)
  return(-sum(log(l)))
}

Sol3=nlminb(c(0.0001,2),log.likelihood3, hessian = TRUE)
Sol3 #Code debe dar 1 o 2
betaHat3=Sol3$par[1]
lambdaHat3=Sol3$par[2]

#### Tempreature 120 ˚C (Censored data) ####

data2=c(1121,1572,2329,2573,2702,3702,4277)

r2=length(data2)
C2=4500
n2=8

log.likelihood2= function(tetha){
  beta=tetha[1]
  lambda=tetha[2]
  l=dweibull(data2,beta,1/lambda)
  l[(r2+1):n2]=pweibull(C2,beta,1/lambda, lower.tail = FALSE)
  return(-sum(log(l)))
}

Sol2=nlminb(c(2,0.0001),log.likelihood2, hessian = TRUE)
Sol2 #Code debe dar 1 o 2
betaHat2=Sol2$par[1]
lambdaHat2=Sol2$par[2]

#### Tempreature 100 ˚C (Censored data) ####

data1=c(1638, 1944, 2764, 2846, 3546, 4803, 5139, 5446)

r1=length(data1)
C1=5500
n1=8

log.likelihood1= function(tetha){
  beta=tetha[1]
  lambda=tetha[2]
  l=dweibull(data1,beta,1/lambda)
  l[(r1+1):n1]=pweibull(C1,beta,1/lambda, lower.tail = FALSE)
  return(-sum(log(l)))
}

Sol1=nlminb(c(2,0.0001),log.likelihood1, hessian = TRUE)
Sol1 #Code debe dar 1 o 2
betaHat1=Sol1$par[1]
lambdaHat1=Sol1$par[2]



##### Acelerating life Testing with Exponential distribution #### 

data1=c(1770,2448,3230,3445,3538,5809,6590,6744)
data2=c(1090,1907,2147,2645,2903,3357,4135,4381)
data3=c(630,848,1121,1307,1321,1357,1984,2331)

S0=50
S1=80
S2=100
S3=120
n1=length(data1)
n2=length(data2)
n3=length(data3)

log.likelihood= function(theta){
  b0=theta[1]
  b1=theta[2]
  l=n1*(b0+b1*S1)-exp(b0+b1*S1)*sum(data1)+n2*(b0+b1*S2)-exp(b0+b1*S2)*sum(data2)+n3*(b0+b1*S3)-exp(b0+b1*S3)*sum(data3)
  return(-l)
}

log.likelihood(c(1,1))
Sol=nlm(log.likelihood,c(0.5,0.05), hessian = TRUE)
Sol #Code debe dar 1 o 2
betaHat=Sol$par[1]
lambdaHat=Sol$par[2]