
high.corr <- function(d){
  d <- abs(cor(d))
  d[lower.tri(d)] <- 0
  diag(d) <- 0
  index <- which(d == max(d), arr.ind = T)
  return(rownames(d)[index])
}
high.corr(swiss)
high.corr(iris[,-5])

# Пример правильного решения студента Артема Капылова stepic.org/users/16368599:    

high.corr <- function(x){    
  cr <- cor(x)    
  diag(cr) <- 0    
  return(rownames(which(abs(cr)==max(abs(cr)),arr.ind=T)))}