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
