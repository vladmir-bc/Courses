
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


test_data  <- read.csv("https://stepik.org/media/attachments/course/129/test_data.csv")
shap1 <- shapiro.test(test_data[, 1])
shap2 <- shapiro.test(test_data[, 2])
if ((shap1$p.value >= 0.05) & (shap2$p.value >= 0.05)){
  
  
  cor.test(x = test_data[, 1], y = test_data[, 2], method = "spearman")$
    statistic
} else {
  cor.test(x = test_data[, 1], y = test_data[, 2])$
    statistic
}

test_data[, 1]
?shapiro.test
?cor.test

test_data  <- read.csv("https://stepik.org/media/attachments/course/129/test_data.csv")

smart_cor <- function(x){
  shap1 <- shapiro.test(x[, 1])
  shap2 <- shapiro.test(x[, 2])
  if ((shap1$p.value >= 0.05) & (shap2$p.value >= 0.05)){
    cor.test(x = x[, 1], y = x[, 2])$estimate
  } else {
    cor.test(x = x[, 1], y = x[, 2], method = "spearman")$estimate
  }
}

str(smart_cor(test_data))
