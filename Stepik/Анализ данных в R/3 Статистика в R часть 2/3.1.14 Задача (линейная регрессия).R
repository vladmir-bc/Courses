
regr.calc <- function(x){
  if (cor.test(x = x[, 1], y = x[, 2])$p.value < 0.05){
    ft <- lm(x[, 1] ~ x[, 2], x)
    x$fit <- ft$fitted.values
    return(x)
  } else {
    return("There is no sense in prediction")
  }
}

?lm

my_df = iris[,1:2] # на вход подаем данные iris только с переменными Sepal.Length и Sepal.Width
regr.calc(iris[,1:2]) # переменные значимо не коррелируют 
my_df = iris[,c(1,4)] # на вход подаем данные iris только с переменными Sepal.Length и Petal.Width
regr.calc(my_df) # переменные значимо коррелируют 