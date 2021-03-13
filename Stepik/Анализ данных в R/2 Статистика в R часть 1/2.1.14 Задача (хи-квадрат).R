library(ggplot2)
diamonds$factor_price <- factor(diamonds$price >= mean(diamonds$price), labels = c(0, 1))
diamonds$factor_carat <- factor(diamonds$carat >= mean(diamonds$carat), labels = c(0, 1))
main_stat <- chisq.test(diamonds$factor_price, diamonds$factor_carat)$statistic
