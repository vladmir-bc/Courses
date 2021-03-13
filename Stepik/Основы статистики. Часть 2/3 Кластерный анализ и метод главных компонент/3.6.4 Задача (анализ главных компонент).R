get_pca2 <- function(data){
  fit <- prcomp(data)
  data <- cbind(data, fit$x[, 1 : which(summary(fit)$importance[3, ] >= 0.9)[1]])
  return(data)
}


# Пример правильного решения участника курса Максима Гальченко stepic.org/users/172958    

get_pca2 <- function(test_data){    
  fit <- prcomp(test_data)    
  cum_prop <- summary(fit)$importance['Cumulative Proportion',]    
  test_data <- cbind(test_data, fit$x[,1:min(which(cum_prop>0.9))])    
  return(test_data)
}