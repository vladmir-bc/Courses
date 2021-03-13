df <- mtcars
# сделаем, чтобы номинативные переменные были факторами 
# (тип двигател€: v-образный или s-образный)
df$vs <- factor(df$vs , labels = c("V", "S"))  # labels - названи€ уровней фактора
df$am <- factor(df$am , labels = c("Automatic", "Manual"))  # автоматическа€ или ручна€ коробка передач

library(ggplot2)

ggplot(df, aes(x = mpg)) + # в aes отображаетс€, какие перменные будут отображены на графике и каким образом
  geom_histogram(fill = "white", col = "black", binwidth = 2) # указываем слой (что будет отображатьс€ на графике)

ggplot(df, aes(x = mpg, fill = am)) + # построим dotplot. «аполним кружочки в зависимости от типа коробки передач
  geom_dotplot()

ggplot(df, aes(x = mpg)) + # построим функцию плотности
  geom_density(fill = "red")

ggplot(df, aes(x = mpg, fill = am)) + # построим функцию плотности в зависимости от типа коробки передач
  geom_density(alpha = 0.5)  # alpha определ€ет прозрачность слоев
