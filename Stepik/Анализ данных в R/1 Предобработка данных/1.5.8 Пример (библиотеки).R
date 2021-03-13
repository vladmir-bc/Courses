df <- mtcars
df$vs <- factor(df$vs, labels = c("V", "S"))
df$am <- factor(df$am, labels = c("Auto", "Manual"))

library(psych)  # импортируем бибилиотеку

?describe

describe(x = df)  # будут предупреждения связанные с номинативными переменными, для них статистики не могут быть рассчитаны
descr <- describe(x = df[, -c(8, 9)])  # убрали номинативные переменные
