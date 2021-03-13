library(ggplot2)

bad_var_estimator <- function(x) {  # создали функцию, которая считает плохую оценку дисперсии
  n <- length(x)
  return(var(x)*(n-1)/n)  # испортили множителем дисперсию, чуть менее 1
}

JN_bias_correction <- function(x, estimator){  # функция осуществляет коррекцию смещения
  # по методу jackknife
  n <- length(x)
  theta_stars <- vector("numeric",n)
  ind <- c(1:n)
  
  for(i in ind) {
    sample <- x[ind != i]
    theta_stars[i] <- estimator(sample)
  }
  
  theta_hat <- estimator(x)
  theta_dot <- mean(theta_stars)
  
  bias_jack <- (theta_dot - theta_hat)*(n-1)
  theta_hat_jack <- theta_hat - bias_jack
  return(theta_hat_jack)
}
start <- 3

sample_sizes <- c(start:50)
test <- 100

results_good <- sample_sizes
results_bad <- sample_sizes
results_corrected <- sample_sizes

for (n in sample_sizes){
  samples <- matrix (rnorm(n*test), n)
  
  good_estimations <- apply (samples, 2, var)
  bad_estimations <- apply (samples, 2, bad_var_estimator)
  corrected_estimations <- apply(samples, 2, JN_bias_correction, estimator = bad_var_estimator)
  
  results_good[n-start+1] <- mean(good_estimations)
  results_bad[n-start+1] <- mean(bad_estimations)
  results_corrected[n-start+1] <- mean(corrected_estimations)
}

df <- data.frame(x = rep(sample_sizes,3),
                 y = c(results_good,results_bad, results_corrected),
                 gr = factor(rep(1:3, each = length(sample_sizes)),
                             labels = c("results_good","results_bad","results_corrected")))

ggplot(df, aes(x, y, col = gr))+
  geom_jitter()