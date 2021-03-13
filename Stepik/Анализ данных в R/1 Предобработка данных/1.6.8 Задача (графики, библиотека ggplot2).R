df <- iris
plot1 <- ggplot(df, aes(x=Sepal.Length, y=Sepal.Width, col = Species))+
  geom_point(aes(size=Petal.Length))
