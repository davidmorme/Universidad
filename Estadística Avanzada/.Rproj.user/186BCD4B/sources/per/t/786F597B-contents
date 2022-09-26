rm(list = ls())
library(readr)
Base_rendimientoQ <- read_table2("~/9 Semestre/Estadística Avanzada/Semana 12/Base_rendimientoQ.txt")
library(ggplot2)
install.packages("rsm")
library(rsm)
library(nortest)
library(lmtest)
library(corrplot)


#Factores
Reactivo<-factor(Base_rendimientoQ$A)
Catalizador<-factor(Base_rendimientoQ$B)

#Variable de respuesta
Rendimiento<-Base_rendimientoQ$Y

#Modelo
modelo1<-lm(Rendimiento~Reactivo*Catalizador)
#Anova modelo
summary(aov(modelo1)) #Se logra evidenciar que la interacción no es significativa
summary(modelo1)

#Gráfico interacción
ggplot(data = Base_rendimientoQ, aes(x = Reactivo, y = Rendimiento, colour = Catalizador,
                                     group = Catalizador)) +
  stat_summary(fun = mean, geom = "point") +
  stat_summary(fun = mean, geom = "line") +
  labs(y  =  "Rendimiento", x="Reactivo") +
  theme_bw()

#Datos codificados
Y1<-Base_rendimientoQ$Y
X1<-Base_rendimientoQ$X1
X2<-Base_rendimientoQ$X2

modelo2<-rsm(Y1~FO(X1,X2),data = Base_rendimientoQ)
summary(modelo2)

#Superficie de respuesta

persp(modelo2, X2 ~ X1, 
      zlab = "Rendimiento", 
      zlim = c(18,35), contours = list(z = "bottom", col = "colors"), # posicion y color
      at = c(summary(modelo2$canonical$xs)),
      theta = 320, # coordenadas graficas
      phi = 30)

contour(modelo2, ~ X1 + X2, image = TRUE)

modelo3<-lm(Y1~FO(X1,X2)+TWI(X1,X2),data = Base_rendimientoQ)
summary(modelo3)

AIC(modelo2,modelo3)

# Validación de los supuestos.

#Linealidad

#Todos los betas son significativos.

#Normalidad
qqnorm(residuals(modelo2))
qqline(residuals(modelo2),col="red")
shapiro.test(residuals(modelo2))
lillie.test(residuals(modelo2))

#Independencia
ggplot(data = modelo2, aes(x = c(1:length(Y1)), y = modelo2$residuals)) +
  geom_point() +
  theme_bw()+labs(x = "Observación",y = "Residuo")

# Test de Durbin Watson
dwtest(modelo2)


#Varianza constante
#Test Breush Pagan
bptest(modelo2)

#Colinealidad
matriz_corr<-cor(Base_rendimientoQ[,c(-3,-4,-5)])
corrplot(matriz_corr,method = "number")

matriz_corr<-cor(Base_rendimientoQ[,c(-1,-2,-5)])
corrplot(matriz_corr,method = "number")


#Intervalos de confianza

##Intervalo de confianza para Y dado los valores X1 y X2 (Reactivo bajo - Catalizador alto)  
round(predict(modelo2, data.frame(X1=-1,X2=1), interval = "confidence",level = 0.95),3)

#Intervalo de confianza para Y futuro dado los valores X1 y X2
round(predict(modelo2, data.frame(X1=-1,X2=1), interval = "prediction",level = 0.95),3)


#Intervalos de confianza
##Intervalo de confianza para Y dado los valores X1 a X2 (Reactivo alto - Catalizador bajo)  
round(predict(modelo2, data.frame(X1=1,X2=-1), interval = "confidence",level = 0.95),3)

##Intervalo de confianza para Y futuro dado los valores X1 a X2 (Reactivo alto - Catalizador bajo)  
round(predict(modelo2, data.frame(X1=1,X2=-1), interval = "prediction",level = 0.95),3)
