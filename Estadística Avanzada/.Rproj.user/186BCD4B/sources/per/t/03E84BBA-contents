rm(list = ls())
#intervalos de confianza.

#punto 1
## Creo el vector de datos
datos_P1<-c(96.11, 91.06, 93.38, 88.52, 89.57, 92.63, 85.20, 91.41, 89.79, 92.62)

#Estimador puntual de la media
xbar<-round(mean(datos_P1),2)

#La raíz del estimador puntual de la varianza no es necesariamente un factor insesgado. Tiene cierto sesgo.
#Estimador puntual de la desviación estándar (Tiene cierto sesgo)
S<-round(sd(datos_P1),2)
c(xbar,S)

#IC para la media
n<-length(datos_P1)
t<-round(qt(0.05/2,n-1,lower.tail = FALSE),2)
c(n,t)
L_inf_media<-round(xbar-t*S/sqrt(n),2)
L_sup_media<-round(xbar+t*S/sqrt(n),2)
c(L_inf_media,L_sup_media)

#Intervalo de confianza para la varianza
L_inf_SD<-round(sqrt(((n-1)*S^2)/qchisq(0.025,n-1,lower.tail = FALSE)),2)
L_sup_SD<-round(sqrt(((n-1)*S^2)/qchisq(0.025,n-1)),2)
c(L_inf_SD,L_sup_SD)

## a.	Plantee una hipótesis para la media en la que contraste el resultado con el parámetro poblacional 92. ¿Qué puede inferir?

t_calculado = abs((xbar-92)/(S/sqrt(n)))
t_critico =t
c(t_calculado,t_critico)
t.test(datos_P1, mu=92)
t.test(datos_P1, mu=92, alternative = "less")

install.packages("EnvStats")
library(EnvStats)

IC_SD<-varTest(datos_P1)
round(sqrt(IC_SD$conf.int),2)

## Punto 2
n_1<-250
x<-15
p_est<-round(x/n_1,2)
p_est
z<-round(qnorm(0.05/2,lower.tail = FALSE),2)
L_inf_prop<-round(p_est-(z*sqrt(((p_est*(1-p_est))/n_1))),3)
L_sup_prop<-round(p_est+(z*sqrt((p_est*(1-p_est)/n_1))),3)
c(L_inf_prop,L_sup_prop)

##Prueba chi cuadrado de pearson
prop.test(x=x,n=n_1,p=0.07)

## Binomial exacta

binom.test(x=x,n=n_1,p=0.07)
binom.test(x=x,n=n_1,p=0.07, alternative = "less")

## Punto 3

miu_A<-36
miu_B<-42
dif_medias<-miu_B-miu_A
z_1<-round(qnorm((0.04/2),lower.tail = FALSE),2)
z_1
D_est_A<-6
D_est_B<-8
n_A<-50
n_B<-75
ee_dif_medias<-sqrt((D_est_A^2/n_A)+(D_est_B^2/n_B))
L_inf_dif_medias<-round(dif_medias-(z_1*ee_dif_medias),2)
L_sup_dif_medias<-round(dif_medias+(z_1*ee_dif_medias),2)
c(L_inf_dif_medias,L_sup_dif_medias)


#Punto 4
n_est_1<-12
n_est_2<-10
xbar_est_1<-3.11
xbar_est_2<-2.04
dif_medias_1<-xbar_est_1-xbar_est_2
D_est_est_1<-0.771
D_est_est_2<-0.448
gl<-n_est_1+n_est_2-2
t_1<-qt(0.95,gl)
t_1
ee_dif_medias_1<-sqrt((1/n_est_1)+(1/n_est_2))
sp<-sqrt(round((((n_est_1-1)*(D_est_est_1^2))+((n_est_2-1)*D_est_est_2^2))/gl,3))
L_inf_dif_medias_1<-round(dif_medias_1-(t_1*sp*ee_dif_medias_1),3)
L_sup_dif_medias_1<-round(dif_medias_1+(t_1*sp*ee_dif_medias_1),3)
c(L_inf_dif_medias_1,L_sup_dif_medias_1)


#Punto 5
n_esta_1<-15
n_esta_2<-12
xbar_esta_1<-3.84
xbar_esta_2<-1.49
D_est_esta_1<-3.07
D_est_esta_2<-0.80
dif_medias_2<-xbar_esta_1-xbar_esta_2
num_gl<-((D_est_esta_1^2/n_esta_1)+(D_est_esta_2^2/n_esta_2))^2
den_gl<-(((D_est_esta_1^2/n_esta_1)^2)/(n_esta_1-1))+(((D_est_esta_2^2/n_esta_2)^2)/(n_esta_2-1))
gl2<-trunc(num_gl/den_gl)
t_2<-round(qt(0.05/2,gl2,lower.tail = FALSE),3)
ee_dif_medias_2<-sqrt((D_est_esta_1^2/n_esta_1)+(D_est_esta_2^2/n_esta_2))
L_inf_dif_medias_2<-round(dif_medias_2-(t_2*ee_dif_medias_2),3)
L_sup_dif_medias_2<-round(dif_medias_2+(t_2*ee_dif_medias_2),3)
c(L_inf_dif_medias_2,L_sup_dif_medias_2)

#Punto 6
datos_antes<-c(25,20,25,28,30,30,26,15,18,22,23,25)
datos_despues<-c(30,25,28,29,30,31,24,22,25,27,24,26)
dif<-datos_antes-datos_despues
S_dif<-sd(dif)
n_dif<-length(datos_antes)
media_dif<-mean(dif)
t_dif<-qt(0.01/2,n_dif-1,lower.tail = FALSE)
t_dif
L_inf_dif<-round(media_dif-(t_dif*(S_dif/sqrt(n_dif))),3)
L_sup_dif<-round(media_dif+(t_dif*(S_dif/sqrt(n_dif))),3)
c(L_inf_dif,L_sup_dif)


## Intervalo de confianza al 99%
t.test(datos_antes,datos_despues,paired = TRUE,conf.level = 0.99)

## Razón de varianza de los tratamientos
var.test(datos_antes,datos_despues)

## Diferencia de medias

t.test(x=(datos_despues-datos_antes),mu=0,conf.level = 0.99)
