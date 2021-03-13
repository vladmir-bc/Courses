# my_vector <- c(20.67, 23.34, 22.65, 17.11, 22.1, 26.32, 20.39, 21.04, 23.78, 31.11, 21.13, 22.44, 23.21)

for (i in 1:length(my_vector)){
  if (mean(my_vector) > 20){
    result <- "My mean is great"
  } else {
    result <- "My mean is not so great"
  }
}
