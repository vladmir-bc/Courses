library(dplyr)
library(ggplot2)


set.seed(42)

d <- data_frame(y = rnorm(30),
                x_1 = rnorm(30),
                x_2 = x_1,
                x_3 = rnorm(30))


# нарисуем скаттер плот
pairs(d)



# проанализируем модель, которая содержит мультиколлинеарность
# x_1 == x_2
fit <- lm(y ~ ., d)
summary(fit)
x <- c(1, 2, -5, -10, -19, 9, -183, -11, 18, 195, 65)
y <- abs(x)

cor.test(x = x, y = y)


# интересный самостоятельный пример:

happiness <- c(5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90)
statistic <- c(8, 12, 13, 18, 29, 30, 36, 39, 41, 55, 56, 65, 67, 75, 75, 79, 89, 100)
salary <- c(2500, 2750, 2800, 2800,  2850, 2900, 3150, 3256, 3200,  3390, 3450,  3685,  3700, 3800, 4200, 4345, 4500, 4900)
df <- data.frame(happiness = happiness, statistic = statistic, salary = salary)

fit <- anova(aov(happiness ~ statistic, df))
fit1 <- lm(happiness ~ statistic, df)
fit2 <- lm(happiness ~ salary, df)
fit3 <- lm(happiness ~ statistic + salary, df)
fit4 <- lm(happiness ~ statistic * salary, df)
summary(fit4)

ggplot(df, aes(x = salary, y = happiness)) + 
  geom_point() + 
  geom_smooth(method = 'lm')




cor.test(x = salary, y = happiness)
rnorm(30, mean = 2500, sd = 500)
aov()