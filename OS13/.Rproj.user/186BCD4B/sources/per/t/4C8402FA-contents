data=c(0.06,0.8,0.3,0.03,1.2,0.7,0.92,0.41,0.23,0.32,1.1,1.9,0.4,1.31,1.2,0.7,1.4,0.9,0.93,0.27)
data=sort(data)

t=c(0,unique(data))
RHat=rep(0, length(t))

for(i in 1:length(RHat)){
  RHat[i]=sum(data>t[i])/length(data)
}

plot(t,RHat, type = "s")

RHat*20



#### ESTIMATE THE DISTRIBUTION ####


set.seed(2022)
data=rexp(1000,rate = 3)
hist(data, freq = FALSE)



qqplot(qexp(ppoints(500),rate = 3) ,data)
qqline(data, distribution = function(p) qexp(p,rate = 3), col="red")
qqPlot(data, distribution = "exp", rate = 3)
ks.test(data,"pexp",rate=3)

qqplot(qgamma(ppoints(500), rate = 3, shape = 1) ,data)
qqline(data, distribution = function(p) qgamma(p,rate = 3, shape = 1), col="red")
qqPlot(data, distribution = "gamma", rate = 3, shape = 1)
ks.test(data,"pgamma",rate=3, shape = 1)

qqplot(qlnorm(ppoints(500), meanlog =  5, sdlog = sqrt(5)) ,data)
qqline(data, distribution = function(p) qlnorm(p,meanlog =  5, sdlog = sqrt(5)), col="red")
qqPlot(data, distribution = "lnorm", meanlog =  5, sdlog = sqrt(5))
ks.test(data,"plnorm",meanlog =  5, sdlog = sqrt(5))

qqnorm(data)
qqline(data, col="red")


library(MASS)
hist(cats$Hwt, freq = FALSE,breaks = 30)

qqnorm(cats$Hwt)
qqline(cats$Hwt, distribution = qnorm, col="red")


shapiro.test(cats$Hwt)
library(nortest)
lillie.test(cats$Hwt)
ks.test(cats$Hwt,"pnorm", mean=mean(cats$Hwt), sd=sd(cats$Hwt))


dataN=rnorm(100,12,3)
shapiro.test(dataN)
lillie.test(dataN)
ks.test(dataN,"pnorm", mean=mean(dataN), sd=sd(dataN))

library(car)
qqPlot(dataN,distribution = "norm", mean = 12)
