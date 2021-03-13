normality_by <- function(test_data){
  fit <- aggregate(test_data[, 1] ~ test_data[, 2] + test_data[, 3], test_data, function(x) shapiro.test(x)$p.value)
  colnames(fit) <- c(names(test_data)[2], names(test_data)[3], "p_value")
  return(fit)
}
normality_by(test_data)
normality_by(mtcars[, c("mpg", "am", "vs")])



#  ѕример правильного решени€:
  
  normality_by <- function(test){    
    grouped_data <- aggregate(test[,1],by=list(test[,2], test[,3]),                                  
                              FUN = function(x) {shapiro.test(x)$p.value})                                  
    names(grouped_data) <- c(colnames(test)[2:3],'p_value')                                  
    return(grouped_data)    
  }


#  »спользу€ dplyr (при условии, что мы знаем имена переменных в данных):
  
  library(dplyr)    
normality_by <- function(test_data){    
  result <- test_data %>% group_by(y, z) %>%     
    summarize(p_value = shapiro.test(x)$p.value)     
  return(result)    
}


#  Ѕолее общее решение с dplyr:
  
  library(dplyr)    
get_p_value <- function(x){      
  shapiro.test(x)$p.value    
}    
normality_by <- function(test){    
  grouped <- test %>%    
    group_by_(.dots = colnames(.)[2:3]) %>%         
    summarise_each(funs(get_p_value))         
  names(grouped)[3] <- 'p_value'         
  return(grouped)         
}