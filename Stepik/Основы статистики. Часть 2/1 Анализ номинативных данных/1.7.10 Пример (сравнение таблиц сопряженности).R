#  хи-тест

patients <- rbind(c(18, 7), c(6, 13))
chisq.test(patients)


#  анализ остатков
#воссоздадим таблицу
patients <- rbind(c(18, 7), c(6, 13))
#подпишем строки и столбцы
colnames(patients) <- c("Yes", "No")
rownames(patients) <- c("Placebo", "Aspirin")
#вот график, который нам нужен
mosaicplot(patients, color=T, shade=T, ylab="Thrombosis", xlab="Group")
#а вот так можно в точности воспроизвести рисунок, который мы видели
mosaicplot(patients, color=T, shade=T, ylab="Thrombosis", xlab="Group", cex.axis=1, main="")

#воссоздадим таблицу
patients2 <- rbind(c(25, 1), c(3, 30))
#подпишем строки и столбцы
colnames(patients2) <- c("Yes", "No")
rownames(patients2) <- c("Placebo", "Aspirin")
#вот наш график
mosaicplot(patients2, color=T, shade=T, ylab="Thrombosis", xlab="Group", cex.axis=1, main="")

#  Чтобы просмотреть остатки в R:
O <- matrix(c(18, 7, 6, 13), ncol = 2, nrow = 2, byrow = T)
print(chisq.test(O)$residuals)


#  картинка в R
#воссоздадим таблицу
dtp <- rbind(c(10, 40), c(35, 15))
#подпишем строки и столбцы
colnames(dtp) <- c("Был в ДТП", "Не был в ДТП")
rownames(dtp) <- c("Проходит курсы", "Не проходит курсы")
#вот наш график
mosaicplot(dtp, color=T, shade=T, xlab="ДТП", ylab="Group", cex.axis=1, main="")

test <- chisq.test(dtp)
test$observed # observed counts (same as M) (наблюдаемые значения)
test$expected # expected counts under the null (ожидаемые значения)
test

network <- rbind(c(28.9, 43.5, 20.28, 41.8, 66, 11.5, 33, 44, 40.4, 44.6), c(73, 70.7, 43.7, 76.6, 94.4, 22.5, 34.7, 67, 71, 77.3))
rownames(network) <- c("Рашка, Мб/сек", "Пендосы, Мб/сек")
chisq.test(network)
library(ggplot2)
mydata <- as.data.frame(network)
str(mydata)
mydata <- read.csv("steam_internet.csv", header = T)
ggplot(mydata, aes(x = origin, y = price))+
  geom_boxplot()