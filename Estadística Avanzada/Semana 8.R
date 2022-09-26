rm(list = ls())

#Planteamiento del modelo de regresión
#Datos

X<-c(12,4,18,24,28,26,8,16,22,10,30,6,20,14)
Y<-c(144,134,157,167,174,171,142,156,166,149,183,145,168,160)

#Modelo de regresión

regression_model<-summary(lm(Y~X))
## Salidas del planteamiento del modelo de regresión

regression_model


##Gráfico de dispersión

require("ggplot2")
ggplot(lm(X~Y), mapping = aes(x = X, y = Y)) +
  geom_point(color = "firebrick", size = 2) +
  geom_smooth(method = "lm", se = TRUE, color = "BLACK",level=0.95) +
  labs(title = "Resistencia ~ Porcentaje de fibra", x = "Porcentaje de fibra", y = "Resistencia") +
  theme_bw() + theme(plot.title = element_text(hjust = 0.5))


## Anova modelo de regresión

ANOVA<-anova(lm(Y~X))
ANOVA

#Calidad del ajuste modelo de regresión

#Coeficiente de determinación ajustado
regression_model$adj.r.squared

#Coeficiente de correlación
cor(X,Y)

#Error estándar de la estimación
sqrt(ANOVA$`Mean Sq`[2])
regression_model$sigma

#Media del error absoluto
mea<-round(mean(abs(residuals(regression_model))),4)
mea

#validación supuestos del modelo forma gráfica
par(mfrow=c(2,2))
plot(lm(Y~X))

#Linealidad - Se comprueba rechazando la hipótesis b_1=0
par(mfrow=c(1,1))
#Prueba de independencia
install.packages("lmtest")
library(lmtest)
dwtest(regression_model)
plot(residuals(regression_model))

#Normalidad de los residuos
qqnorm(residuals(regression_model))
qqline(residuals(regression_model),col="red")
shapiro.test(residuals(regression_model))
library(nortest)
lillie.test(residuals(regression_model))

#Homocedasticidad - varianza constante
bptest(regression_model)

#Intervalo de confianza resistencia PROMEDIO que esperarímos utilizando 12 en (porcentaje de fibra). 
predict(lm(Y~X), data.frame(X=12), interval = "confidence")

#Intervalo de confianza resistencia que esperarímos utilizando de 12 (porcentaje de fibra). Observación futura
predict(lm(Y~X), data.frame(X=12), interval = "prediction")
