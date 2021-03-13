mydata <- read.csv('evals.csv')

a <- 0

# опреатор if

if (a > 0){
  print('positive')
} 
if (a == 0){
  print('equal')
} else {
  print('not positive')
}

# другой вариант записи в одну строчку. Отличие такой структуры - может работать с векторами произвольной длины
a <- c(1, -1)

ifelse(a > 0, 'positive', ifelse(a == 0, 'equal', 'not positive'))  # итерируемая конструкция
