library(nortest)
library(car)
library(lmtest)
library(ggplot2)
install.packages("DescTools")
library(DescTools)

Temperatura<-Base_temp$y
Silo<-factor(Base_temp$i)
Dia<-factor(Base_temp$j)


#Diagrama de cajas y bigotes
#Silo
ggplot(Base_temp, aes(x=Silo, y=Temperatura,color=Silo)) + 
  geom_boxplot()+ 
  
  labs(
    title = "Temperatura por silo")

#Día
ggplot(Base_temp, aes(x=Dia, y=Temperatura, color=Dia)) + 
  geom_boxplot()+ 
  
  labs(
    title = "Temperatura diaria")

# ANOVA

modelo<-lm(Temperatura~Silo+Dia)
summary.aov(modelo)
summary(modelo)

#Normalidad de los residuos
qqnorm(residuals(modelo))
qqline(residuals(modelo),col="red")
shapiro.test(residuals(modelo))
lillie.test(residuals(modelo))

#Varianza constante
#Prueba de Bartlett

bartlett.test(Temperatura~Silo)
bartlett.test(Temperatura~Dia)

#Prueba de Levene
leveneTest(Temperatura~Silo)
leveneTest(Temperatura~Dia)

#Independencia
N<-length(Base_temp$y)
ggplot(data = Base_temp, aes(x = c(1:N), y = modelo$residuals)) +
  geom_point() +
  theme_bw()+labs(x = "Observaciones",y = "Residuo")

# Test de Durbin Watson
dwtest(modelo)

#Mejor modelo
step(modelo)

#modelo 2
modelo2<-lm(Temperatura~Silo)
summary(aov(modelo2))
summary(modelo2)

#Normalidad de los residuos Modelo 2
qqnorm(residuals(modelo2))
qqline(residuals(modelo2),col="red")
shapiro.test(residuals(modelo2))
lillie.test(residuals(modelo2))

#Independencia
N<-length(Base_temp$y)
ggplot(data = Base_temp, aes(x = c(1:N), y = modelo2$residuals)) +
  geom_point() +
  theme_bw()+labs(x = "Observaciones",y = "Residuo")

# Test de Durbin Watson
dwtest(modelo2)

#Comparación de tratamientos con un control
DunnettTest(x = Temperatura,g = Silo, control = "B")

library(ggstatsplot)
#Gráficos con estadísticos incluidos

ggbetweenstats(
  data = Base_temp,
  x = i,
  y = y,
  title = "Temperatura por silo", type = "parametric", var.equal = TRUE)

stats_results <- ggbetweenstats(Base_temp, i, y, output = "subtitle",type = "parametric",var.equal = TRUE)

ggplot(data = Base_temp, aes(x = Silo, y = Temperatura, color = Silo)) +
  geom_boxplot() +
  theme_bw()+labs(
    subtitle = stats_results,
  )

# Comparación o prueba de rangos múltiples

#Método Corrección de Bonferroni
pairwise.t.test(x = Temperatura,g = Silo,p.adjust.method = "bonf")

#Método de Tukey
TukeyHSD(aov(modelo2))
plot(TukeyHSD(aov(modelo2)))
