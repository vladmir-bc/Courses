test_data <- read.csv("https://stepic.org/media/attachments/course/524/test_luggage_1.csv", stringsAsFactors = T)

test_data <- read.csv("https://stepic.org/media/attachments/course/524/test_luggage_2.csv", stringsAsFactors = T)


get_features <- function(dataset){
  fit <- glm(is_prohibited ~ weight + length + width + type, dataset, family = 'binomial')
  if (length(names(dataset[which(anova(fit, test="Chisq")$Pr < 0.05)]))){
    return(names(dataset[which(anova(fit, test="Chisq")$Pr < 0.05)]))
    
  } else{
    return("Prediction makes no sense")
  }
}
get_features(test_data)


# Пример правильного решения:
  
get_features <- function(test_data){    
  fit <- glm(is_prohibited ~., test_data, family = 'binomial')    
  result <- anova(fit, test = 'Chisq')    
  if (all(result$`Pr(>Chi)`[-1] > 0.05)){      
    return('Prediction makes no sense')}    
  return(rownames(result)[-1] [result$`Pr(>Chi)`[-1] < 0.05])  
}