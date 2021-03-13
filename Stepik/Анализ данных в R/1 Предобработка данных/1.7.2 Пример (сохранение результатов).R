df <- mtcars
str(df)
library(ggplot2)
library(psych)


mean_mpg <- mean(df$mpg)

descr_df <- describe(df[, -c(8,9)])

boxplot <- ggplot(df, aes(x=factor(am), y=disp))+
  geom_boxplot()+
  xlab("Transmission")+
  ylab("Displacement (cu.in)")+
  ggtitle("Box - plot")

# Сохранение данных: в начало скрипта можно вставить:

setwd("~/R/Projects/Анализ данных в R/1 Предобработка данных")

# можно данные mtcars сохранить в виде csv файла
write.csv(df, "df.csv")

# расчеты блольших значений также можно сохранить отдельно:
my_mean <- mean(10^6:10^9)
save(my_mean, file = "my_mean.RData")
