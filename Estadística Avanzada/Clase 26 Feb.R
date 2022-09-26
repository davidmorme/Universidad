require('dplyr')
require('corrplot')

str(base_ratones)

summary(base_ratones)

base_ratones$Sexo=base_ratones$Sexo %>%
  factor(labels = unique(base_ratones$Sexo))

calcula_muestra<-function(alfa,varX,E,N)
{
  z<-round(qnorm(1-(alfa/2)),digits=2)
  numerador <- (z^2)*(N)*(varX)
  denominador <- ((N-1)*(E^2))+((z^2)*(varX))
  
  n<-round(numerador/denominador,digits=0)
  
  print(n)
  
}

calcula_muestra(0.05,19.2,1,200)

#Muestreo aleatorio simple
#Extraer una muestra de 54.
#creamos la semilla y el generador
N<-base_ratones$N
set.seed(63)
a<-sample(N,54,replace = FALSE)
a
#Extraer los elementos del muestreo de la base
muestra<-base_ratones[sort(a),]
View(muestra)
#variables definidas de mi muestra
str(muestra)
summary(muestra)

mean(muestra$Talla_rata)
var(muestra$Talla_rata)
sd(muestra$Talla_rata)



#Muestreo aleatorio estratificado.

install.packages("survey")
install.packages("sampling")
library(survey)
library(sampling)
datos<-cbind.data.frame(sort(base_ratones$Sexo),base_ratones$Talla_rata)
datos
names(datos)=c("Sexo","Talla")
#selección de la muestra
s=strata(datos,c("Sexo"),size=c(54,54),method="srswor")
muestra3<-getdata(base_ratones,s)
View(muestra3)

mean(muestra3$Talla_rata)
sd(muestra3$Talla_rata)
var(muestra3$Talla_rata)

require('ggplot2')
ggplot(data = base_ratones, aes(x = Sexo, y = Talla_rata)) +
  geom_boxplot() +
  xlab('Sexo') +
  ylab("Talla rata") +
  ggtitle("Talla rata por Sexo") +
  geom_boxplot(aes(colour=Sexo, group=Sexo))+
  stat_summary(fun=mean, geom="point")

by(muestra3$Talla_rata, muestra3$Sexo, mean)
by(muestra3$Talla_rata, muestra3$Sexo, var)
by(muestra3$Talla_rata, muestra3$Sexo, sd)

power.t.test(n = 200, delta = 1)
power.t.test(sig.level = 0.05,power = .95,delta = 0.5,type = "one.sample")

