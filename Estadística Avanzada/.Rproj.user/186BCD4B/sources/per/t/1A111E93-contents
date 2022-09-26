install.packages("BSDA")
library(BSDA)
library(ggplot2)
library(car)
library(dplyr)
library(readxl)

#U Mann Withney - Suma de rangos de Wilcoxon

##Ejercicio 1
Base_NP = read_excel("C:/Users/DAVID MORA MEZA/Desktop/Base_NP.xlsx")
View(Base_NP)
## Prueba de normalidad para la variable de índice de masa corporal muestra total 
IMC<-as.double(Base_NP$IMC)
shapiro.test(IMC)

## Segmentación de los datos de acuerdo con la variable de tabaquismo
IMC_SI_tabaquismo<-Base_NP%>%select(Tabaquismo,IMC)%>%filter(Tabaquismo=="Sí")
IMC_NO_tabaquismo<-Base_NP%>%select(Tabaquismo,IMC)%>%filter(Tabaquismo=="No")

#Boxplot

ggplot(data = Base_NP, mapping = aes(x = Tabaquismo, y = as.double(IMC), colour = Tabaquismo)) +
  geom_boxplot() +
  theme_bw() +
  theme(legend.position = "none")

##Medida de posición

median(as.double(IMC_SI_tabaquismo$IMC))
median(as.double(IMC_NO_tabaquismo$IMC))

## Prueba de nornalidad segmentado por tabaquismo

shapiro.test(as.double(IMC_SI_tabaquismo$IMC))
shapiro.test(as.double(IMC_NO_tabaquismo$IMC))

##Prueba de rangos de Wilcoxon

tabaquismo<-factor(Base_NP$Tabaquismo)
wilcox.test(IMC~tabaquismo, alternative = "two.sided")

## Prueba de Kruskal Wallis

#Boxplot

ggplot(data = Base_NP, mapping = aes(x = reorder(Gravedad_asma,as.double(IMC)), y = as.double(IMC), colour = Gravedad_asma)) +
  geom_boxplot() +
  theme_bw() +
  theme(legend.position = "none")

#Varianza constante
leveneTest(as.double(IMC) ~ factor(Gravedad_asma), data = Base_NP, center = "median")

#Prueba de Kruskal Wallis
kruskal.test(as.double(IMC) ~ factor(Gravedad_asma), data = Base_NP)

#Chi cuadrado crítico
qchisq(0.05,2,lower.tail = FALSE)


## Parte 2

## U Mann Whitney

A<-c(60,80,25,30,40,60,90,100,60,55)
B<-c(55,70,90,110,45,60,60,75,80,95,100,110,95,60,70,80,40,65,50,75,90,90,100,80,100)

datos1<-data.frame( Sistema_Estudio = c(rep("A", length(A)), rep("B", length(B))), Fluidez = c(A,B))
head(datos1)

shapiro.test(datos1$Fluidez)

shapiro.test(A)
shapiro.test(B)

ggplot(data = datos1, mapping = aes(x = Sistema_Estudio, y = Fluidez, colour = Sistema_Estudio)) +
  geom_boxplot() +
  theme_bw() +
  theme(legend.position = "none")

var.test(A,B)

t.test(A,B,var.equal = TRUE)

#En caso de que no se comporten normal
##Prueba de rangos de Wilcoxon

wilcox.test(A,B, alternative = "two.sided")

#Punto 5
datos2 <- data.frame( Sistema = c(rep("S1", 5), rep("S2", 6), rep("S3", 8)), TU = c(24,16.7,22.8,19.8,18.9,23.2,19.8,18.1,17.6,20.2,17.8,18.4,19.1,17.3,17.3,19.7,18.9,18.8,19.3))
head(datos2)

#Boxplot

ggplot(data = datos2, mapping = aes(x = Sistema, y = TU, colour = Sistema)) +
  geom_boxplot() +
  theme_bw() +
  theme(legend.position = "none")

shapiro.test(datos2$TU)

#Varianza constante
leveneTest(TU ~ factor(Sistema), data = datos2, center = "median")

#Prueba de Kruskal Wallis

kruskal.test(TU ~ Sistema, data=datos2)

#Chi cuadrado crítico
qchisq(0.05,2,lower.tail = FALSE)