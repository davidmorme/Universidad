##### LogNormal distribution #####

#### Company 1 complete data ####

dataC1=c(170,205,207,240,275,285,324,328,334,352,385,479,500,607,701)

n1=length(dataC1)


log.likelihood= function(tetha){
  miu = tetha[1]
  sigma = tetha[2]
  l=dlnorm(x = dataC1,meanlog = miu, sdlog = sigma)
  return(-sum(log(l)))
}

#nlm(f = log.likelihood, p = c(5,2), hessian = TRUE)

Sol=nlm(f = log.likelihood, p = c(5,2), hessian = TRUE)
Sol #Code debe dar 1 o 2
miuHat=Sol$estimate[1]
sigmaHat=Sol$estimate[2]
miuHat
sigmaHat**2

IHes=solve(Sol$hessian) #Inversa de la matriz hessian

Varmiu=IHes[1,1]
Varsigma=IHes[2,2]

## Confidence interval with 95% of cofidence ##

ConfMiu = miuHat+qnorm(1-0.05/2)*c(-sqrt(Varmiu),sqrt(Varmiu))
ConfSigma= sigmaHat+qnorm(1-0.05/2)*c(-sqrt(Varsigma),sqrt(Varsigma))

ConfMiu
ConfSigma

#### Company 2 partial data ####

dataC2=c(220,264,269,310,408,451,489,537,575,663)

r2=length(dataC2)
C2=701
n2=15

log.likelihood= function(tetha){
  miu = tetha[1]
  sigma = tetha[2]
  l=dlnorm(x = dataC2,meanlog = miu, sdlog = sigma)
  l[(r2+1):n2]=plnorm(C2,meanlog = miu, sdlog = sigma, lower.tail = FALSE)
  return(-sum(log(l)))
}

log.likelihood(c(10,5))

nlm(f = log.likelihood, p = c(10,5), hessian = TRUE)

Sol2=nlm(f = log.likelihood, p = c(10,5), hessian = TRUE)
Sol2 #Code debe dar 1 o 2
miuHat2=Sol2$estimate[1]
sigmaHat2=Sol2$estimate[2]
miuHat2
sigmaHat2**2

IHes2=solve(Sol2$hessian) #Inversa de la matriz hessian

Varmiu2=IHes2[1,1]
Varsigma2=IHes2[2,2]

## Confidence interval with 95% of cofidence ##

ConfMiu2 = miuHat2+qnorm(1-0.05/2)*c(-sqrt(Varmiu2),sqrt(Varmiu2))
ConfSigma2= sigmaHat2+qnorm(1-0.05/2)*c(-sqrt(Varsigma2),sqrt(Varsigma2))

ConfMiu2
ConfSigma2
ConfSigma2**2


#### Comparissons ###
ConfMiu2-ConfMiu
ConfSigma2-ConfSigma


R=function(t){
  return(plnorm(t, miuHat, miuHat,lower.tail = FALSE))
}
R2=function(t){
  return(plnorm(t, miuHat2, miuHat2,lower.tail = FALSE))
}


tt=seq(0, 500, 0.5)
rr=sapply(tt, R)
rr2=sapply(tt, R2)

plot(tt,rr, type = 'l', col='red')
lines(tt,rr2, type = 'l', col='blue')
title('Realibility Function of the 2 companies')
legend("topright", c("Company 1", "Company 2"), lty = 1, col = c('red','blue'))

