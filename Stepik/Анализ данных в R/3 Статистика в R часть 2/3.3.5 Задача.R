

?attitude
?step
model_full <- lm(rating ~ ., data = attitude) 

model_null <- lm(rating ~ 1, data = attitude)

ideal_model <- step(object = model_null, scope = list(lower = model_null, upper = model_full), direction = "forward")

anova(model_full, ideal_model)
