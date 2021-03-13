library(boot)


slope_cl_boot <- function(df){
  fc <- function(d, i){
    d2 <- d[i,]
    fit <- lm(d2[, 2] ~ d2[, 1], d2)
    return(coefficients(fit))
  }
  
  results <- boot(df, fc, R=1000)
  boot.ci(results, type="basic", index = 2)$basic[c(4,5)]
}

slope_cl_boot(cars)