test_data <- read.csv("https://stepic.org/media/attachments/course/524/cen_data.csv")
var_names = c("X4", "X2", "X1")


centered <- function(test_data, var_names){
  test_data[, var_names] <- sapply(var_names, function(x) test_data[,x] - mean(test_data[,x]))
  return(test_data)
}
centered(test_data, var_names)


# Пример правильного решения:

centered <- function(test_data, var_names){    
  test_data[var_names] <- sapply(test_data[var_names], function(x) x - mean(x))    
  return(test_data)    
}
