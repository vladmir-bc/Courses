1 : 67  # ������ [1;67]

my_vector1 <- 1 : 67
my_vector2 <- c(-32, 45, 67, 12.78, 129, 0, -65)

my_vector1[1]  # ���������� � ������� �������� �������
my_vector1[3]

my_vector2[2]

my_vector2[c(1, 2, 3)]  # ���������� � 1, 2, 3 �������� my_vector2
my_vector2[1:3]  # ���������� � 1, 2, 3 �������� my_vector2
my_vector2[c(1,5,6,7,10)] # 10 ������� ����

# �������� � ���������

my_vector1 + 10 #  ��������� 10 � ������� �������� �������
my_vector2 + 56 #  ��������� 56 � ������� �������� �������

my_vector2 == 0  # ��������� � 0 ����� ����������� ��� ������� �������� �������
my_vector1 > 30  # ��������� � 30 ����� ����������� ��� ������� �������� �������

x <- 23
my_vector1 > 23
my_vector1 > x

