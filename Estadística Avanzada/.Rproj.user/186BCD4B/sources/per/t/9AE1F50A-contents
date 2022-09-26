library(readr)
Base_arcilla <- read_table2("~/9 Semestre/Estadística Avanzada/Semana 12/Base_arcilla.txt", 
                            col_types = cols(A = col_character(), 
                                             B = col_character()))
View(Base_arcilla)

library(ggplot2)
library(nortest)
library(lmtest)
library(DescTools)
library(dplyr)

summary(Base_arcilla)

Base_arcilla$A<-factor(Base_arcilla$A)
Base_arcilla$B<-factor(Base_arcilla$B)
#Y<-Base_arcilla$Y

attach(Base_arcilla)

#Diagrama de cajas

ggplot(data = Base_arcilla, aes(x = A, y = Y, color = A)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Temperatura",y = "Color aceite")+scale_y_continuous(limit = c(3,6))


ggplot(data = Base_arcilla, aes(x = B, y = Y, color = B)) +
  geom_boxplot() +
  theme_bw()+labs(x = "% Arcilla",y = "Color aceite")+scale_y_continuous(limit = c(3,6))


#Modelo tipo 1
modelo1<-lm(Y~A+B+(A*B))
#Anova modelo
summary(aov(modelo1))
summary(modelo1)


#El modelo 1 también lo podemos escribir de la siguiente manera:
#modelo1<-lm(Y~A*B) o modelo1<-lm(Y~(A+B)^2)

#Gráfico de interacción
ggplot(data = Base_arcilla, aes(x = B, y = Y, colour = A,
                                group = A)) +
  stat_summary(fun = mean, geom = "point") +
  stat_summary(fun = mean, geom = "line") +
  labs(y  =  "Color aceite", x="% arcilla") +
  theme_bw()

#Validación de los supuestos del modelo

#Normalidad de los residuos
qqnorm(residuals(modelo1))
qqline(residuals(modelo1),col="red")
shapiro.test(residuals(modelo1))
lillie.test(residuals(modelo1))

#Varianza constante
#Test Breush Pagan
bptest(modelo1)

#Independencia
ggplot(data = modelo1, aes(x = c(1:length(Y)), y = modelo1$residuals)) +
  geom_line() +
  theme_bw()+labs(x = "Observaciones",y = "Residuo")

# Test de Durbin Watson M1
dwtest(modelo1)


NDF=filter(Base_arcilla,B!=1.1)
View(NDF)

modelo2=lm(Y~A*B,data=NDF)
summary.aov(modelo2)
summary(modelo2)

oneway.test(Y~A)
oneway.test(Y~B)
