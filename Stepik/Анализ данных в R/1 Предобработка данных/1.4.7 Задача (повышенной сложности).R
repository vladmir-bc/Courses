# 1 решение
a <- as.vector(AirPassengers)
moving_average <- numeric(135)
for (i in 1:length(moving_average)){
  moving_average[i] <- mean(a[i:(i+9)])
}
moving_average

# 2 решение - без циклов

n <- 10    
d <- AirPassengers   
cx <- c(0, cumsum(d))    
moving_average <- (cx[(n + 1):length(cx)] - cx[1:(length(cx) - n)]) / n
