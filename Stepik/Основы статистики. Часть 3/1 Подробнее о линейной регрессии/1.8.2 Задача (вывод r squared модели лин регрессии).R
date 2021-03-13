
hetero_test <-  function(df){
  cols <- ncol(df)
  df2 <- df[, 2:cols]
  fit <- lm(df[, 1] ~ ., df2)
  fit2 <- lm(fit$residuals^2 ~ ., df2)
  return(summary(fit2)$r.squared)
}
hetero_test(mtcars)
