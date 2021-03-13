#########################################################################################
library(dplyr)
library(ggplot2)
library(vcd)

# Считаем данные
titanic <- read.csv("https://stepic.org/media/attachments/course/524/train.csv")
titanic <- na.omit(titanic)
glimpse(titanic)
titanic <- mutate(titanic, 
                  Survived = factor(Survived, labels = c("No", "Yes")), 
                  Pclass = factor(Pclass, labels = c("First", "Second", "Third")), 
                  Sex = factor(Sex, labels = c("Female", "Male")))

# Построим мозаичный график
mosaic(~ Sex + Survived | Pclass, data=titanic) 

# Модель без предикторов (Intercept only model)
simple_fit <- glm(Survived ~ 1, titanic, family = "binomial")  # 1 показывает, что у нас только интерсепт. Построим модель
coef(simple_fit)  # показывает коэффициент у модели
table(titanic$Survived)  # таблица сопряженности по выжившим и погибшим. Показывает распределение частот
odds <- 290 / 424  # рассчитываем шанс, что случайно взятый пассажир выживет
# шанс меньше 1, это означает, что вероятность положительного исхода меньше, чем отрицательного
log(odds) # -0.3798525
exp(-0.3798525) # это и есть шансы, рассчитанные в модели (290/424)
summary(simple_fit)

#########################################################################################

# Модель с одним номинативным предиктором
fit1 <- glm(Survived ~ Sex, titanic, family = "binomial")  # Теперь добавим в качестве предиктора пол
coef(fit1)
table(titanic$Survived, titanic$Sex)  # построим табл. сопряженности м/у полом и тем, выжил человек или нет

odds_male <- 93 / 360  # рассчитаем шанс выжить для мужчин < 1
odds_female <- 197 / 64  # рассчитаем шанс выжить для женщин > 1

log(odds_female)  # рассчитаем логарифм шансов для женщин
log(odds_male)  # рассчитаем логарифм шансов для мужчин

odds_ratio <- odds_male / odds_female  # отношение шансов выжить для мужчин к шансам выжить женщинам
# шанс выжить мужчине существенно ниже, чем шанс выжить женщине
log(odds_ratio)  # логарифм отношения шансов или же значение при НП переменной в нашей модели (SexMale)
#########################################################################################


