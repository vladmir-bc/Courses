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
