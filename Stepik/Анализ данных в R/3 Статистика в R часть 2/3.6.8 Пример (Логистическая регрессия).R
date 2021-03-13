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
########################################################################


head(predict(object = fit))  # получим значения логарифма от odds для каждого испытуемого

head(predict(object = fit, type = 'response')) # получим сразу результаты в виде вероятности
# для каждого испытуемого у нас есть предсказанная вероятность того, что он окончит школу с красным дипломом

my_df$prob <- predict(object = fit, type = 'response')
# биномиальная регрессия нам возвращает вероятность
########################################################################

# построим ROC кривую

library(ROCR)
pred_fit <- prediction(my_df$prob, my_df$hon)  # помещаем в функцию предсказанные и реальные значения
perf_fit <- performance(pred_fit, "tpr", "fpr")
plot(perf_fit, colorize=T, print.cutoffs.at = seq(0.1,by=0.1))
# узнаем площадь под кривой

auc <- performance(pred_fit, measure = "auc")
str(auc)  # получили значение площади под кривой 0,87

# функцией performance создадим объект, в котором сохраним соотношение между
# значением порога, после которого мы будем говорить что исход будет положительным
# и специфичностью классификатора

# специфичность - это то, насколько хорошо нам удается правильно предсказывать
# отрицательный исход события
perf3 <- performance(pred_fit, x.measure = "cutoff", measure = "spec")
# чувствительность - то, насколько хорошо нам удается предсказывать положительный исход события
perf4 <- performance(pred_fit, x.measure = "cutoff", measure = "sens")
# нанесем еще соотношение между значением порога и общей эффективностью классификатора
perf5 <- performance(pred_fit, x.measure = "cutoff", measure = "acc")

plot(perf3, col = "red", lwd = 2)
plot(add=T, perf4, col = "green", lwd = 2)
plot(add=T, perf5, lwd=2)

legend(x = 0.6, y = 0.3, c("spec", "sens", "accur"),
       lty=1, col=c("red", "green", "black"), bty = 'n', cex = 1, lwd = 2)
# порог отсечения разумно сделать на пересечении трех показателей
abline(v=0.225, lwd=2)  # добавим ертикальную линию, которая показывает точку пересечения

# создадим новую переменную pred_respond, и это уже будет не просто вероятность,
# а реальные значения, либо получил красный диплом, либо нет
my_df$pred_resp <- factor(ifelse(my_df$prob > 0.225, 1, 0), labels = c("N", "Y"))

# далее мы можем создать еще одну переменную, где запишем, правильно или неправильно мы предсказали
# с точки зрения бинарного исхода
my_df$correct <- ifelse(my_df$pred_resp == my_df$hon, 1, 0)

# построим график, который показывает, насколько правильно мы идентифициаровали
ggplot(my_df, aes(prob, fill = factor(correct)))+
  geom_dotplot()+
  theme(axis.text=element_text(size=25),
        axis.title=element_text(size=25,face="bold"))

#рассчитаем процент правильных классификаций:
mean(my_df$correct)
########################################################################
# мы можем использовать полученные результаты, чтобы предсказывать значения на новых данных

test_df <- read.csv("test.csv", sep = ";")
test_df$hon <- NA

test_df$hon <- predict(fit, newdata = test_df, type = "response")  # указываем, что мы хотим получать вероятности, а не значения логарифма
View(test_df)
