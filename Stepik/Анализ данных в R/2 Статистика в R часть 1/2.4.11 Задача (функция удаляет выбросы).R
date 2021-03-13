outliers.rm <- function(vect){
  # put your code here
  vect <- ifelse((vect < (quantile(vect, probs = c(0.25, 0.75))[1]-IQR(vect)*1.5)) | (vect > (quantile(vect, probs = c(0.25, 0.75))[2]+IQR(vect)*1.5)), NA, vect)
  vect <- vect[!is.na(vect)]
  return(vect)
}

outliers.rm(c(2, 2, 3, 4, 5, 8, 9, 5, 6, 7, 8, 20, -20, 19, -19,13,-13))

# Пример правильного решения студентки курса Евгении Головиной stepic.org/users/17517:    
  
outliers.rm <- function(x){    
  q <- quantile(x, 0.25) + quantile(x, 0.75)    
  return(x[abs(x - q/2) <= 2*IQR(x)])}
