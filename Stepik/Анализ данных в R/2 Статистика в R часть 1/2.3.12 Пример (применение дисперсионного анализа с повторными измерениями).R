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

#########################################################################
# � ���������� �������� ������ ���� 2 ������, �������� ���� ���� ���������, ���� �������������
# ������������� ������ ����� ���, ��� � ���� ����� ������� ����� ����� �����
# ����� ������� ����� ����������� ������������� ��������� � ���������� �� ������������� ���������:
# ����� ��������, ��� ������ ������ ���� ��� �� ��������� ���������� - ���� ���������

mydata <- read.csv("shops.csv", stringsAsFactors = T)  # ��������� ��� �� �������� � ������ ��������� ������

ggplot(mydata, aes(x = food, y = price))+
  geom_boxplot()

fit5 <- aov(price ~ food, data=mydata)
summary(fit5)  # �� ����� �������, ��� ������ ��������� ������� ���������� �� ����, �� �� ����� �������, ����� ������
# ��� ����, ����� �������, ����� ������ ������ ����������, ��� ���� ������������ ������������� ���������

TukeyHSD(fit5)  # �������� ����� - ��������� ������� �������� ���������. �������� �������� ����� �������, ��� ����������

#########################################################################

# ������������� ������ � ���������� �����������. �� ���������, ����� ���� ���������� �� ����������, � ������������� �� �����-�� ����������.
# ��������, � ��� ���� ���������, ������ �� ������� �������� ��������� ������. � ��� �����, ��� ���������� ����� ����� �����������, ���������� ��������� ������������� ������ � ���������� �����������

library(ggplot2)

mydata2 <- read.csv("therapy_data.csv", stringsAsFactors = T)
str(mydata2)

mydata2$subject <- as.factor(mydata2$subject)  # ���������� ��� ������
#  �������� ������:

fit1 <- aov(well_being ~ therapy, data = mydata2)  # ������ ������� ��������� �� ������
summary(fit1)

# ��� ����� ����, ��� ������ ���������� �������� ��� ����� ������������ (3 ��������� ����, ��������� ������ �� ���� ���������)
fit1b <- aov(well_being ~ therapy + Error(subject/therapy), data = mydata2)  # ��������� �������� Error - ������, ��������� � ����������. ������������ ������ - subject � ������, ������� �������� �� ����� ������ - �������
summary(fit1b)

fit2 <- aov(well_being ~ therapy*price, data = mydata2)
summary(fit2)  # ���� ��������� �������� ��������

ggplot(mydata2, aes(x = price, y = well_being)) + 
  geom_boxplot()

#  �������� �� �� ����� ������ � ������ ���������, ��������� � �����������

fit2b <- aov(well_being ~ therapy*price + Error(subject/(therapy*price)), data = mydata2)
summary(fit2b)  # ������ ������� ���� ��������� �� �������� ��������, � ��� ���������

ggplot(mydata2, aes(x = price, y = well_being)) + 
  geom_boxplot() + 
  facet_grid(~subject)

fit3 <- aov(well_being ~ therapy*price*sex, data = mydata2)
summary(fit3)  # ����� ���� ��� �������� ������

fit3b <- aov(well_being ~ therapy*price*sex + Error(subject/(therapy*price)), data = mydata2)  # ����� ���������, ��������� � ����������. � �������� �������� � ������� ��������� ������ ��������������� �������
summary(fit3b)
