library(ggplot2)

smart_hclust<-  function(test_data, cluster_number){
  dist_matrix <- dist(test_data)
  fit <- hclust(dist_matrix)
  cluster <- cutree(fit, cluster_number)
  test_data$cluster <- as.factor(as.vector(cluster))
  return(test_data)
}

swiss <- smart_hclust(swiss, 2)
my_plot <- ggplot(swiss, aes(Education, Catholic, col = cluster)) + 
  geom_smooth(method = lm) + 
  geom_point()

# Пример правильного решения:    
  
dist_matrix <- dist(swiss)    
fit <- hclust(dist_matrix)     
swiss$cluster <- as.factor(cutree(fit, 2))    
my_plot <- ggplot(swiss, aes(Education, Catholic, col = cluster)) +      
  geom_point() +      
  geom_smooth(method = 'lm')

