my_calc <- function(x, y){
  s <- x + y
  return(s)
}

result <- my_calc(10, 15)

s <- 100

my_calc <- function(x, y){
  s <- x + y
  d <- x - y
  return(c(s, d))
}

my_calc(10, 15)

my_calc2 <- function(x, y, z){
  s <- x + y + z
  d <- x - y - z
  return(c(s, d))
}

my_calc2(1, 2, 3)
