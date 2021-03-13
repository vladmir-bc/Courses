df <- mtcars
# сделаем, чтобы номинативные переменные были факторами 
# (тип двигателя: v-образный или s-образный)
df$vs <- factor(df$vs , labels = c("V", "S"))  # labels - названия уровней фактора
df$am <- factor(df$am , labels = c("Automatic", "Manual"))  # автоматическая или ручная коробка передач

library(ggplot2)

ggplot(df, aes(x = am, y = hp))+
  geom_boxplot(aes(group=am))

ggplot(df, aes(x = mpg, y = hp, col=vs))+
  geom_point(size = 3)  # увеличим размер точек

ggplot(df, aes(x = mpg, y = hp, col=vs, size = qsec))+  # теперь размер точек зависит от времени разгона
  geom_point()

# В отличие от базовой графики мы можем сохранять результаты построения графиков в одну перемнную
my_plot <- ggplot(df, aes(x = mpg, y = hp, col=vs, size = qsec))+  # теперь размер точек зависит от времени разгона
  geom_point()

my_plot2 <- ggplot(df, aes(x = am, y = hp, col=vs))  # можем сделать заготовку
my_plot2 + geom_boxplot()
