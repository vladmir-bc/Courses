test_data <- read.csv("https://stepik.org/media/attachments/course/524/test_data_01.csv")
str(test_data)

test_data  <- transform(test_data, x = factor(x), y = factor(y))
get_coefficients <- function(dataset){
  fit <- glm(dataset[, 2] ~ dataset[, 1], dataset, family = 'binomial')
  return(exp(fit$coefficients))
}

get_coefficients(test_data)
