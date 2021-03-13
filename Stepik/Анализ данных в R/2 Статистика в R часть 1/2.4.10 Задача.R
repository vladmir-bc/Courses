filtered.sum <- function(x){
  return(sum(x[x > 0], na.rm = T))
}

filtered.sum(c(1, -2, 3, NA, NA))
