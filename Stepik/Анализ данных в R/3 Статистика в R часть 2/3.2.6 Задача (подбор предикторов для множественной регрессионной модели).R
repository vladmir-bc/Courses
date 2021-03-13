
mtcars
df <- mtcars[, c(1, 3:6)]
fit <- lm(wt ~ mpg + disp + hp, data = df)
summary(fit)
df$pred <- predict(fit, df)

library(PerformanceAnalytics)
chart.Correlation(df)
