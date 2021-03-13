NA.position1 <- function(x){
  which(is.na(x))
}

NA.position2 <- function(x){
  for (i in 1:length(x)){
    if (is.na(x[i])){
      print(i)
    }
  }
}

my_vector <- c(1, 2, 3, NA, NA)
NA.position1(my_vector)
NA.position2(my_vector)
