stat_mode <- function(x){
  k <- names(which(table(x) == max(table(x))))
  return(as(k, "integer"))
}


v <- c(1, 2, 3, 3, 3, 4, 5)
stat_mode(v)

v <- c(1, 1, 1, 2, 3, 3, 3)
stat_mode(v)