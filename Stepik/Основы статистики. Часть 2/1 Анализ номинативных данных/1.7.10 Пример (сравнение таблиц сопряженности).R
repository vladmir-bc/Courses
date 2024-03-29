#  ��-����

patients <- rbind(c(18, 7), c(6, 13))
chisq.test(patients)


#  ������ ��������
#����������� �������
patients <- rbind(c(18, 7), c(6, 13))
#�������� ������ � �������
colnames(patients) <- c("Yes", "No")
rownames(patients) <- c("Placebo", "Aspirin")
#��� ������, ������� ��� �����
mosaicplot(patients, color=T, shade=T, ylab="Thrombosis", xlab="Group")
#� ��� ��� ����� � �������� ������������� �������, ������� �� ������
mosaicplot(patients, color=T, shade=T, ylab="Thrombosis", xlab="Group", cex.axis=1, main="")

#����������� �������
patients2 <- rbind(c(25, 1), c(3, 30))
#�������� ������ � �������
colnames(patients2) <- c("Yes", "No")
rownames(patients2) <- c("Placebo", "Aspirin")
#��� ��� ������
mosaicplot(patients2, color=T, shade=T, ylab="Thrombosis", xlab="Group", cex.axis=1, main="")

#  ����� ����������� ������� � R:
O <- matrix(c(18, 7, 6, 13), ncol = 2, nrow = 2, byrow = T)
print(chisq.test(O)$residuals)


#  �������� � R
#����������� �������
dtp <- rbind(c(10, 40), c(35, 15))
#�������� ������ � �������
colnames(dtp) <- c("��� � ���", "�� ��� � ���")
rownames(dtp) <- c("�������� �����", "�� �������� �����")
#��� ��� ������
mosaicplot(dtp, color=T, shade=T, xlab="���", ylab="Group", cex.axis=1, main="")

test <- chisq.test(dtp)
test$observed # observed counts (same as M) (����������� ��������)
test$expected # expected counts under the null (��������� ��������)
test

network <- rbind(c(28.9, 43.5, 20.28, 41.8, 66, 11.5, 33, 44, 40.4, 44.6), c(73, 70.7, 43.7, 76.6, 94.4, 22.5, 34.7, 67, 71, 77.3))
rownames(network) <- c("�����, ��/���", "�������, ��/���")
chisq.test(network)
library(ggplot2)
mydata <- as.data.frame(network)
str(mydata)
mydata <- read.csv("steam_internet.csv", header = T)
ggplot(mydata, aes(x = origin, y = price))+
  geom_boxplot()