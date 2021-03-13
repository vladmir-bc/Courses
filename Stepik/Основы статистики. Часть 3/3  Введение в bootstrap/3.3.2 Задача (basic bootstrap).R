median_cl_boot <- function(x){
  med <- median(x)
  f <- c()
  for (i in 1:1000){
    f <- c(f, median(sample(x, 1000, replace = T)) - med)
  }
  f <- sort(f)
  m <- c(f[50], f[950]) + med
  return(m)
}


median_cl_boot(rnorm(1000, 10000))
