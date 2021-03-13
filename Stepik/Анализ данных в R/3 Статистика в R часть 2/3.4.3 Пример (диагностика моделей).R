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
