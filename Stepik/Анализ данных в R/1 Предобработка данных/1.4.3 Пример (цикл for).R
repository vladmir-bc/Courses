mydata <- read.csv('evals.csv')


# for
for (i in 1:100){
  print(i)
}

for (i in 1:nrow(mydata)){  # оператор for Обязательно должен включать в себя вектор значений
  print(mydata$score[i])
}

for (i in 1:nrow(mydata)){
  if (mydata$gender[i] == 'male'){
    print(mydata$score[i])
  }
}


# for + if vs ifelse

mydata$quality <- rep(NA, nrow(mydata))  # создаем новую переменную (столбец), присваиваем ей пустые значения NA
mydata$quality <- NA

for (i in 1:nrow(mydata)){
  if (mydata$score[i] > 4){
    mydata$quality[i] <- 'good'
  } else {
    mydata$quality[i] <- 'bad'
    }
}

# с помощью ifelse:

mydata$quality2 <- ifelse(mydata$score > 4, 'good', 'bad')
mydata$quality2

# оператор while
i <- 1

while (i < 51){
  print(mydata$score[i])  # вывод оценки преподавателя в i-ой строчке
  i <- i+1
}
