resid.norm  <- function(fit){
  df <- data.frame(fit$resid)
  if (shapiro.test(fit$residuals)$p.value < 0.05){
    a <- ggplot(df, aes(fit.resid)) + geom_histogram(binwidth = 4, fill = "red")
    return(a)
  } else{
    b <- ggplot(df, aes(fit.resid)) + geom_histogram(binwidth = 4, fill = "green")
    return(b)
  }
}