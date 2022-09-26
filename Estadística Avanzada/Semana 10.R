library(ggplot2)
library(nortest)
library(lmtest)
library(car)

P_algodon<-factor(Base_Algodon$P_algodon)
Y<-Base_Algodon$Y

#Diagrama de cajas
ggplot(data = Base_Algodon, aes(x = P_algodon, y = Y, color = P_algodon)) +
  geom_boxplot() +
  theme_bw()

#Modelo
modelo<-lm(Y~P_algodon)

#Anova modelo
summary(aov(modelo))
summary(modelo)

#Validación de los supuestos del modelo

#Normalidad de los residuos
qqnorm(residuals(modelo))
qqline(residuals(modelo),col="red")
shapiro.test(residuals(modelo))
lillie.test(residuals(modelo))

#Varianza constante

#Test de Bartlett
bartlett.test(Y~P_algodon, data = Base_Algodon)

#Test Breush Pagan
bptest(Y~P_algodon)

#Test de Levene
leveneTest(Y~P_algodon)

#Independencia
ggplot(data = modelo, aes(x = c(1:25), y = modelo$residuals)) +
  geom_point() +
  theme_bw()+labs(x = "Observación",y = "Residuo")

# Test de Durbin Watson
dwtest(modelo)

# Comparación o prueba de rangos múltiples

#Método Corrección de Bonferroni
pairwise.t.test(x = Y,g = P_algodon,p.adjust.method = "bonf")

#Método de Tukey
TukeyHSD(aov(modelo))
plot(TukeyHSD(aov(modelo)))


#Tamaño del efecto
install.packages("effectsize")
library(effectsize)

a<-effectsize::eta_squared(modelo)
b<-effectsize::omega_squared(modelo)

interpret_eta_squared(a, rules = "cohen1992")
interpret_omega_squared(b, rules = "cohen1992")

install.packages("ggstatsplot")
library(ggstatsplot)

#Gráficos con estadísticos incluidos

ggbetweenstats(
  data = Base_Algodon,
  x = P_algodon,
  y = Y,
  title = "Distribución resistencia por porcentaje de algodón")

stats_results <- ggbetweenstats(Base_Algodon, P_algodon, Y, output = "subtitle",type = "parametric",var.equal = TRUE)

ggplot(data = Base_Algodon, aes(x = P_algodon, y = Y, color = P_algodon)) +
  geom_boxplot() +
  theme_bw()+labs(
    subtitle = stats_results,
    x = "Porcentaje de algodón",
    y = "Resistencia"
  )
