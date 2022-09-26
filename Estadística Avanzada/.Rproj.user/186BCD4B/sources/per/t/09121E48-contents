mtcars2=read.csv('mtcars2.csv',sep = ';')
head(mtcars2, 10)
summary(mtcars2)

install.packages('dplyr')
install.packages('ggplot2')
install.packages('corrplot')

require('dplyr')
require('ggplot2')
require('corrplot')

#La función str de R me indica el tipo de datos en el conjunto de datos de "mtcars". 
str(mtcars2)

#La función de resumen me permite ver estadísticas de resumen básicas para cada columna.
summary(mtcars2)

# Los cilindros se encuentran en entero, tienen que ser un valor discreto

mtcars2$cylinders = mtcars2$cylinders %>%
  factor(labels = sort(unique(mtcars2$cylinders)))

str(mtcars2$cylinders)

#Cambiar la etiqueta de los países "1,2,3" por el respectivo nombre.

origins <- c('USA', 'Europe', 'Japan')
mtcars2$origin <- factor(mtcars2$origin, labels = origins)


#Gráficos univariados
#histograma
#millas por galón

hist(mtcars2$mpg, xlab = "Millas por galón", ylab = "Frecuencia", 
     main='Histograma: Millas por galón',col = "blue")

#¿Que tipo de asimetría presenta?

#Número de cilindros

qplot(mtcars2$cylinders, xlab = "Cilindros", ylab = "Cuenta", 
      main="Diagrama de barras - número de cilindros")

# Número de cilindros presentación en tabla
table(mtcars2$cylinders)

# Histograma Peso

hist(mtcars2$weight, xlab = "Peso", ylab = "Frecuencia", 
     main='Histograma: Peso',col = "blue", breaks=sqrt(length(mtcars2$weight)))


#¿Qué tipo de asimetría presenta? Positiva
#¿Qué tipo de curtosis presenta?

# Histograma aceleración
hist(mtcars2$acceleration, xlab = "Aceleración", ylab = "Frecuencia", 
     main='Histograma: Aceleración',col = "green",breaks =sqrt(length(mtcars2$acceleration)))

#¿Qué tipo de asimetría presenta?0
#¿Qué tipo de curtosis presenta?0
#¿Gráficamente podría comportarse como una distribución normal? Quizá sí

#Gráfico de barras frecuencia número de vehículos por año

qplot(mtcars2$model, xlab = "Modelo", ylab = "Frecuencia", 
      main="Diagrama de barras - Vehículos por modelo")
table(mtcars2$model)


#Gráfico de barras frecuencia - número de vehículos por fabricante

# ¿Qué país presenta una mayor frecuencia?

ggplot(mtcars2, aes(x = origin)) +
  geom_bar() +
  geom_text(aes(label = ..count..), stat = "count", vjust = 1.25, colour = "white")+
  xlab("País fabricante")+
  ylab("Frecuencia")

#Gráficos bivariados

#Gráfico de dispersión (peso vs millas por galón)

ggplot(data = filter(mtcars2,mpg>100), aes(x = mpg, y = weight)) +
  geom_point() +
  geom_smooth(method='lm') +
  xlab('Millas por galón') +
  ylab("Peso") +
  ggtitle("MPG vs. Peso")

ggplot(data = filter(mtcars2,mpg<100), aes(x = mpg, y = weight)) +
  geom_point() +
  geom_smooth(method='lm') +
  xlab('Millas por galón') +
  ylab("Peso") +
  ggtitle("MPG vs. Peso")


#Diagrama de cajas y bigotes
#Millas por galón segmentado por país

ggplot(data = filter(mtcars2,mpg>100), aes(x = origin, y = mpg)) +
  geom_boxplot() +
  xlab("Región de origen") +
  ylab('MPG') +
  ggtitle("Comparación MPG por región de Origen")+ geom_boxplot(aes(colour=origin, group=origin))

ggplot(data = filter(mtcars2,mpg<100), aes(x = origin, y = mpg)) +
  geom_boxplot() +
  xlab("Región de origen") +
  ylab('MPG') +
  ggtitle("Comparación MPG por región de Origen")+ geom_boxplot(aes(colour=origin, group=origin))



model_years = sort(unique(mtcars2$model))
mtcars2$model = mtcars2$model %>%
factor(labels = model_years)


#Millas por galón por año de fabricación

ggplot(data = mtcars2, aes(x = model, y = mpg)) +
  geom_boxplot() +
  xlab('Model Year') +
  ylab('MPG') +
  ggtitle('MPG Comparison by Model Year')+geom_boxplot(aes(colour=model, group=model))

summary(mtcars2$model)

## Realice un diagrama de cajas y bigotes para determinar gráficamente si existe alguna diferencia
## entre los pesos de los vehículos por su origen de fabricación.

ggplot(data = mtcars2, aes(x = origin, y = weight)) +
  geom_boxplot() +
  xlab('Origin Country') +
  ylab('Weight') +
  ggtitle('Weight Comparison by Origin Country')+geom_boxplot(aes(colour=origin, group=origin))


## Realice un diagrama de cajas y bigotes para determinar gráficamente si existe alguna diferencia
## entre el rendimiento de los vehículos por su número de cilindros.

ggplot(data = mtcars2, aes(x = cylinders, y = mpg)) +
  geom_boxplot() +
  xlab('Cylinders') +
  ylab('Milles per Galon') +
  ggtitle('MPG Comparison by number of Cylinders')+geom_boxplot(aes(colour=cylinders, group=cylinders))



## ¿Existe un relación entre el número de cilindros y el peso de los vehículos? ¿Qué gráfico utilizaría para argumentar su respuesta?
ggplot(data = mtcars2, aes(x = cylinders, y = weight)) +
  geom_boxplot() +
  xlab('Cylinders') +
  ylab('Weight') +
  ggtitle('Weight Comparison by number of Cylinders')+geom_boxplot(aes(colour=cylinders, group=cylinders))



## Nombrar las variables que presentan correlación positiva (>=70%) y correlación  negativa (<= - 70%).

str(mtcars2)

mtcars3<-mtcars2[,c(-1,-3,-8,-9,-10)]
head(mtcars3)
M <- cor(mtcars3)
library(corrplot)
corrplot(M, method = "circle")
corrplot(M, method = "number")
M>0.7
M[1,1]
col.names()
NamesStat=c('mpg',         
            'displacement',
            'horsepower',  
            'weight',      
            'acceleration')

for (i in c(2:4)){
  for (j in c((i+1):5)){
    if ((M[i,j]>=0.7) | (M[i,j]<=-0.7)){
      print(paste('Hay correlación entre',NamesStat[i],'y',NamesStat[j]))
    }
  }
}

