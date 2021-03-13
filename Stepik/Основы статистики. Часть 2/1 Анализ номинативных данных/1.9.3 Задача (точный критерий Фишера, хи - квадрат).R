y <- table(mtcars[1:20, c("am", "vs")])
test_data <- as.data.frame(list(am = c(1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1), vs = c(0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1)))
test <- table(test_data)


smart_test <-  function(x){
  x <- table(x)
  if (length(x[x < 5]) == 0){
    return(c(chisq.test(x)$statistic, chisq.test(x)$parameter, chisq.test(x)$p.value))
  }
  else{
    return(fisher.test(x)$p.value)
  }
}

smart_test(test_data)

