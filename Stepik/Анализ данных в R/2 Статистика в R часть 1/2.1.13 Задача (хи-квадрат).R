library(ggplot2)
main_stat <- chisq.test(diamonds$cut, diamonds$color)$statistic
