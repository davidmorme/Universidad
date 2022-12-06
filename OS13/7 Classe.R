library(car)
library(MASS)
library(nortest)

#### ESTIMATE THE DISTRIBUTION ####

FailureTimes_5=read.csv('FailureTimes_5.csv',sep = ',')
data=FailureTimes_5$Heures
hist(data, freq = FALSE)


#### Exponential distribution ####
qqPlot(data, distribution = "exp", rate = 1/mean(data), main='Quantile-Quantile Plot of data with Exponential distribution')
ks.test(data,"pexp",rate=1/mean(data))

hist(data, freq = FALSE, ylim = c(0,0.0002), main="Data avec exponential distribution")
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

qqPlot(data, distribution = "weibull", shape=betaHatW, scale=1/lambdaHatW , main='Quantile-Quantile Plot of data with Weibull distribution')
ks.test(data,"pweibull",shape=betaHatW,scale=1/lambdaHatW)

hist(data, freq = FALSE, ylim = c(0,0.0002), main="Data avec Weibull distribution")
curve(dweibull(x, shape=betaHatW, scale=1/lambdaHatW), from=0, to=max(data), col='blue', add=TRUE)


#### Gamma distribution ####

forma=mean(data)**2/var(data)
escala=mean(data)/forma

qqPlot(data, distribution = "gamma", scale = escala, shape = forma, main='Quantile-Quantile Plot of data with Gamma distribution')
ks.test(data,"pgamma",scale = escala, shape = forma)

hist(data, freq = FALSE, ylim = c(0,0.0002), main="Data avec Gamma distribution")
curve(dgamma(x, scale = escala, shape = forma), from=0, to=max(data), col='blue', add=TRUE)


#### LogNormal distribution ####
solLN=fitdistr(data, "log-normal")

#mlog=log(mean(data)/sqrt(var(data)/mean(data)**2 + 1))
#stdlog=sqrt(log(var(data)/mean(data)**2 + 1))
mlog=solLN$estimate[1]
stdlog=solLN$estimate[2]

qqPlot(data, distribution = "lnorm",meanlog =  mlog, sdlog=stdlog, main='Quantile-Quantile Plot of data with Log-Normal distribution')
ks.test(data,"plnorm",meanlog =  mlog, sdlog=stdlog)

hist(data, freq = FALSE, ylim = c(0,0.0002), main="Data avec Log-Normal distribution")
curve(dlnorm(x, meanlog =  mlog, sdlog=stdlog), from=0, to=max(data), col='blue', add=TRUE)

#### Chi-Squared distribution ####
solLN=fitdistr(data, "chi-squared",start=list(df=3) )
dfCh=solLN$estimate[1]

qqPlot(data, distribution = "chisq", df=dfCh, main='Quantile-Quantile Plot of data with Chi-Squared distribution')
ks.test(data,"pchisq",df =  dfCh)
