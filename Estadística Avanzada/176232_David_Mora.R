field_data=read.csv('field_data.csv',sep = ',')

require('dplyr')
require('ggplot2')
require('corrplot')

str(field_data)

summary(field_data)

unique(field_data$height)
unique(field_data$fertilizer)
unique(field_data$region)


field_data$height = field_data$height %>%
  factor(labels = sort(unique(field_data$height)))

field_data$fertilizer = field_data$fertilizer %>%
  factor(labels = sort(unique(field_data$fertilizer)))

field_data$region = field_data$region %>%
  factor(labels = sort(unique(field_data$region)))

summary(field_data)

#¿Evidencia una relación entre las variables de temperatura y humedad?

ggplot(data = field_data, aes(x = temp, y = humidity)) +
  geom_point() +
  xlab('Temperatura') +
  ylab("Humedad") +
  ggtitle("Temperatura vs. Humedad")

#¿Cuál es la región que puede presentar un rendimiento promedio superior en el cultivo?

ggplot(data = field_data, aes(x = region, y = yield)) +
  geom_boxplot() +
  xlab('Región') +
  ylab("Rendimiento") +
  ggtitle("Rendimiento por Región") +
  geom_boxplot(aes(colour=region, group=region))+
  stat_summary(fun=mean, geom="point")


#¿Entre más temperatura más rendimiento?

ggplot(data = field_data, aes(x = temp, y = yield)) +
  geom_point() +
  xlab('Temperatura') +
  ylab("Rendimiento") +
  ggtitle("Temperatura vs. Rendimiento")

#¿Entre más humedad más rendimiento?

ggplot(data = field_data, aes(x = humidity, y = yield)) +
  geom_point() +
  geom_smooth(method='lm') +
  xlab('Humedad') +
  ylab("Rendimiento") +
  ggtitle("Humedad vs. Rendimiento")

#¿La variable de altura produce un rendimiento superior en su nivel más alto?

ggplot(data = field_data, aes(x = height, y = yield)) +
  geom_boxplot() +
  xlab('Altura') +
  ylab("Rendimiento") +
  ggtitle("Rendimiento por Altura") +
  geom_boxplot(aes(colour=height, group=height))+
  stat_summary(fun=mean, geom="point")

#Validación de relaciones entre variables

field_data2<-field_data[,c(-1,-4,-6)]
M <- cor(field_data2)
corrplot(M, method = "circle")
corrplot(M, method = "number")
