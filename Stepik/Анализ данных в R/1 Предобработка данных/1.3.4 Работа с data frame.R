?read.table
?read.csv

mydata <- read.csv('evals.csv', stringsAsFactors=TRUE)
mydata


head(mydata, 3)  #  ���������� ������ 3 ������
tail(mydata)  # ���������� ��������� 6 �����

View(mydata)  # ��������

str(mydata)  # ����������� ���������

summary(mydata)  # �������� �������������� ���������� �� ����. ����������
a <- names(mydata)  # �������� ������� (����������) - ������ ��������. �������� �������� � ���������

# Variables

b <- mydata$score  # ������� ������ �������� ����������
mean(mydata$score)  # ������� ��� ��������� ��������
summary(mydata$score)  # ���������� � �������� ������
mydata$ten_point_scale <- mydata$score * 2  # �������� ����� ������� � mydata �� ���������� *2

summary(mydata$ten_point_scale)  # ����� ������������ ���������� ����� � 2 ���� ������

mydata$new_varible <- 0  # ����� ������� � �������� ����������
mydata$number <- 1:nrow(mydata)  # ������ ���� ������� ������ � 1 �� ���������
summary(mydata$number)


nrow(mydata)  # ���������� ���������� ������� � mydata
ncol(mydata)  # ���������� ��������, ������� � mydata

#  Subsetting

mydata$score[1:10]

mydata[1,1]
mydata[c(2,193,225),1]  # �������� ����� 2,193,225 � 1 ������� (score)
mydata[101:200,1]  # �������� 101:200 � 1 ������� (score)
mydata[5,]  # ��� �������� 5 ������
mydata[,1]  # ��� �������� 1 �������
mydata[,1] == mydata$score

mydata[,2:5]  # ��� ������� �� 2-5 ��������
head(mydata[,2:5])  # ������ 6 ������� �� 2-5 ��������
