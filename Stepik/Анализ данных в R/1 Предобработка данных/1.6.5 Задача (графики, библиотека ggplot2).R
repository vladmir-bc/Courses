library(ggplot2)
df <- airquality
df$Month <- factor(df$Month)  # Обратите внимание, что для корректного отображения графика ggplot ожидает факторную переменную по оси x.
ggplot(subset(df, Month==9), aes(x = Month, y = Ozone))+geom_boxplot()

