my_vector <- c(1, 2, 3, NA, NA)

NA.counter <- function(x){
  return(sum(is.na(x)))
}

NA.counter(my_vector)
