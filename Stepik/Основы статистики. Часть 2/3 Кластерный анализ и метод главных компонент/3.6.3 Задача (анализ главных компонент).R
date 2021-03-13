test_data <- read.csv("https://stepic.org/media/attachments/course/524/pca_test.csv")

get_pc <- function(d){
  d <- cbind(d, prcomp(d)$x[, c(1, 2)])
  return(d)
}
get_pc(test_data)
