######################################################
# regression diagnostics

data(swiss)
str(swiss)


# ѕосмотрим взаимосв€зь между всеми переменными
pairs(swiss)  # принимает либо датасет, либо матрицу с переменными
# посмотрим на взаимосв€зь Examination и Education

library(ggplot2)

# построим диаграмму рассеивани€
ggplot(swiss, aes(x = Examination, y = Education)) + 
  geom_point() + 
  theme(axis.text = element_text(size=25),
        axis.title = element_text(size = 25, face = "bold"))

######################################################

# дл€ начала посмотрим на выбросы (outliers)

ggplot(swiss, aes(x = Examination, y = Education)) + 
  geom_point() + 
  theme(axis.text = element_text(size=25),
        axis.title = element_text(size = 25, face = "bold")) + 
  geom_smooth(method = 'lm')
# Ќекоторые точки сильно отклон€ютс€ от регрессионной линии
