#Ejercicio tipo parcial

#Experimento factorial
#Dos niveles (Factores) K= 3
#n runs

library(FrF2)
library(ggplot2)
library(nortest)
library(lmtest)
library(rsm)


Y<-c(29, 20, 22, 16, 43, 51, 39, 49,
     24, 21, 25, 19, 45, 49, 40, 48,
     30, 24, 20, 18, 40, 52, 37, 50)

dis_fac<-FrF2(nruns = 8,nfactors = 3,
              factor.names = list(A=c(-1,1),B=c(-1,1),C=c(-1,1))
              ,replications = 3,randomize = FALSE)

dis_fac<-add.response(design = dis_fac,response = Y)
dis_fac

modelo1<-lm(Y~(A+B+C)^3,data = dis_fac)
summary(modelo1)

#Si P es menor que alpha = Hay influencia significativa

#Hay influencia significativa con los factores: A, B, C y con las iinteracciones: AC

?step

step(modelo1)

#El AIC para el modelo Y ~ A + B + C + A:C es menor comparado con los demas modelos propuestos

#Se crea un segundo modelo con los factores e interacciones significativas

##Gráfico de interacción

ggplot(data = dis_fac, aes(x = A, y = Y, colour = C,
                           group = C)) +
  stat_summary(fun=mean, geom = "point") +
  stat_summary(fun=mean, geom = "line") +
  labs(y = "efecto contaminación", x="Extracto") +
  theme_bw()+ facet_wrap(~B, scales = "fixed")


modelo2<-lm(Y~A+B+C+A:C, data = dis_fac)
#modelo2<-rsm(Y~FO(A,B,C), data = dis_fac)
summary(modelo2)

## Validacion de supuestos

## Normalidad
qqnorm(residuals(modelo2))
qqline(residuals(modelo2),col="red")
shapiro.test(residuals(modelo2))
lillie.test(residuals(modelo2))

# Si p es menor que alpha, se acepta H0 = es normal

## Independencia

ggplot(data = modelo2, aes(x = c(1:length(Y)), y = modelo2$residuals)) +
  geom_point() +
  labs(x = "Observación",y = "Residuo")+
  theme_bw()

# Test de Durbin Watson
dwtest(modelo2)

# si p es mayor que alpha, se acpeta H0 = hay independencia

## Varianza constante

#Test Breush Pagan
bptest(modelo2)
modelo2
##Respuesta mínima.
min(round(predict(modelo2,level = 0.95),3))

#round(predict(modelo2, data.frame(A=1,B=1,C=-1), interval = "confidence",level = 0.95),3)
#modelo2
