test_data <- read.csv("https://stepic.org/media/attachments/course/524/cluster_1.csv")
test_data <- read.csv("https://stepic.org/media/attachments/course/524/cluster_2.csv")


smart_hclust<-  function(test_data, cluster_number){
  dist_matrix <- dist(test_data)
  fit <- hclust(dist_matrix)
  cluster <- cutree(fit, cluster_number)
  test_data$cluster <- as.factor(as.vector(cluster))
  return(test_data)
}


get_difference<-  function(test_data, n_cluster){
  test_data <- smart_hclust(test_data, n_cluster)
  result <- sapply(test_data[sapply(test_data, is.numeric)], function(x) anova(aov(x ~ cluster, test_data))$P[1])
  return(names(which(result < 0.05)))
}

get_difference(test_data, 2)
