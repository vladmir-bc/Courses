mydata <- read.csv('evals.csv')

a <- 0

# �������� if

if (a > 0){
  print('positive')
} 
if (a == 0){
  print('equal')
} else {
  print('not positive')
}

# ������ ������� ������ � ���� �������. ������� ����� ��������� - ����� �������� � ��������� ������������ �����
a <- c(1, -1)

ifelse(a > 0, 'positive', ifelse(a == 0, 'equal', 'not positive'))  # ����������� �����������
