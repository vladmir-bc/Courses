######################################################
# regression diagnostics

data(swiss)
str(swiss)


# ��������� ����������� ����� ����� �����������
pairs(swiss)  # ��������� ���� �������, ���� ������� � �����������
# ��������� �� ����������� Examination � Education

library(ggplot2)

# �������� ��������� �����������
ggplot(swiss, aes(x = Examination, y = Education)) + 
  geom_point() + 
  theme(axis.text = element_text(size=25),
        axis.title = element_text(size = 25, face = "bold"))

######################################################

# ��� ������ ��������� �� ������� (outliers)

ggplot(swiss, aes(x = Examination, y = Education)) + 
  geom_point() + 
  theme(axis.text = element_text(size=25),
        axis.title = element_text(size = 25, face = "bold")) + 
  geom_smooth(method = 'lm')
# ��������� ����� ������ ����������� �� ������������� �����
######################################################

# ��������� �� ��, ��������� �� ������������ ����������, � �������� �� ��������

ggplot(swiss, aes(x = Examination)) + 
  geom_histogram()

ggplot(swiss, aes(x = Education)) + 
  geom_histogram()  # ���������� ������������ �� ���������, ������� ��������� ��������������
# ��������, ��� �������������� ����� ����� ��������

ggplot(swiss, aes(x = log(Education))) + 
  geom_histogram() # ����� ������������� ��������� ������
