
beta.coef <- function(x){
  fit <- lm(scale(x[, 1]) ~ scale(x[, 2]), data = x)$coefficients
  return(fit)
}

beta.coef(mtcars[,c(1,3)])
beta.coef(swiss[,c(1,4)])
