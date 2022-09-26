install.packages("FrF2")
install.packages("unrepx")
library(FrF2)
library(unrepx)
library(ggplot2)
library(nortest)
library(lmtest)
library(corrplot)
library(dplyr)

A<-factor(Base_Isatina$A)
B<-factor(Base_Isatina$B)
C<-factor(Base_Isatina$C)
D<-factor(Base_Isatina$D)
Y<-(Base_Isatina$Y)

##Matriz de diseño

dis_fac<-FrF2(nruns = 16,nfactors = 4,
              factor.names = list(A=c(-1,1),B=c(-1,1),C=c(-1,1),D=c(-1,1))
              ,replications = 1,randomize = FALSE)

dis_fac<-add.response(design = dis_fac,response = Y)
dis_fac

##ANOVA completo

modelo1<-lm(Y~(A+B+C+D)^4,data = dis_fac)
ANOVA<-aov(modelo1)
summary(modelo1)

## también podemos escribir el modelo factorial como lm(Y~A*B*C*D)

##Cálculo de los efectos

efectos<-round(2*modelo1$coefficients,2)
efectos

efectos_absolutos<-sort(abs(efectos),decreasing = TRUE)
efectos_absolutos

#Daniel´s plot
DanielPlot(modelo1,half = TRUE,main = "Gráfico normal de efectos")

#PSE Lenth
unrepx::PSE(efectos,method = "Lenth")

#Pareto Plot
unrepx::parplot(efectos[-1],absolute = TRUE,horiz = FALSE,method = "Lenth")

##Prueba de efectos
unrepx::eff.test(effects = efectos,method = "Lenth")

##ANOVA modelo de interacciones dobles

#Datos codificados
X1<-Base_Isatina$X1
X2<-Base_Isatina$X2
X3<-Base_Isatina$X3
X4<-Base_Isatina$X4

modelo2<-lm(Y~(X1+X2+X3+X4)^2,data = dis_fac)
summary(modelo2)

modelo3<-lm(Y~(A+B+D)^2,data=dis_fac)
summary(modelo3)

##Criterio de información de Akaike
AIC(modelo2,modelo3)

##Gráfico de interacción

ggplot(data = dis_fac, aes(x = B, y = Y, colour = D,
                           group = D)) +
  stat_summary(fun=mean, geom = "point") +
  stat_summary(fun=mean, geom = "line") +
  labs(y  =  "Conversión", x="Temperatura") +
  theme_bw()

# Validación de los supuestos.

#Normalidad
qqnorm(residuals(modelo2))
qqline(residuals(modelo2),col="red")
shapiro.test(residuals(modelo2))
lillie.test(residuals(modelo2))

#Independencia
ggplot(data = modelo2, aes(x = c(1:length(Y)), y = modelo2$residuals)) +
  geom_point() +
  theme_bw()+labs(x = "Observación",y = "Residuo"
  ) 

# Test de Durbin Watson
dwtest(modelo2)  

# Validación de los supuestos modelo 3.

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

# Test de Durbin Watson
dwtest(modelo3)  

##Independencia 2

Base_Isatina<- Base_Isatina%>%arrange(RO)

modelo4<-lm(Y~(A+B+D)^2,data=Base_Isatina)

ggplot(data = modelo4, aes(x = c(1:length(Y)), y = modelo4$residuals)) +
  geom_point() +
  theme_bw()+labs(x = "Observación",y = "Residuo"
  ) 

dwtest(modelo4)

