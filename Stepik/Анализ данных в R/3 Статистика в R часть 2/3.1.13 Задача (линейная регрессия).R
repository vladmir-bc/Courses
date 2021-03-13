library(ggplot2)
diamonds
df <- subset(diamonds, cut == "Ideal" & carat == 0.46)
fit <- lm(price ~ depth, df)
fit_coef <- fit$coefficients # коэффициенты модели
