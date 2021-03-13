VIF <-  function(df){
  df <- df[-1]
  for (i in 1:ncol(df)) {
    df_new <- df[-i]
    fit <- lm(df[, i] ~ ., df_new)
    if (i == 1){
      nms <- c(names(df[i]))
      vf <- c(1/(1 - (summary(fit)$r.squared)))
    }else{
      nms <- c(nms, names(df[i]))
      vf <- c(vf, 1/(1 - (summary(fit)$r.squared)))
    }
  }
  new_data <- vf
  names(new_data) <- nms
  return(new_data)
}

VIF(mtcars)
