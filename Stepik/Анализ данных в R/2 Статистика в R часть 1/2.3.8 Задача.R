mydata <- data.frame(npk)
str(mydata)
fit1 <- aov(yield ~ N*P, data = mydata)
summary(fit1)
