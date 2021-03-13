######################################################
# regression diagnostics

data(swiss)
str(swiss)


# Посмотрим взаимосвязь между всеми переменными
pairs(swiss)  # принимает либо датасет, либо матрицу с переменными
# посмотрим на взаимосвязь Examination и Education

library(ggplot2)

# построим диаграмму рассеивания
ggplot(swiss, aes(x = Examination, y = Education)) + 
  geom_point() + 
  theme(axis.text = element_text(size=25),
        axis.title = element_text(size = 25, face = "bold"))

######################################################

# для начала посмотрим на выбросы (outliers)

ggplot(swiss, aes(x = Examination, y = Education)) + 
  geom_point() + 
  theme(axis.text = element_text(size=25),
        axis.title = element_text(size = 25, face = "bold")) + 
  geom_smooth(method = 'lm')
# Некоторые точки сильно отклоняются от регрессионной линии
######################################################

# посмотрим на то, нормально ли распределены переменные, с которыми мы работаем

ggplot(swiss, aes(x = Examination)) + 
  geom_histogram()

ggplot(swiss, aes(x = Education)) + 
  geom_histogram()  # переменная распределена не нормально, поэтому требуется преобразование
# например, для преобразования можно взять логарифм

ggplot(swiss, aes(x = log(Education))) + 
  geom_histogram() # центр распределения сдвинулся вправо
