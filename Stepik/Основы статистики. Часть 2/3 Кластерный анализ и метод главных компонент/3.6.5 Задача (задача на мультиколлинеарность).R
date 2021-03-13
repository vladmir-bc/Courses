test_data <- read.csv("https://stepic.org/media/attachments/course/524/Norris_1.csv")
test_data <- read.csv("https://stepic.org/media/attachments/course/524/Norris_2.csv")
test_data <- read.csv("https://stepic.org/media/attachments/course/524/Norris_3.csv")


is_multicol <- function(d){
  corr_t <- cor(d)
  diag(corr_t) <- 0
  is_multic <- row.names(which((corr_t > 0.999 | corr_t < -0.999), arr.ind = T))
  if (length(is_multic) > 0){
    return(is_multic)
  } else {
    return("There is no collinearity in the data")
  }
}

is_multicol(test_data)


#Пример правильного решения:      

is_multicol <- function(d){    
  d <- abs(cor(d))     
  d[lower.tri(d)] <- 0    
  diag(d) <- 0    
  index <- which((1-d) < 1e-10, arr.ind = T)
  if (length(index) == 0){      
    return('There is no collinearity in the data')    
  } else {      
    return(rownames(d)[index])      
  }      
}

is_multicol(test_data)
