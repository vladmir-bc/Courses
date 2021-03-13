df <- mtcars
df$vs <- factor(df$vs, labels = c("V", "S"))
df$am <- factor(df$am, labels = c("Auto", "Manual"))

library(psych)  # импортируем бибилиотеку

?describe

describe(x = df)  # будут предупреждения связанные с номинативными переменными, для них статистики не могут быть рассчитаны
descr <- describe(x = df[, -c(8, 9)])  # убрали номинативные переменные

?describeBy()  # описательные статистики, расчитанные по группам

descr2 <- describeBy(x = df[, -c(8, 9)], group = df$vs)  # рассчитывает описательные статистики для групп (по типу двигателя)
descr2$V  # вывести данные только для V-образного двигателя
descr2$S  # вывести данные только для S-образного двигателя


descr2 <- describeBy(x = df[, -c(8, 9)], group = df$vs, mat = T, digits = 1)  # преобразовали в dataframe с одним знаком после запятой

descr3 <- describeBy(x = df[, -c(8, 9)], group = df$vs, mat = T, digits = 1, fast = T)  # по сравнению с предыдущим вариантом рассчитываются базовые вещи

describeBy(df$qsec, group = list(df$vs, df$am), mat = T, digits = 1,
           fast = T)  # можем разбить наблюдения сразу по двум переменным (по типу двигателя и коробке передач)
