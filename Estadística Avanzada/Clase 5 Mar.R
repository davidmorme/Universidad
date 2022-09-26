## Punto 1 - Caso 2

##Pollo pequeño

pollo_calc<-function(X,media,des_est){
  
  Z<-(X-media)/des_est
  print(round(pnorm(Z),4))
}
pollo_calc(3.5,3.8,0.6)

##Pollo mediano

pollo_calc2<-function(X1,X2,media,des_est){
  
  Z1<-(X1-media)/des_est
  Z2<-(X2-media)/des_est
  print(round(pnorm(Z2)-pnorm(Z1),3))
}
pollo_calc2(3.5,4.9,3.8,0.6)

##Pollo grande

pollo_calc3<-function(X3,media,des_est){
  
  Z3<-(X3-media)/des_est
  print(round(pnorm(Z3,lower.tail = FALSE),4))
}
pollo_calc3(4.9,3.8,0.6)

# Punto 2 - Caso 1

percentil=0.6
media=3.8
des_est=0.6

round(qnorm(percentil,media,des_est),3)

# Punto 3 - Caso 1

exitos<-3
ensayos<-5

round(dbinom(exitos,ensayos,0.3085),4)


## caso 2 (Lo realiza el estudiante)


## Para trabajar en R

# n tamaño de la muestra
# mu y SD es la media y la desviación estándar de la muestra

# rnorm(n,mu,SD)

n<-100
mu<-10
SD<-0.03

muestra<-rnorm(n,mu,SD)

##Histograma

hist(muestra, breaks = 7, freq = F, border = "gray50",main = "Histograma datos generados")
lines(density(muestra))
curve(dnorm(x, mu, SD), lwd = 2, col = "blue", add = T)
legend("topleft", c("curva observada", "curva (normal) teórica"),
       lty = 1, lwd = 2, col = c("black", "blue"), bty = "n",
       cex = 0.8)

#Gráfico de probabilidad normal 

qqnorm(muestra,main = "gráfico de probabilidad normal")
qqline(muestra,col="red")

##Pruebas de normalidad
shapiro.test(muestra)

install.packages("nortest")
library(nortest)
lillie.test(muestra)
