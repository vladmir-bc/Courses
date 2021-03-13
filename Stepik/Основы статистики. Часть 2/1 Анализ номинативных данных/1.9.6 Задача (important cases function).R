get_important_cases <- function(x){
  m <- length(x)
  for (i in 1:nrow(x)){
    counter <- 0
    for (j in 1:ncol(x)){
      if (is.numeric(x[,j])){
        if (x[i, j] > mean(x[, j])){
          counter = counter + 1
        }
      }
    }
    if (counter > (m)/2){
      x$important_cases[i] <- "Yes"
    } else {
      x$important_cases[i] <- "No"
    }
  }
  x$important_cases <- factor(x$important_cases, levels = c("Yes", "No"))
  return(x)
}

test_data <- data.frame(V1 = c(16, 21, 18), 
                        V2 = c(17, 7, 16), 
                        V3 = c(25, 23, 27), 
                        V4 = c(20, 22, 18), 
                        V5 = c(16, 17, 19))

get_important_cases(test_data)


test_data <- as.data.frame(list(V1 = c(13, 31, 21, 19, 21, 12), V2 = c(15, 15, 15, 21, 12, 23), V3 = c(25, 21, 10, 23, 32, 14), V4 = c(14, 16, 12, 26, 27, 9), V5 = c(20, 16, 14, 15, 24, 18), V6 = c(31, 23, 26, 24, 10, 21)))
get_important_cases(test_data)
mean(test_data[,6])
