library(unrepx)
library(ggplot2)
library(nortest)
library(lmtest)
library(corrplot)
library(dplyr)
Lanzamientos <- read_excel("C:/Users/DAVID MORA MEZA/Desktop/Ejercicio_Semana_14.xlsx")

A<-factor(Lanzamientos$Altitud)
B<-factor(Lanzamientos$Masa)
Y<-(Lanzamientos$Respuesta)

##ANOVA completo

modelo1<-lm(Respuesta~(Altitud+Masa)^2,data=Lanzamientos)
ANOVA<-aov(modelo1)
summary(modelo1)

##Cálculo de los efectos

efectos<-round(2*modelo1$coefficients,2)
efectos

efectos_absolutos<-sort(abs(efectos),decreasing = TRUE)
efectos_absolutos

#Daniel´s plot
#DanielPlot(modelo1,half = TRUE,main = "Gráfico normal de efectos")

#PSE Lenth
unrepx::PSE(efectos,method = "Lenth")

#Pareto Plot
unrepx::parplot(efectos[-1],absolute = TRUE,horiz = FALSE,method = "Lenth")

##Prueba de efectos
unrepx::eff.test(effects = efectos,method = "Lenth")


ggplot(data = Lanzamientos, aes(x = B, y = Y, color = B)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Masa",y = "Distancia en X")

ggplot(data = Lanzamientos, aes(x = A, y = Y, color = A)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Altitud",y = "Distancia en X")

##Gráfico de interacción

ggplot(data = Lanzamientos, aes(x = B, y = Y, colour = A,
                           group = A)) +
  stat_summary(fun=mean, geom = "point") +
  stat_summary(fun=mean, geom = "line") +
  labs(y  =  "Distancia en X", x="Masa") +
  theme_bw()

# Validación de los supuestos.

#Normalidad
qqnorm(residuals(modelo1))
qqline(residuals(modelo1),col="red")
shapiro.test(residuals(modelo1))
lillie.test(residuals(modelo1))

#Independencia
ggplot(data = modelo1, aes(x = c(1:length(Y)), y = modelo1$residuals)) +
  geom_point() +
  theme_bw()+labs(x = "Observación",y = "Residuo"
  ) 

# Test de Durbin Watson
dwtest(modelo1)  


##Independencia 2

Lanzamientos<- Lanzamientos%>%arrange(Orden)

modelo2<-lm(Respuesta~(Altitud+Masa)^2,data=Lanzamientos)

ggplot(data = modelo2, aes(x = c(1:length(Y)), y = modelo2$residuals)) +
  geom_point() +
  theme_bw()+labs(x = "Observación",y = "Residuo"
  ) 

dwtest(modelo2)

#Quito factor no significativo
Lanzamientos <- read_excel("C:/Users/DAVID MORA MEZA/Desktop/Ejercicio_Semana_14.xlsx")
modelo3=lm(Respuesta~(Masa), data=Lanzamientos)
summary(modelo3)

#Normalidad
qqnorm(residuals(modelo3))
qqline(residuals(modelo3),col="red")
shapiro.test(residuals(modelo3))
lillie.test(residuals(modelo3))

#Independencia
ggplot(data = modelo3, aes(x = c(1:length(Y)), y = modelo3$residuals)) +
  geom_point() +
  theme_bw()+labs(x = "Observación",y = "Residuo"
  ) 

##Independencia 2

Lanzamientos<- Lanzamientos%>%arrange(Orden)

modelo4<-lm(Respuesta~(Masa),data=Lanzamientos)

ggplot(data = modelo4, aes(x = c(1:length(Y)), y = modelo4$residuals)) +
  geom_point() +
  theme_bw()+labs(x = "Observación",y = "Residuo"
  ) 

dwtest(modelo4)

# Test de Durbin Watson
dwtest(modelo3)  

round(predict(modelo3, data.frame(Masa=1), interval = "confidence",level = 0.95),3)
round(predict(modelo3, data.frame(Masa=10), interval = "confidence",level = 0.95),3)
round(predict(modelo3, data.frame(Masa=20), interval = "confidence",level = 0.95),3)
