library(ggplot2)
library(dplyr)
library(lmtest) # тест Бройша-Пагана

diamonds_2 <- sample_n(diamonds, 500)  # взять первые 500 строк из набора данных

qplot(x = price, y = carat, data = diamonds_2) + 
  geom_smooth(method = lm)
# очевидна нелинейная взаимосвязь + 
# проблема гетероскедастичности (непостоянство
# изменчивости ошибки)


fit1 <- lm(carat ~ price, diamonds_2)
coefficients(fit1)
# коэффициенты говорят о том, что в среднем, при увеличении на 1
# цены, число карат увеличивается на 0,0001, но эта интерпретация неверна

# изобразим остатки модели, чтобы проверить на гетероскедастичность
# в случаях нескольких предикторов

plot(fit1)

# разберем пример логорифмической трансформации
# нарисуем логарифмическую трансформацию исходных данных
qplot(x = log(price), y = log(carat), data = diamonds_2) + 
  geom_smooth(method = lm)
# ситуация улучшилась, есть линейность данных, а проблема гетероскедастичности вроде решена

bptest(lm(price ~ carat, diamonds_2)) # p.value < 0.05
bptest(lm(log(price) ~ log(carat), diamonds_2)) # p.value > 0.05

fit2 <- lm(log(carat) ~ log(price), diamonds_2)
shapiro.test(fit2$residuals)
