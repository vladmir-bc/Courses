df <- mtcars
result <- mean(df$qsec[df$cyl != 3 & df$mpg > 20])
