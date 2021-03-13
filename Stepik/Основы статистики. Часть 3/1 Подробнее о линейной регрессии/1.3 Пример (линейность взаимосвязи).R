library(ggplot2)

qplot(x = hp, y = mpg, data = mtcars)
qplot(x = hp^0.5, y = mpg, data = mtcars)
qplot(x = hp^-0.5, y = mpg, data = mtcars)
qplot(x = -hp^-0.5, y = mpg, data = mtcars)

fit1 <- lm(mpg ~ hp, mtcars)
fit2 <- lm(mpg ~ I(-hp^-0.7), mtcars)

summary(fit1)
summary(fit2)
