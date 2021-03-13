# Чтобы построить столбчатую диаграмму в ggplot, вам нужно подключить нужный пакет, 
# затем преобразовать таблицу HairEyeColor в data frame
library(ggplot2)
mydata <- subset(as.data.frame(HairEyeColor), Sex == 'Female')
obj <- ggplot(data = mydata, aes(x = Hair, y = Freq, fill = Eye)) +
  geom_bar(stat="identity", position=position_dodge()) +
  scale_fill_manual(values=c("Brown", "Blue", "Darkgrey", "Darkgreen"))
