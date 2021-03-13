library(ggplot2)

ggplot(iris, aes(Sepal.Length, Petal.Length, color = Species)) + 
  geom_point()

# пример кластеризации


d <- iris[, c("Sepal.Length", "Petal.Width")]

fit <- kmeans(d, 3)
d$clusters <- factor(fit$cluster)

ggplot(d, aes(Sepal.Length, Petal.Width, col = clusters))+
  geom_point(size = 2)+
  theme_bw() 

# еще один способ

library(ggplot2)
library(factoextra)
theme_set(theme_minimal())
d <- iris[, c("Sepal.Length", "Petal.Width")]
fit <- kmeans(d, 3)
fviz_cluster(fit, d)

# еще один способ


library("cluster")
KM <- kmeans(iris[1:4], 3, iter.max = 1000, algorithm = "Hartigan-Wong")
clusplot(iris[1:4], KM$cluster, color = TRUE, 
         shade = TRUE, labels=2,
         main = 'Cluster Analysis for Iris')

#  ћожно дл€ определени€ оптимального числа кластеров воспользоватьс€ пакетом NbClust:
  
library(NbClust)
data(iris)
dt <- iris[, 1:4]
N <- NbClust(dt, distance = "euclidean",
             min.nc = 2, max.nc = 15, method = "complete", 
             index = "alllong")

# ѕосчитаем сумму квадратов в кластере

sum((c(-3,1,2,3,5,6,7)-3)^2+(c(1,2,3,4,6,8,11)-5)^2)
