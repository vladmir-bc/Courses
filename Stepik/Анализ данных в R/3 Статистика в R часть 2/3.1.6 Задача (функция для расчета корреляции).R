
library(psych)
filtered.cor <- function(x){
  x_num <- x[, sapply(x, is.numeric)]
  fit <- corr.test(x_num)
  diag(fit$r) <- 0
  return(fit$r[which((abs(fit$r) == max(abs(fit$r))))][1]) 
}
filtered.cor(mtcars)
step6 <-  read.table("step6.csv",  header=TRUE, sep=',' )
filtered.cor(step6)
test_data <- as.data.frame(list(V8 = c("q", "q", "q", "q", "q", "q", "q", "q"), V5 = c(-1.1, -0.7, -0.6, -0.4, -0.1, 1.1, 0.7, -0.6), V6 = c(1.1, 0.7, 0.6, 0.4, 0.1, -1.1, -0.7, 0.6), V2 = c(-0.6, -0.3, 0.2, 0.1, -0.3, -0.5, -0.2, 0.2), V7 = c("f", "f", "f", "f", "f", "f", "f", "f"), V4 = c(3.1, 0.2, -0.6, -1.5, 0, 1.9, -0.4, -0.3), V3 = c(0.1, -0.4, -0.8, -1, 0, 0.1, -0.4, -0.3), V1 = c(0, -0.2, 0, 0.7, -1.4, 1.3, -1, -0.8)))
test_data
filtered.cor(test_data)