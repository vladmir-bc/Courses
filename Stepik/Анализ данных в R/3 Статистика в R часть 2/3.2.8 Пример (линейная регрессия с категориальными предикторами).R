
###############################################################
# Рассмотрим линейную регрессию с категориальными предикторами

# cathegorial predictors

hist(swiss$Catholic, col = 'red')

# создадим категориальные переменные

swiss$religious <- ifelse(swiss$Catholic > 60, 'Lots', 'Few') # если число католиков > 60%, то в переменную добавляется значение Lots
swiss$religious <- as.factor(swiss$religious)
fit3 <- lm(Fertility ~ Examination + religious, data = swiss)
summary(fit3)  # intercept включает в себя среднее предсказанное значение рождаемости
# для провинций, где у нас мало католкиов (religious = few). А непрерывные переменные (числовые) = 0

# создадим модель, которая включает взаимодейтсвие категориальных и непрерывных переменных (данная модель бывает проблематичной)
fit4 <- lm(Fertility ~ Examination * religious, data = swiss)
summary(fit4) # в интерсепте по-прежнему хранится значение для religious few
# religiousLots не значим
# но взаимодействие факторов на уровне тенденции - близко к значимому


