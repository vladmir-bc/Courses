library(ggplot2)
df <- airquality
df$Month <- factor(df$Month)  # �������� ��������, ��� ��� ����������� ����������� ������� ggplot ������� ��������� ���������� �� ��� x.
ggplot(subset(df, Month==9), aes(x = Month, y = Ozone))+geom_boxplot()

