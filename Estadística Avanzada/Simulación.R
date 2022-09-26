library(ggplot2)
library(dplyr)
library(readxl)
CycleTime <- read_excel("C:/Users/DAVID MORA MEZA/Desktop/ArchivosInv/CycleTime.xlsx", 
                        col_types = c("text", "text", "numeric", 
                                      "numeric", "text", "text", "numeric"))
View(CycleTime)


CycleTime=filter(CycleTime,Hora>=168)

CycleTimeR=filter(CycleTime,Paciente=="Respiratorio")
CycleTimeT2=filter(CycleTime,Paciente=="Triage 2")
CycleTimeT3=filter(CycleTime,Paciente=="Triage 3")

## Análisis de Triage ##

ggplot(data = CycleTime, aes(x = Paciente, y = Tiempo, color = Paciente)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Tipo de Paciente",y = "Tiempo")

ggplot(data = CycleTime, aes(x = Tiempo, color = Paciente)) +
  geom_density()+
  geom_histogram(fill="white",aes(y=..density..), position="identity", alpha=0.2)

ggplot(data = CycleTime, aes(x = Tiempo, color = Paciente)) + 
  geom_density()+
  labs(x = "Tipo de Paciente",y = "Tiempo")

##Interacción Tipo de Paciente y Covid###
ggplot(data = CycleTime, aes(x = Paciente, y = Tiempo, color = Covid)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Tipo de Paciente",y = "Tiempo")

ggplot(data = CycleTime, aes(x = Covid, y = Tiempo, colour = Paciente,
                                group = Paciente)) +
  stat_summary(fun = mean, geom = "point") +
  stat_summary(fun = mean, geom = "line") +
  labs(y  =  "Tiempo en sistema", x="Proporción pacientes Covid") +
  theme_bw()

###Análisis de Covid Respiratorio###

ggplot(data = CycleTimeR, aes(x = Covid, y = Tiempo, color = Covid)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Porcentaje de Covid",y = "Tiempo")

ggplot(data = CycleTimeR, aes(x = Tiempo, color = Covid)) +
  geom_density()+
  geom_histogram(fill="white",aes(y=..density..), position="identity", alpha=0.2)

ggplot(data = CycleTimeR, aes(x = Tiempo, color = Covid)) + 
  geom_density()

##Análisis de turno Respiratorio##

ggplot(data = CycleTimeR, aes(x = reorder(Turno,Tiempo), y = Tiempo, color = Turno)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Turno",y = "Tiempo")

ggplot(data = CycleTimeR, aes(x = Tiempo, color = Turno)) + 
  geom_histogram(fill="white",aes(y=..density..), position="identity", alpha=0.2)

ggplot(data = CycleTimeR, aes(x = Tiempo, color = Turno)) + 
  geom_density()


##Análisis de día Respiratorio##
ggplot(data = CycleTimeR, aes(x = reorder(Día,Tiempo), y = Tiempo, color = Día)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Día",y = "Tiempo")
ggplot(data = CycleTimeR, aes(x = Tiempo, color = Día)) + 
  geom_density()

###Análisis de Covid Triage 2###

ggplot(data = CycleTimeT2, aes(x = Covid, y = Tiempo, color = Covid)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Porcentaje de Covid",y = "Tiempo")

ggplot(data = CycleTimeT2, aes(x = Tiempo, color = Covid)) +
  geom_density()+
  geom_histogram(fill="white",aes(y=..density..), position="identity", alpha=0.2)

ggplot(data = CycleTimeT2, aes(x = Tiempo, color = Covid)) + 
  geom_density()

##Análisis de turno Triage 2##

ggplot(data = CycleTimeT2, aes(x = reorder(Turno,Tiempo), y = Tiempo, color = Turno)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Turno",y = "Tiempo")

ggplot(data = CycleTimeT2, aes(x = Tiempo, color = Turno)) + 
  geom_histogram(fill="white",aes(y=..density..), position="identity", alpha=0.2)

ggplot(data = CycleTimeT2, aes(x = Tiempo, color = Turno)) + 
  geom_density()


##Análisis de día Triage 2##
ggplot(data = CycleTimeT2, aes(x = reorder(Día,Tiempo), y = Tiempo, color = Día)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Día",y = "Tiempo")
ggplot(data = CycleTimeT2, aes(x = Tiempo, color = Día)) + 
  geom_density()


###Análisis de Covid Triage 3###

ggplot(data = CycleTimeT3, aes(x = Covid, y = Tiempo, color = Covid)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Porcentaje de Covid",y = "Tiempo")

ggplot(data = CycleTimeT3, aes(x = Tiempo, color = Covid)) +
  geom_density()+
  geom_histogram(fill="white",aes(y=..density..), position="identity", alpha=0.2)

ggplot(data = CycleTimeT3, aes(x = Tiempo, color = Covid)) + 
  geom_density()

##Análisis de turno Triage 3##

ggplot(data = CycleTimeT3, aes(x = reorder(Turno,Tiempo), y = Tiempo, color = Turno)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Turno",y = "Tiempo")

ggplot(data = CycleTimeT3, aes(x = Tiempo, color = Turno)) + 
  geom_histogram(fill="white",aes(y=..density..), position="identity", alpha=0.2)

ggplot(data = CycleTimeT3, aes(x = Tiempo, color = Turno)) + 
  geom_density()


##Análisis de día Triage 3##
ggplot(data = CycleTimeT3, aes(x = reorder(Día,Tiempo), y = Tiempo, color = Día)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Día",y = "Tiempo")
ggplot(data = CycleTimeT3, aes(x = Tiempo, color = Día)) + 
  geom_density()

### WIP  ###

WIP <- read_excel("C:/Users/DAVID MORA MEZA/Desktop/ArchivosInv/WIP.xlsx", 
                          col_types = c("numeric", "numeric", "text", 
                                        "text", "text", "text"))
View(WIP)

WIP=filter(WIP,Hora>=168)

ggplot(data = WIP, aes(x = Hora, y = Pacientes, color=Covid)) + 
  geom_line() +
  theme_bw()+labs(x = "Día",y = "Tiempo")

WIP90=filter(WIP,Covid=="0.9")

ggplot(data = WIP90, aes(x = Hora, y = Pacientes, color=Réplica)) + 
  geom_line() +
  theme_bw()+labs(x = "Día",y = "Tiempo")


NWIP=aggregate(WIP$Pacientes, list(WIP$Hora,WIP$Covid), FUN=mean)

NWIP=tibble(NWIP)
colnames(NWIP)=c("Hora","Covid","Pacientes")
NWIP$Turno=ifelse(NWIP$Hora%%24<=4,"0:00-4:00",
                  ifelse(NWIP$Hora%%24<=8,"4:00-8:00",
                         ifelse(NWIP$Hora%%24<=12,"8:00-12:00",
                                ifelse(NWIP$Hora%%24<=16,"12:00-16:00",
                                       ifelse(NWIP$Hora%%24<=20,"16:00-20:00","20:00-24:00")))))
NWIP$Día=ifelse(NWIP$Hora%%168<=24,"Lunes",
                  ifelse(NWIP$Hora%%168<=48,"Martes",
                         ifelse(NWIP$Hora%%168<=72,"Miércoles",
                                ifelse(NWIP$Hora%%168<=96,"Jueves",
                                       ifelse(NWIP$Hora%%168<=120,"Viernes",
                                              ifelse(NWIP$Hora%%168<=144,"Sábado","Domingo"))))))

ggplot(data = NWIP, aes(x = Hora, y = Pacientes, color=Covid)) + 
  geom_line() +
  theme_bw()+labs(x = "Hora",y = "Cantidad de Pacientes")

ggplot(data = NWIP, aes(x = Pacientes, color = Covid)) +
  geom_density()+
  geom_histogram(fill="white",aes(y=..density..), position="identity", alpha=0.2)

ggplot(data = NWIP, aes(x = Pacientes, color = Covid)) + 
  geom_density()

ggplot(data = NWIP, aes(x = reorder(Turno,Pacientes), y = Pacientes, color = Covid)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Día",y = "Tiempo")

ggplot(data = filter(NWIP,Covid != 0.05), aes(x = reorder(Turno,Pacientes), y = Pacientes, color = Covid)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Día",y = "Tiempo")
ggplot(data = filter(NWIP,Covid == 0.05), aes(x = reorder(Turno,Pacientes), y = Pacientes, color = Turno)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Día",y = "Tiempo")

ggplot(data = filter(NWIP,Covid == 0.05), aes(x = reorder(Día,Pacientes), y = Pacientes, color = Día)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Día",y = "Tiempo")

ggplot(data = filter(NWIP,Covid == 0.05), aes(x = reorder(Día,Pacientes), y = Pacientes, color = Turno)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Día",y = "Tiempo")

ggplot(data = NWIP, aes(x = reorder(Día,Pacientes), y = Pacientes, color = Covid)) + 
  geom_boxplot() +
  theme_bw()+labs(x = "Día",y = "Tiempo")
