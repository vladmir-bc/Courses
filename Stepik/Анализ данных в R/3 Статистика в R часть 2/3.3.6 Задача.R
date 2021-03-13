LifeCycleSavings
model <- lm(sr ~ (pop15 + pop75 + dpi + ddpi)^2, data = LifeCycleSavings)
summary(model)
