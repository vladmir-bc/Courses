smart_hclust<-  function(test_data, cluster_number){
  dist_matrix <- dist(test_data)
  fit <- hclust(dist_matrix)
  cluster <- cutree(fit, cluster_number)
  test_data$cluster <- as.factor(as.vector(cluster))
  return(test_data)
}
test_data <- read.csv("https://stepic.org/media/attachments/course/524/test_data_hclust.csv")
smart_hclust(test_data, 3)
