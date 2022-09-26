library(readr)
Base_mq <- read_table("~/9 Semestre/Estadística Avanzada/Semana 5/diametro_piezas.txt")
View(Base_mq)

## Realizamos la selección de la muestra por máquina por muestreo aleatorio simple

power.t.test(sig.level = 0.01,power = .98,delta = 0.5,type = "one.sample")

#Muestreo aleatorio simple
#Extraer una muestra de 89.
#creamos la semilla y el generador
N<-1000
set.seed(6)
a<-sample(N,89,replace = FALSE)
a
#Extraer los elementos del muestreo de la base
muestra_Mq<-Base_mq[sort(a),]
View(muestra_Mq)

media_M1<-mean(muestra_Mq$M1)
desv_M1<-sd(muestra_Mq$M1)

media_M2<-mean(muestra_Mq$M2)
desv_M2<-sd(muestra_Mq$M2)

media_M1
desv_M1

media_M2
desv_M2

## Diagrama de cajas y bigotes

par(mfrow=c(1,2))
boxplot(Base_mq$M1,main="Boxplot M1", col = "green")
boxplot(Base_mq$M2,main="Boxplot M2", col = "blue")

## Piezas defectuosas M1
LimInf=195
LimSup=205
pnorm(LimInf,mean = media_M1, desv_M1,lower.tail = TRUE)+
  pnorm(LimSup,mean = media_M1, desv_M1,lower.tail = FALSE)

## Piezas defectuosas M2

pnorm(LimInf,mean = media_M2, desv_M2,lower.tail = TRUE)+
  pnorm(LimSup,mean = media_M2, desv_M2,lower.tail = FALSE)

## reproceso M1

defectuosas_M1_reproceso<-function(XM3,media_M1,desv_M1){
  
  ZM3<-(XM3-media_M1)/(desv_M1)
  print(round(pnorm(ZM3,lower.tail = FALSE),4))
}
defectuosas_M1_reproceso(205,media_M1,desv_M1)

pnorm(195,mean = media_M1,sd = desv_M1)

## reproceso M2

defectuosas_M2_reproceso<-function(XM4,media_M2,desv_M2){
  
  ZM4<-(XM4-media_M2)/(desv_M2)
  print(round(pnorm(ZM4,lower.tail = FALSE),4))
}
defectuosas_M2_reproceso(205,media_M2,desv_M2)
