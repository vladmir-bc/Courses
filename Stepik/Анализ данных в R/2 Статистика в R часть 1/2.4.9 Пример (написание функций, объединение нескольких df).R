setwd("~/R/Projects/Анализ данных в R/2 Статистика в R часть 1/grants")

read_data <- function(){
  df <- data.frame()
  number <<- 0  # в таком случае переменная number сохранится и будет доступна за пределами функции
  for (i in dir(pattern = "*.csv")){
    temp_df <- read.csv(i)
    df <- rbind(temp_df, df)  # добавляет строки
    number <<- number + 1
  }
  print(paste(as.character(number), "files were combined"))
  return(df)
}

grants2 <- read_data()

