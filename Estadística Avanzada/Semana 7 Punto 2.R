rm(list = ls())

#Muestreo aleatorio simple

N<-length(base_resortes$Resorte_A)
set.seed(6)
a<-sample(N,0.2*N,replace = FALSE)
set.seed(16)
b<-sample(N,0.2*N,replace = FALSE)

#Extraer los elementos del muestreo de la base
muestra_Re<-base_resortes[sort(a),]
muestra_Re$Resorte_B<-base_resortes[sort(b),"Resorte_B"]
View(muestra_Re)

##Histograma
par(mfrow=c(1,1))

hist(muestra_Re$Resorte_A, breaks = 7, freq = F, border = "gray50",main = "Histograma de muestra de Resorte A")
lines(density(muestra_Re$Resorte_A))
curve(dnorm(x, mean(muestra_Re$Resorte_A), sd(muestra_Re$Resorte_A)), lwd = 2, col = "blue", add = T)
legend("topleft", c("curva observada", "curva (normal) teórica"),
       lty = 1, lwd = 2, col = c("black", "blue"), bty = "n",
       cex = 0.8)

hist(muestra_Re$Resorte_B, breaks = 7, freq = F, border = "gray50",main = "Histograma de muestra de Resorte B")
lines(density(muestra_Re$Resorte_B))
curve(dnorm(x, mean(muestra_Re$Resorte_B), sd(muestra_Re$Resorte_B)), lwd = 2, col = "blue", add = T)
legend("topleft", c("curva observada", "curva (normal) teórica"),
       lty = 1, lwd = 2, col = c("black", "blue"), bty = "n",
       cex = 0.8)


#Gráfico de probabilidad normal 

par(mfrow=c(1,2))
qqnorm(muestra_Re$Resorte_A,main = "Gráfico de probabilidad normal del Resorte A")
qqline(muestra_Re$Resorte_A,col="red")

qqnorm(muestra_Re$Resorte_B,main = "Gráfico de probabilidad normal del Resorte B")
qqline(muestra_Re$Resorte_B,col="red")

##Pruebas de normalidad Confianza 98%

shapiro.test(muestra_Re$Resorte_A) #No rechaza que sea normal
shapiro.test(muestra_Re$Resorte_B) #Rechaza que sea normal

install.packages("nortest")
library(nortest)
lillie.test(muestra_Re$Resorte_A) #No rechaza que sea normal
lillie.test(muestra_Re$Resorte_B) #No rechaza que sea normal

ad.test(muestra_Re$Resorte_A)     #No rechaza que sea normal
ad.test(muestra_Re$Resorte_B)     #Rechaza que sea normal

#Estimador puntual de la media
xbarRA<-round(mean(muestra_Re$Resorte_A),2)
xbarRB<-round(mean(muestra_Re$Resorte_B),2)

#La raíz del estimador puntual de la varianza no es necesariamente un factor insesgado. Tiene cierto sesgo.
#Estimador puntual de la desviación estándar (Tiene cierto sesgo)
SRA<-round(sd(muestra_Re$Resorte_A),2)
SRB<-round(sd(muestra_Re$Resorte_B),2)
c(xbarRA,SRA)
c(xbarRB,SRB)

## Razón de varianza de los Resortes
var.test(muestra_Re$Resorte_A,muestra_Re$Resorte_B)
#Varianzas desconocidas diferentes, siendo la A significativamente mayor que la B

#El resorte B está más cercano a la especificación

## Diferencia de medias
t.test(x=(muestra_Re$Resorte_A-muestra_Re$Resorte_B),mu=0,conf.level = 0.98, var.equal = FALSE)
t.test(x=muestra_Re$Resorte_A, y=muestra_Re$Resorte_B,conf.level = 0.98, var.equal = FALSE)
#No hay una diferencia significativa en la diferencia de medias

t.test(x=muestra_Re$Resorte_A,mu=25,conf.level = 0.98)
t.test(x=muestra_Re$Resorte_B,mu=25,conf.level = 0.98)

#No se descarta que sumedia poblacional sea igual a 25

#Sí le recomendaría cambiar porque a pesar de que la media de la elongación
#de los resortes no es significativa, sí hay un cambio grande en la varianza 
#del mismo, y así se mejora la calidad

## Histogramas 

hist(muestra_Re$Resorte_A, breaks = 7, freq = F, main = "Histograma de muestras de Resortes A y B", ylim = c(0,0.4))
hist(muestra_Re$Resorte_B, add= TRUE, breaks = 7, freq = F, col = rgb(1, 0, 0, alpha = 0.5))

lines(density(muestra_Re$Resorte_A), col='blue')
lines(density(muestra_Re$Resorte_B), col='green')

legend("topright", c("curva observada Resorte A", "curva observada Resorte B"),
       lty = 1, lwd = 2, col = c("blue", "green"), bty = "n",
       cex = 0.8)

hist(muestra_Re$Resorte_A, breaks = 7, freq = F, main = "Histograma de muestras de Resortes A y B", ylim = c(0,0.4))
hist(muestra_Re$Resorte_B, add= TRUE, breaks = 7, freq = F, col = rgb(1, 0, 0, alpha = 0.5))

curve(dnorm(x, mean(muestra_Re$Resorte_A), sd(muestra_Re$Resorte_A)), lwd = 2, col = "blue", add = T)
curve(dnorm(x, mean(muestra_Re$Resorte_B), sd(muestra_Re$Resorte_B)), lwd = 2, col = "green", add = T)

abline(v=25,  col="cyan")
abline(v=c(20,30),  col="magenta")

legend("topright", c("curva (normal) teórica Resorte A", "curva (normal) teórica Resorte B"),
       lty = 1, lwd = 2, col = c("blue", "green"), bty = "n",
       cex = 0.8)

## Diagrama de cajas y bigotes

par(mfrow=c(1,1))
boxplot(muestra_Re,main="Boxplot Resorte A y B", col = c("green", "cyan"))
abline(h=25,  col="blue")
abline(h=c(20,30),  col="red")
