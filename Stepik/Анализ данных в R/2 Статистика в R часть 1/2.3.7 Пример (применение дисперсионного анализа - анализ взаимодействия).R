### ANOVA

library(ggplot2)

DV ~ IV  # таким образом можно указать взаимосвязь м/у зависимой и независимой переменными

DV ~ IV1 + IV2  # так можно указать, что на независимую переменную влияют 2 зависимых

DV ~ IV1:IV2  # : используется для указания взаимодейтсвий, т.е. когда влияние одной переменной на другую зависит от уровня 3 переменной

DV ~ IV1 + IV2 + IV1:IV2  # формула с главными эффектами + взаимодействие

DV ~ IV1 * IV2  # предыдущую формулу можно записать через *. Она означает формулу с главными эффектами + взаимодействие

DV ~ (IV1 + IV2 + IV3)^2  # указать, что есть 3 независимых переменных (3 предиктора) и нас интересуют все основные эффекты + взаимодействие до 2 уровня

DV ~ IV1 + Error(subject/IV1)  # повторные измерения для дисп. анализа
#########################################################################

library(ggplot2)
mydata <- read.csv("shops.csv", stringsAsFactors = T)  # сравнение цен на продукты в разных магазинах России

str(mydata)

boxplot(price ~ origin, data = mydata)  # взаимосвязь м/у зависимой и независимой переменной

ggplot(mydata, aes(x = origin, y = price))+
  geom_boxplot()

fit <- aov(price ~ origin, data = mydata)  # используется, чтобы запустить дисперсионный анализ, сравнить группы
summary(fit)  # показывает информацию о различии групп
#########################################################################

# двухфакторный дисперсионный анализ


fit1 <- aov(price ~ origin + store, data = mydata)
summary(fit1)

model.tables(fit1, "means")  # показывает интересующую метрику по таблице (средние)
#########################################################################

pd <- position_dodge(0.1)
ggplot(mydata, aes(x = store, y = price, color = origin, group = origin))+  #group=origin для того, чтобы показать, что в какой группе находиться (более толстые линии на графике)
  stat_summary(fun.data=mean_cl_boot,
               geom='errorbar', width=0.1,
               position=position_dodge(width=0.2)) +  # position=position_dodge(width=0.2) для того, чтобы сместить разделение по магазину с одной линии
  stat_summary(fun.data=mean_cl_boot,
               geom='line', size=1,
               position=position_dodge(width=0.2)) +
  stat_summary(fun.data=mean_cl_boot,
               geom='point', shape='square',
               size=3, position=position_dodge(width=0.2)) +
  theme_bw()  # The classic dark-on-light ggplot2 theme. May work better for presentations displayed with a projector.

fit3 <- aov(price ~ origin*store, data=mydata)  # origin + store + origin:store
summary(fit3)
