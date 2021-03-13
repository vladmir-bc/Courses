fill_na <- function(x){
  fit <- glm(x[, 1] ~ x[, 4] * x[, 3], data = x, family = 'binomial')
  x$y_full <- predict(fit, df, type = 'response')
  x$y_full <- ifelse(is.na(x$admit), x$y_full, 0)
  m <- subset(df[, 1], is.na(df$admit) == FALSE)
  x$y_full2 <- factor(ifelse(x$y_full >= 0.4, 1, 0), labels = c("N", "Y"))
  return(length(subset(x[, 6], x$y_full2 == 'Y')))
}
fill_na(df)
