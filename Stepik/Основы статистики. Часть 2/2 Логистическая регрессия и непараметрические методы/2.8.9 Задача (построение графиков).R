library(ggplot2)

ggplot(data = iris, aes(Sepal.Length, fill = Species))+
  geom_density(alpha = 0.2)
  