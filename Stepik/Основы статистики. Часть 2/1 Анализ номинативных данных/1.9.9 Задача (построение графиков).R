library(ggplot2)

df <- diamonds

obj <- ggplot(df, aes(x = color, fill=cut)) + 
  geom_bar(position="dodge", stat="count")


#Пример правильного решения:

obj <- ggplot(diamonds, aes(x=color, fill=cut)) +
  geom_bar(position='dodge')