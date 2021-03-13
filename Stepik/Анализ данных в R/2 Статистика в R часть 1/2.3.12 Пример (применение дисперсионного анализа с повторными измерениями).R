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

#########################################################################
# в предыдущих примерах всегда было 2 уровня, продукты были либо импортные, либо отечественные
# дисперсионный анализ хорош тем, что в него можно загонть сразу много групп
# каким образом можно осуществить множественные сравнения с поправками на множественные сравнения:
# будем смотреть, как влияют разные типы еды на зависимую переменную - цену продуктов

mydata <- read.csv("shops.csv", stringsAsFactors = T)  # сравнение цен на продукты в разных магазинах России

ggplot(mydata, aes(x = food, y = price))+
  geom_boxplot()

fit5 <- aov(price ~ food, data=mydata)
summary(fit5)  # мы можем сказать, что группы продуктов значимо отличаются по цене, но не можем сказать, какие именно
# для того, чтобы сказать, какие именно группы отличаются, нам надо использовать множественные сравнения

TukeyHSD(fit5)  # критерий Тьюки - позволяет сделать попарные сравнения. Поправка является менее строгой, чем Бонферрони

#########################################################################

# дисперсионный анализ с повторными измерениями. Он необходим, когда наши наблюдения не независимы, а сгруппированы по каким-то переменным.
# например, у нас есть испытемые, каждый из которых проходил несколько тестов. И для учета, что испытуемые между собой различаются, необходимо применять дисперсионный анализ с повторными измерениями

library(ggplot2)

mydata2 <- read.csv("therapy_data.csv", stringsAsFactors = T)
str(mydata2)

mydata2$subject <- as.factor(mydata2$subject)  # испытуемые как фактор
#  построим модели:

fit1 <- aov(well_being ~ therapy, data = mydata2)  # эффект терапии получился не значим
summary(fit1)

# для учета того, что каждый испытуемый проходил три курса психотерапии (3 измерения того, насколько хорошо он себя чувствует)
fit1b <- aov(well_being ~ therapy + Error(subject/therapy), data = mydata2)  # добавляем параметр Error - ошибка, связанная с испытуемым. Группирующий фактор - subject и фактор, влияние которого мы хотим узнать - терапия
summary(fit1b)

fit2 <- aov(well_being ~ therapy*price, data = mydata2)
summary(fit2)  # цена оказалась значимым фактором

ggplot(mydata2, aes(x = price, y = well_being)) + 
  geom_boxplot()

#  построим ту же самую модель с учетом дисперсии, связанной с испытуемыми

fit2b <- aov(well_being ~ therapy*price + Error(subject/(therapy*price)), data = mydata2)
summary(fit2b)  # теперь влияние цены оказалось не значимым фактором, и это корректно

ggplot(mydata2, aes(x = price, y = well_being)) + 
  geom_boxplot() + 
  facet_grid(~subject)

fit3 <- aov(well_being ~ therapy*price*sex, data = mydata2)
summary(fit3)  # снова цена как значимый фактор

fit3b <- aov(well_being ~ therapy*price*sex + Error(subject/(therapy*price)), data = mydata2)  # учтем дисперсию, связанную с испытуемым. В качестве элемента с ошибкой добавляем только внутригрупповые факторы
summary(fit3b)
