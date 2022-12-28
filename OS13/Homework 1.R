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
