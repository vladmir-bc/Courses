?read.table
?read.csv

mydata <- read.csv('evals.csv', stringsAsFactors=TRUE)
mydata


head(mydata, 3)  #  показывает первые 3 строки
tail(mydata)  # показывает последние 6 строк

View(mydata)  # просмотр

str(mydata)  # показыввает структуру

summary(mydata)  # основные статистические показатели по кажд. переменной
a <- names(mydata)  # названия колонок (переменных) - вектор значений. Доступны операции с векторами

# Variables

b <- mydata$score  # получим вектор значений переменной
mean(mydata$score)  # среднее для численных векторов
summary(mydata$score)  # информация о разбросе данных
mydata$ten_point_scale <- mydata$score * 2  # создадим нвоый столбец в mydata со значениями *2

summary(mydata$ten_point_scale)  # новые описательные статистики будут в 2 раза больше

mydata$new_varible <- 0  # новый столбец с нулевыми значениями
mydata$number <- 1:nrow(mydata)  # вектор знач номеров строки с 1 по последний
summary(mydata$number)


nrow(mydata)  # возвращает количество строчек в mydata
ncol(mydata)  # количество столбцов, колонок в mydata

#  Subsetting

mydata$score[1:10]

mydata[1,1]  # выводит значение первого столбца, первой строки
mydata[c(2,193,225),1]  # значения номер 2,193,225 в 1 столбце (score)
mydata[101:200,1]  # значения 101:200 в 1 столбце (score)
mydata[5,]  # все значения 5 строки
mydata[,1]  # все значения 1 столбца
mydata[,1] == mydata$score

mydata[,2:5]  # все строчки по 2-5 столбцам
head(mydata[,2:5])  # первые 6 строчек по 2-5 столбцам

##


# Subsetting with condition

mydata$gender
mydata$gender == 'female'
head(mydata[mydata$gender == 'female',1:3])  # за счет логического вектора будут выведены первые шесть значений 1-3 переменых для female


head(subset(mydata, gender == 'female'))  # вывести только для female, условие для subset
head(subset(mydata, score > 3.5))  # отсеивает dataframe, чтобы score был выше 3,5

# rbind, cbind

mydata2 <- subset(mydata, gender == 'female')
mydata3 <- subset(mydata, gender == 'male')
mydata4 <- rbind(mydata2, mydata3)  # соединяет 2 dataframe одинаковой ширины вместе


mydata5 <- mydata[,1:10]  # первые 10 переменных
mydata6 <- mydata[,11:24]  # с 11 по 24 переменные
mydata7 <- cbind(mydata5, mydata6)  # соединяет dataframe по столбцам
