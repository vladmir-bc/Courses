### ANOVA

library(ggplot2)

DV ~ IV  # ����� ������� ����� ������� ����������� �/� ��������� � ����������� �����������

DV ~ IV1 + IV2  # ��� ����� �������, ��� �� ����������� ���������� ������ 2 ���������

DV ~ IV1:IV2  # : ������������ ��� �������� ��������������, �.�. ����� ������� ����� ���������� �� ������ ������� �� ������ 3 ����������

DV ~ IV1 + IV2 + IV1:IV2  # ������� � �������� ��������� + ��������������

DV ~ IV1 * IV2  # ���������� ������� ����� �������� ����� *. ��� �������� ������� � �������� ��������� + ��������������

DV ~ (IV1 + IV2 + IV3)^2  # �������, ��� ���� 3 ����������� ���������� (3 ����������) � ��� ���������� ��� �������� ������� + �������������� �� 2 ������

DV ~ IV1 + Error(subject/IV1)  # ��������� ��������� ��� ����. �������
#########################################################################

library(ggplot2)
mydata <- read.csv("shops.csv", stringsAsFactors = T)  # ��������� ��� �� �������� � ������ ��������� ������

str(mydata)

boxplot(price ~ origin, data = mydata)  # ����������� �/� ��������� � ����������� ����������

ggplot(mydata, aes(x = origin, y = price))+
  geom_boxplot()

fit <- aov(price ~ origin, data = mydata)  # ������������, ����� ��������� ������������� ������, �������� ������
summary(fit)  # ���������� ���������� � �������� �����
#########################################################################

# ������������� ������������� ������


fit1 <- aov(price ~ origin + store, data = mydata)
summary(fit1)

model.tables(fit1, "means")  # ���������� ������������ ������� �� ������� (�������)
#########################################################################

pd <- position_dodge(0.1)
ggplot(mydata, aes(x = store, y = price, color = origin, group = origin))+  #group=origin ��� ����, ����� ��������, ��� � ����� ������ ���������� (����� ������� ����� �� �������)
  stat_summary(fun.data=mean_cl_boot,
               geom='errorbar', width=0.1,
               position=position_dodge(width=0.2)) +  # position=position_dodge(width=0.2) ��� ����, ����� �������� ���������� �� �������� � ����� �����
  stat_summary(fun.data=mean_cl_boot,
               geom='line', size=1,
               position=position_dodge(width=0.2)) +
  stat_summary(fun.data=mean_cl_boot,
               geom='point', shape='square',
               size=3, position=position_dodge(width=0.2)) +
  theme_bw()  # The classic dark-on-light ggplot2 theme. May work better for presentations displayed with a projector.

fit3 <- aov(price ~ origin*store, data=mydata)  # origin + store + origin:store
summary(fit3)
