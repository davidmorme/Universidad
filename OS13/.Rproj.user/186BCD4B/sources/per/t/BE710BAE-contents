f=function(x) x^2

a=c(-5,0,5)
y=sapply(a,f)
plot(a,y,type = "l")

a=seq(-5,5.1, by = 0.1)
y=sapply(a,f)
plot(a,y,type = "l", col="blue", xlab = "x")
title("X^2   -5<x<5")

h=function(t) exp(sqrt(t))/(2*sqrt(t))
h(3)

a=seq(0.1,5, by = 0.1)
y=sapply(a,h)
plot(a,y,type = "l", col="blue", xlab = "t")
title("Function of h(t)")

##############################################

integrate(f,lower = -5, upper = 5)

R=function(t) exp(-integrate(h,lower = 0, upper = t)$value)
R(3)

y=sapply(a,R)
plot(a,y,type = "l", col="blue", xlab = "t")
title("Function of R(t)")

Ft=function(t) 1-R(t)
Ft(1)

plot(a,sapply(a,R),type = "l", ylim = c(0,1))
lines(a,sapply(a,Ft))

# Calcular la probabilidad de que viva u tiempo dado que ya ha vivido t 

R=function(t) 4/(t+2)**2

m=function(t) integrate(R, lower = t, upper = Inf)$value/R(t)
m(3)

Ft=expression(1-4/(t+2)**2)
Ft1=function(t) 1-4/(t+2)**2

D(Ft,"t")
f=function(t) 4 * (2 * (t + 2))/((t + 2)^2)^2
h=function(t) f(t)/R(t)

a=seq(0,20, by = 0.1)
plot(a,sapply(a,h), type="l",ylim=c(0,1))
title("h(t)")

plot(a,sapply(a,R), type="l",ylim=c(0,1))
title("R(t)")

plot(a,sapply(a,Ft1), type="l",ylim=c(0,1))
title("F(t)")

plot(a,sapply(a,f), type="l",ylim=c(0,1))
title("f(t)")

R1=expression(4/(t+2)**2)


E1 = expression(x**2*y+z)


D(R1,"t")


D(E1,"x")
D(E1,"y")
D(E1,"z")

