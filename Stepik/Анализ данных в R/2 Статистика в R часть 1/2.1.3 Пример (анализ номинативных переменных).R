# Categorical data

df <- read.csv("grants.csv")

str(df)  # структура данных

df$status <- as.factor(df$status)  # 1 способ представить данные в типе "фактор"
levels(df$status) <- c("Not funded", "Funded")  # позвол€ет увидеть уровни фактора

df$status <- factor(df$status, labels = c("Not funded", "Funded"))  # 2 способ сделать факторную переменную

# другой пример

set.seed(124)
schtyp <- sample(0:1, 20, replace = TRUE)
schtyp
is.factor(schtyp)  # False
is.numeric(schtyp)  # True
schtyp.f <- factor(schtyp, labels = c("private", "public"))
schtyp.f
## Levels: private public
is.factor(schtyp.f)  # True

# —генерируем значени€-строки, назовем ses (социально-экономический статус)
ses <- c("low", "middle", "low", "low", "low", "low", "middle", "low", "middle",
         "middle", "middle", "middle", "middle", "high", "high", "low", "middle",
         "middle", "low", "high")

is.factor(ses)  # FALSE
is.character(ses)  # TRUE

# Creating a factor variable ses.f.bad.order based on ses.
ses.f.bad.order <- factor(ses)
is.factor(ses.f.bad.order)  # TRUE
levels(ses.f.bad.order)  ## [1] "high"   "low"    "middle"
#  сделав так, мы по факту переименуем уровни high в low, low в middle, middle в high, т.е. вместо изменени€ реального пор€дка уровней, мы прицепили новые €рлыки (наименовани€, лэйблы) старым уровн€м и значени€м и хот€ пор€док новых уровней стал таким, как мы хотели, но данные уже не исходные, а перепутанные, что недопустимо

# если делать через levels:
ses.lev <- factor(ses, levels = c("low", "middle", "high"))
ses
