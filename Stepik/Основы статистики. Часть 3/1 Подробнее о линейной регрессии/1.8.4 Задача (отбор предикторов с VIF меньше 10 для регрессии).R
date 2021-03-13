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

mtcars[, VIF(mtcars)>10]

mtcars[, -"mpg"]

mtcars[,VIF(mtcars) < 10]

names(VIF(mtcars))
names(VIF(mtcars) < 10)
mtcars[VIF(mtcars) > 10]

str(VIF(mtcars))

vif_n <- VIF(mtcars)
names(vif_n['cyl'])
mtcars[names(vif_n['cyl'])]
length(vif_n)

new_data
for (i in 1:length(vif_n)){
  if (vif_n[i] < 10){
      nms <- c(names(vif_n[i]))
    }
  else{
    NA
  }
}
n <- as.vector(unlist(VIF(mtcars)))
mtcars[VIF(mtcars) < 10]
ifelse(VIF(mtcars) < 10, names(VIF(mtcars)), NA)
length((VIF(mtcars) < 1000))
which.max(VIF(mtcars))
mtcars[, -(as.vector(which.max(VIF(mtcars))) + 1)]
m <- c()
m <- c(as.vector(VIF(mtcars) < 10), m)
m <- c(FALSE, m)
length(mtcars)
mtcars[m]
df <- mtcars
df_new <- mtcars[m]
ft <- lm(df[, 1] ~ ., df_new)
summary(ft)$coefficients
all(as.vector(VIF(mtcars) < 10))


fit <- lm(mpg ~ hp + drat + wt + qsec + vs + am + gear + carb, mtcars)
summary(fit)$coefficients


str(summary(fit))
