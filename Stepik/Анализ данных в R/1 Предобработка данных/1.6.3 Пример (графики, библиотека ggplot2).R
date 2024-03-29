df <- mtcars
# �������, ����� ������������ ���������� ���� ��������� 
# (��� ���������: v-�������� ��� s-��������)
df$vs <- factor(df$vs , labels = c("V", "S"))  # labels - �������� ������� �������
df$am <- factor(df$am , labels = c("Automatic", "Manual"))  # �������������� ��� ������ ������� �������

library(ggplot2)

ggplot(df, aes(x = mpg)) + # � aes ������������, ����� ��������� ����� ���������� �� ������� � ����� �������
  geom_histogram(fill = "white", col = "black", binwidth = 2) # ��������� ���� (��� ����� ������������ �� �������)

ggplot(df, aes(x = mpg, fill = am)) + # �������� dotplot. �������� �������� � ����������� �� ���� ������� �������
  geom_dotplot()

ggplot(df, aes(x = mpg)) + # �������� ������� ���������
  geom_density(fill = "red")

ggplot(df, aes(x = mpg, fill = am)) + # �������� ������� ��������� � ����������� �� ���� ������� �������
  geom_density(alpha = 0.5)  # alpha ���������� ������������ �����
