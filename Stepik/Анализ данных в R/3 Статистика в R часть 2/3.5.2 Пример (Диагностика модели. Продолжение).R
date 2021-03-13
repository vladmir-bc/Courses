########################################################################
# следующее допущение, которое мы рассмотрим - линейность взаимосвязи
# между независимой и зависимой переменными

# Чтобы регрессия работала хорошо, переменные должны быть связаны линейно

# добавим в график линию тренда

library(ggplot2)

ggplot(swiss, aes(x = Examination, y = Education)) + 
  geom_point() + 
  geom_smooth()
# тренд нелинеен

# построим простую линейную модель
lm1 <- lm(Education ~ Examination, swiss)
summary(lm1)
# R^2 составляет 0,4878. p-value значимо

# попробуем построить полиномиальную модель, которая содержит не только один предиктор 1 степени, но и более высокие степени

swiss$Examination_squared <- (swiss$Examination)^2  # возведенное в квадрат значение Examination


lm2 <- lm(Education ~ Examination + Examination_squared, swiss)
summary(lm2)  # Examination - перестала быть значимой, а Examination_squared значимо предсказывает

# проведем тесты на сравнение моделей 
anova(lm2, lm1)  # разница моделей оказалась значимой

# запишем в swiss предсказанные значения

swiss$lm1_fitted <- lm1$fitted
swiss$lm2_fitted <- lm2$fitted
swiss$lm1_resid <- lm1$resid  # остатки
swiss$lm2_resid <- lm2$resid  # остатки
swiss$obs_number <- 1:nrow(swiss)


# построим графики предсказанных значений для наших двух моделей
ggplot(swiss, aes(x = Examination, y = Education)) + 
  geom_point(size = 3) + 
  geom_line(aes(x = Examination, y = lm1_fitted), col = 'red', lwd=1) + 
  geom_line(aes(x = Examination, y = lm2_fitted), col = 'blue', lwd=1)
  
# график, где по оси X идут предсказанные значения, а по оси y идут остатки
# предсказанные значения и остатки для линейной модели:
ggplot(swiss, aes(x = lm1_fitted, y = lm1_resid)) + 
  geom_point(size = 3) + geom_hline(yintercept = 0, col = 'red', lwd = 1)

ggplot(swiss, aes(x = lm2_fitted, y = lm2_resid)) + 
  geom_point(size = 3) + geom_hline(yintercept = 0, col = 'red', lwd = 1)



