
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

my_df = iris[,1:2] # �� ���� ������ ������ iris ������ � ����������� Sepal.Length � Sepal.Width
regr.calc(iris[,1:2]) # ���������� ������� �� ����������� 
my_df = iris[,c(1,4)] # �� ���� ������ ������ iris ������ � ����������� Sepal.Length � Petal.Width
regr.calc(my_df) # ���������� ������� ����������� 