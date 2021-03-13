########################################################################



library(ggplot2)

my_df <- read.csv('train.csv', sep = ';', stringsAsFactors = T)  # данные: как на то, получил или не получил ученик красный диплом,
# влияет его успеваемость
str(my_df)


# визуализируем данные

ggplot(my_df, aes(read, math, col = gender))+
  geom_point()+
  facet_grid(.~hon)+
  theme(axis.text = element_text(size=25),
        axis.title = element_text(size=25, face="bold"))

# пропишем регрессионную модель

fit <- glm(hon ~ read + math + gender, my_df, family = 'binomial')  # вместо lm используется glm
# family = binomial - использование логистической регрессии
summary(fit)

exp(fit$coefficients)  # перейдем от логарифма odds к значениям odds

