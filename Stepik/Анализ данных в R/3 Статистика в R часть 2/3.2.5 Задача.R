
?predict

test_data <- read.csv("https://stepic.org/media/attachments/course/129/fill_na_test.csv")
str(test_data)
fit <- lm(test_data[, 3] ~ test_data[, 1] + test_data[, 2], data = test_data)
summary(fit)
test_data$y_full <- predict(fit, test_data)
test_data$y_full <- ifelse(is.na(test_data$y), test_data$y_full, test_data$y)

fill_na <- function(x){
  fit <- lm(x[, 3] ~ x[, 1] + x[, 2], data = x)
  x$y_full <- predict(fit, test_data)
  x$y_full <- ifelse(is.na(x$y), x$y_full, x$y)
  return(x)
}

fill_na(test_data)

