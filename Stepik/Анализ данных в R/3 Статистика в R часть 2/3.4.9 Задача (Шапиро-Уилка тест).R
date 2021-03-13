p.val_shapiro <- function(x){
  return(shapiro.test(x)$p.value)
}


normality.test  <- function(x){
  return(unlist(sapply(x, p.val_shapiro)))
}
normality.test(mtcars[,1:6])


# ѕример правильного решени€ студентки Daria Loginova stepic.org/users/18697914    

normality.test  <- function(x){    
  return(sapply(x, FUN =  shapiro.test)['p.value',])}


