normality_test <- function(df){
  return(unlist(sapply(df[sapply(df, is.numeric)], shapiro.test)['p.value',]))
}

normality_test(iris)
test <- read.csv("https://stepic.org/media/attachments/course/524/test.csv")
normality_test(test)
