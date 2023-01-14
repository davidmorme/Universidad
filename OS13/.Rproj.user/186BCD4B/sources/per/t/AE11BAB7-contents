library(car)
library(MASS)
library(nortest)

#### ESTIMATE THE DISTRIBUTION ####

FailureTimes_5=read.csv('FailureTimes_5.csv',sep = ',')
data=FailureTimes_5$Heures
hist(data, freq = FALSE,breaks = 9, main='Histogramme de temps de panne')


#### Exponential distribution ####
qqPlot(data, distribution = "exp", rate = 1/mean(data), main='Quantile-Quantile Plot de temps de panne avec distribution Exponentielle')
ks.test(data,"pexp",rate=1/mean(data))

hist(data, freq = FALSE, ylim = c(0,0.0002), main="Temps de panne avec distribution Exponentielle")
curve(dexp(x, rate = 1/mean(data)), from=0, to=max(data), col='blue', add=TRUE)

#### Weibull distribution ####

log.likelihoodWEIBULL= function(tetha){
  beta=tetha[1]
  lambda=tetha[2]
  l=dweibull(data,beta,1/lambda)
  return(-sum(log(l)))
}

SolW=nlminb(c(0.001,2),log.likelihoodWEIBULL, hessian = TRUE)
SolW #Code debe dar 1 o 2
betaHatW=SolW$par[1]
lambdaHatW=SolW$par[2]

qqPlot(data, distribution = "weibull", shape=betaHatW, scale=1/lambdaHatW , main='Quantile-Quantile Plot de temps de panne avec distribution Weibull')
ks.test(data,"pweibull",shape=betaHatW,scale=1/lambdaHatW)

hist(data, freq = FALSE, ylim = c(0,0.0002), main="Temps de panne avec distribution Weibull")
curve(dweibull(x, shape=betaHatW, scale=1/lambdaHatW), from=0, to=max(data), col='blue', add=TRUE)


#### Gamma distribution ####

forma=mean(data)**2/var(data)
escala=mean(data)/forma

qqPlot(data, distribution = "gamma", scale = escala, shape = forma, main='Quantile-Quantile Plot de temps de panne avec distribution Gamma')
ks.test(data,"pgamma",scale = escala, shape = forma)

hist(data, freq = FALSE, ylim = c(0,0.0002), main="Temps de panne avec distribution Gamma")
curve(dgamma(x, scale = escala, shape = forma), from=0, to=max(data), col='blue', add=TRUE)


#### LogNormal distribution ####
solLN=fitdistr(data, "log-normal")

#mlog=log(mean(data)/sqrt(var(data)/mean(data)**2 + 1))
#stdlog=sqrt(log(var(data)/mean(data)**2 + 1))
mlog=solLN$estimate[1]
stdlog=solLN$estimate[2]

qqPlot(data, distribution = "lnorm",meanlog =  mlog, sdlog=stdlog, main='Quantile-Quantile Plot de temps de panne avec distribution Log-Normal')
ks.test(data,"plnorm",meanlog =  mlog, sdlog=stdlog)

hist(data, freq = FALSE, ylim = c(0,0.0002), main="Temps de panne avec distribution Log-Normal")
curve(dlnorm(x, meanlog =  mlog, sdlog=stdlog), from=0, to=max(data), col='blue', add=TRUE)

#### Chi-Squared distribution ####
solLN=fitdistr(data, "chi-squared",start=list(df=3000) )
dfCh=solLN$estimate[1]

qqPlot(data, distribution = "chisq", df=dfCh, main='Quantile-Quantile Plot de temps de panne avec distribution Chi-Squared')
ks.test(data,"pchisq",df =  dfCh)

hist(data, freq = FALSE, ylim = c(0,0.0002), main="Temps de panne avec distribution Chi-Squared")
curve(dchisq(x, df =  dfCh), from=0, to=max(data), col='blue', add=TRUE)

#### Normal distribution ####
qqPlot(data, distribution = "norm", mean=mean(data),sd=sd(data), main='Quantile-Quantile Plot de temps de panne avec distribution Normal')
ks.test(data,"pnorm", mean=mean(data),sd=sd(data))

hist(data, freq = FALSE, ylim = c(0,0.0002), main="Temps de panne avec distribution Normal")
curve(dnorm(x, mean=mean(data),sd=sd(data)), from=0, to=max(data), col='blue', add=TRUE)
