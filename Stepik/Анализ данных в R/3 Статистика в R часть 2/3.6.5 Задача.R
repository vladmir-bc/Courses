my_df <- mtcars
str(my_df)
?mtcars
my_df$cyl <- as.factor(my_df$cyl)
my_df$vs <- as.factor(my_df$vs)
my_df$am <- as.factor(my_df$am)
fit <- glm(am ~ disp + vs + mpg, my_df, family = 'binomial')  # вместо lm используется glm
summary(fit)
log_coef <- fit$coefficients
str(mtcars)
