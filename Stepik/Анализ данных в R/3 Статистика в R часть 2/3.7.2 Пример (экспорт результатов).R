#######################################################################################
# экспорт результатов

library(xtable)

library(stargazer)

# сделаем простую регрессию

fit1 <- lm(mpg ~ cyl + disp, mtcars)
fit2 <- aov(mpg ~ am + vs, mtcars)

fit_table1 <- xtable(fit1)  # создает специальный объект для регрессионного анализа
fit_table2 <- xtable(fit2)  # создает специальный объект для дисперсионного анализа

print(fit_table1, type="html", file="fit_table1.html")
print(fit_table2, type="html", file="fit_table2.html")

# представим данные более красиво

stargazer(fit1, type = "html",
          dep.var.labels = "mpg",
          covariate.labels = c("cyl","disp"), out = "models1.html")
