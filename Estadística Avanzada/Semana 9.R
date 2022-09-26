attach(Base_RLM)

#Y<-Base_RLM$Y
#X1<-Base_RLM$X1
#X2<-Base_RLM$X2
#X3<-Base_RLM$X3
#X4<-Base_RLM$X4
#X5<-Base_RLM$X5

n<-length(Y)
k<-5

#Modelo de regresión lineal múltiple
M1<-lm(Y~X1+X2+X3+X4+X5)
summary(M1)

#¿Todas las variables regresoras son significativas de acuerdo con el estadístico t?
#¿El modelo es significativo?

#Calidad de ajuste del modelo

#Calidad del ajuste
#Coeficiente de determinación
R2<-round(summary(M1)$r.squared,3)
R2

#Coeficiente de determinación ajustado
R2adj<-round(summary(M1)$adj.r.squared,3)
R2adj

#Coeficiente de correlación múltiple
Coef_corr_mult<-round(sqrt(R2),3)
Coef_corr_mult

#Error estándar de la estimación
ResStandarError<-round(summary(M1)$sigma,4)
ResStandarError

#Media del error absoluto
mea<-round(sum(abs(residuals(M1)))/n,4)
mea

#Intervalos de confianza
##Intervalo de confianza para Y dado los valores X1 a X5  
round(predict(M1, data.frame(X1=89,X2=7.70,X3=49,X4=1.1,X5=2.6), interval = "confidence",level = 0.95),3)

#Intervalo de confianza para Y futuro dado los valores X1 a X5
round(predict(M1, data.frame(X1=89,X2=7.70,X3=49,X4=1.1,X5=2.6), interval = "prediction",level = 0.95),3)

#Selección del modelo (pasos)
step(M1,direction = "both")

#Nuevo modelo
## De acuerdo con los criterios de información planteé un modelo M2 ¿Es el mismo que M1?
M2=lm(formula = Y ~ X2 + X3 + X4 + X5)
summary(M2)
#Validación de los supuestos M2

#Linealidad
library(corrplot)
matriz_corr<-cor(Base_RLM[-2])
corrplot(matriz_corr,method = "number")

library(corrplot)
matriz_corr<-cor(Base_RLM[,c(-2,-5)])
corrplot(matriz_corr,method = "number")

#Independencia
plot(M2$residuals,main = "Diagrama de dispersión")
library(lmtest)
dwtest(M2,alternative = "two.sided")

#Normalidad
qqnorm(M2$residuals)
qqline(M2$residuals,col="red")
shapiro.test(M2$residuals)
library(nortest)
lillie.test(M2$residuals)

# Homocedasticidad
library(ggplot2)
ggplot(data = M2, aes(M2$fitted.values, M2$residuals)) +
  geom_point() +
  geom_smooth(color = "firebrick", se = FALSE) +
  geom_hline(yintercept = 0) +
  theme_bw()

bptest(M2)

#Colinealidad
matriz_corr<-cor(Base_RLM[,c(-1,-2)])
corrplot(matriz_corr,method = "number")

#Análisis de inflación de la varianza
library(car)
?if(M2)

#Modelo eliminando X4
M3<-lm(Y~X2+X3+X5)
summary(M3)
vif(M3)

#Colinealidad M3
matriz_corr<-cor(Base_RLM[,c(-1,-2,-5)])
corrplot(matriz_corr,method = "number")