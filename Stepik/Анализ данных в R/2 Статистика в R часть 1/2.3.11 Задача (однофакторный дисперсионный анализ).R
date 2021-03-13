#########################################################################
library(ggplot2)
df <- iris
ggplot(df, aes(x = Species, y = Sepal.Width))+
  geom_boxplot()
fit <- aov(Sepal.Width ~ Species, data = df)
summary(fit)
TukeyHSD(fit)
