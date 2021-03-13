library(ggplot2)
ToothGrowth$dose <- as.factor(ToothGrowth$dose)
obj <- ggplot(data = ToothGrowth, aes(x = supp, y = len, fill = dose))+
  geom_boxplot()
