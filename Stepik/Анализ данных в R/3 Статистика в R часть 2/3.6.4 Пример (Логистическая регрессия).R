########################################################################



library(ggplot2)

my_df <- read.csv('train.csv', sep = ';', stringsAsFactors = T)  # ������: ��� �� ��, ������� ��� �� ������� ������ ������� ������,
# ������ ��� ������������
str(my_df)


# ������������� ������

ggplot(my_df, aes(read, math, col = gender))+
  geom_point()+
  facet_grid(.~hon)+
  theme(axis.text = element_text(size=25),
        axis.title = element_text(size=25, face="bold"))

# �������� ������������� ������

fit <- glm(hon ~ read + math + gender, my_df, family = 'binomial')  # ������ lm ������������ glm
# family = binomial - ������������� ������������� ���������
summary(fit)

exp(fit$coefficients)  # �������� �� ��������� odds � ��������� odds
########################################################################


head(predict(object = fit))  # ������� �������� ��������� �� odds ��� ������� �����������

head(predict(object = fit, type = 'response')) # ������� ����� ���������� � ���� �����������
# ��� ������� ����������� � ��� ���� ������������� ����������� ����, ��� �� ������� ����� � ������� ��������

my_df$prob <- predict(object = fit, type = 'response')
# ������������ ��������� ��� ���������� �����������