install.packages('pwr')
require('dplyr')
require('ggplot2')
library('readxl')
library('devtools')
Base_aves=read_excel('Base_aves.xlsx')

Base_aves$`Tipo de alimentación`=Base_aves$`Tipo de alimentación` %>%
  factor(labels = unique(Base_aves$`Tipo de alimentación`))

summary(Base_aves)

power.t.test(delta = 0.5, sig.level = 0.02, power = 0.9, type =  "one.sample")

# n=54.81 por lo tanto asumo como 55

N=Base_aves$Ave
set.seed(63)
a=sample(N,55,replace = FALSE)
a

muestra=Base_aves[sort(a),]
View(muestra)
#variables definidas de mi muestra
str(muestra)
summary(muestra)

mean(muestra$Peso)
var(muestra$Peso)
sd(muestra$Peso)

install_github("DFJL/SamplingUtil")
library(SamplingUtil)

set.seed(63)
Nsis=sys.sample(N=nrow(Base_aves),n=55)
muestrasis=Base_aves[sort(Nsis),]
View(muestrasis)

ggplot(data = muestrasis, aes(x = '', y = Peso)) +
  geom_boxplot() +
  xlab('Aves') +
  ylab("Peso") +
  ggtitle("Peso muestra sistématica de Aves") +
  geom_boxplot(col='blue')+
  stat_summary(fun=mean, geom="point", col='red')

library(survey)
library(sampling)

datos=cbind.data.frame(sort(Base_aves$`Tipo de alimentación`),Base_aves$Peso)
datos
names(datos)=c("Tipo de alimentación","Pesp")

s=strata(datos,c("Tipo de alimentación"),size=c(55,55),method="srswor")
muestraEst<-getdata(Base_aves,s)
View(muestraEst)

ggplot(data = muestraEst, aes(x = `Tipo de alimentación`, y = Peso)) +
  geom_boxplot() +
  xlab('Fórmula') +
  ylab("Peso") +
  ggtitle("Peso por Fórmula") +
  geom_boxplot(aes(colour=`Tipo de alimentación`, group=`Tipo de alimentación`))+
  stat_summary(fun=mean, geom="point")

by(muestraEst$Peso, muestraEst$`Tipo de alimentación`, mean)
by(muestraEst$Peso, muestraEst$`Tipo de alimentación`, var)
by(muestraEst$Peso, muestraEst$`Tipo de alimentación`, sd)
