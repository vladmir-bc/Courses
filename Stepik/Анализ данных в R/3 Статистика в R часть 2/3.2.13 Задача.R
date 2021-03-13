

mtcars$am <- factor(mtcars$am, labels = c('Automatic', 'Manual'))
?mtcars
fit <- lm(mpg ~ wt*am, data = mtcars)
summary(fit)
