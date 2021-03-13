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

