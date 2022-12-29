#### Point 2 #####
Rh=0.7356
n=20
z=qnorm(1-0.025)
Rh-z*sqrt(Rh*(1-Rh)/n)
Rh+z*sqrt(Rh*(1-Rh)/n)

#### Point 3 #####

data3=c(1.11,1.25,1.37,1.49,1.53,1.71,1.89,2.03,2.31,2.50)
min(data3)
1/(mean(data3)-min(data3))

#### Point 4 #####
pi=11/20
n=20
z=qnorm(1-0.025)
pi-z*sqrt(pi*(1-pi)/n)
pi+z*sqrt(pi*(1-pi)/n)

qbeta(0.025,16,14)
qbeta(0.975,16,14)

pis=seq(0.005,1,0.001)

com=factorial(20) / (factorial(11) * (factorial(9)))

log_likelihood_Heads=function(pi){
  log(com)+11*log(pi)+9*log(1-pi)
}

log_likelihood_Heads(0)

lLHeads=sapply(pis,log_likelihood_Heads)

plot(pis,lLHeads,'l', main='log-likelihood function',xlab = 'Pi',ylab = 'log-likelihood')


priori=dbeta(pis,5,5)

plot(pis,priori,'l', main='Prior function',xlab = 'Pi',ylab = 'Density')


post=dbeta(pis,16,14)

plot(pis,post,'l', main='Prosterior function',xlab = 'Pi',ylab = 'Density')


plot(pis,post,'l', main='Prior and Posterior functions',xlab = 'Pi',ylab = 'Density', col='red')
lines(pis,priori,'l', col='blue')

legend("topright", legend = c('Prior',"Posterior"),
       lwd = 3, col = c('blue',"red"))


postU=dbeta(pis,12,10)

plot(pis,post,'l', main='Posterior functions',xlab = 'Pi',ylab = 'Density', col='blue')
lines(pis,postU,'l', col='red')

legend("topleft", legend = c('Posterior with information',"Posterior with Uniform"),
       lwd = 3, col = c('blue',"red"), bty = 'n')


plot(pis,post/postU,'l', main="Bayes' factor Posterior functions",xlab = 'Pi',ylab = 'Ratio')


#### Point 5 #####

convexR=function(t){
  1/(t+1)**2
}

ts=seq(0,10,0.1)

plot(ts,sapply(ts,convexR),'l', main="Reliability function of convex example",xlab = 't',ylab = 'R(t)')

convexh=function(t){
  1/(t+1)
}

plot(ts,sapply(ts,convexh),'l', main="Hazard function of convex example",xlab = 't',ylab = 'h(t)')


concaveR=function(t){
  -4/9*t**2+1
}

ts=seq(0,1.5,0.01)

plot(ts,sapply(ts,concaveR),'l', main="Reliability function of concave example",xlab = 't',ylab = 'R(t)')

concaveh=function(t){
  -8*t/(4*t**2-9)
}

plot(ts,sapply(ts,concaveh),'l', main="Hazard function of concave example",xlab = 't',ylab = 'h(t)')


#### Point 6 #####

data1=c(1770,2448,3230,3445)
data2=c(1090,1907,2147,2645,2903)
data3=c(630,848,1121,1307,1321,1357,1984,2331)

S0=50
S1=80
S2=100
S3=120
n1=12
n2=10
n3=8
r1=length(data1)
r2=length(data2)
C1=3500
C2=3000

log.likelihood= function(theta){
  b0=theta[1]
  b1=theta[2]
  l=r1*(b0+b1*S1)-exp(b0+b1*S1)*sum(data1)-exp(b0+b1*S1)*(n1-r1)*C1 + r2*(b0+b1*S2)-exp(b0+b1*S2)*sum(data2)-exp(b0+b1*S2)*(n2-r2)*C2 + n3*(b0+b1*S3)-exp(b0+b1*S3)*sum(data3)
  return(-l)
}

log.likelihood(c(-0.01,-0.1))
Sol=nlm(log.likelihood,c(0.5,-0.001), hessian = TRUE)
Sol #Code debe dar 1 o 2
beta0Hat=Sol$estimate[1]
beta1Hat=Sol$estimate[2]
log.likelihood(c(beta0Hat,beta1Hat))

exp(beta0Hat+beta1Hat*S0)
1/exp(beta0Hat+beta1Hat*S0)

1500*exp(beta0Hat+beta1Hat*S2)/exp(beta0Hat+beta1Hat*S0)
