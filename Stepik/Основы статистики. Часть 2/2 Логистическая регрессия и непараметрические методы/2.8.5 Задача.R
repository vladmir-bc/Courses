test_data <- read.csv("https://stepic.org/media/attachments/course/524/test_data_passangers.csv", stringsAsFactors = T)
str(test_data)

data_for_predict <-read.csv("https://stepic.org/media/attachments/course/524/predict_passangers.csv", stringsAsFactors = T)
str(data_for_predict)


most_suspicious <- function(test_data, data_for_predict){
  fit <- glm(is_prohibited ~., test_data, family = 'binomial')
  data_for_predict$dangerous <- predict(object = fit, newdata = data_for_predict, type = 'response')
  return(data_for_predict[which.max(data_for_predict$dangerous), 5])
}
most_suspicious(test_data, data_for_predict)


# Пример правильного решения:

most_suspicious <- function(test_data, data_for_predict){    
  fit <- glm(is_prohibited ~., test_data, family = 'binomial')    
  probs <- predict(fit, newdata = data_for_predict, type = 'response')    
  index <- which(probs == max(probs))    
  passanger_name <- data_for_predict$passangers[index]    
  return(passanger_name)    
}