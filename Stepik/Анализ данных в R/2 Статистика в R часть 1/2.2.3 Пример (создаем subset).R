?iris
df <- iris

str(df)

df1 <- subset(df, Species != "setosa")
str(df1)
table(df1$Species)  # ���������� ����������, ����������� � ������� �������
