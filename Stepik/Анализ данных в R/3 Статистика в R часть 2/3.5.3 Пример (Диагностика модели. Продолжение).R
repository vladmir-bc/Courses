########################################################################
# ��������� ���������, ������� �� ���������� - ���������� �����������
# ����� ����������� � ��������� �����������

# ����� ��������� �������� ������, ���������� ������ ���� ������� �������

# ������� � ������ ����� ������

library(ggplot2)

ggplot(swiss, aes(x = Examination, y = Education)) + 
  geom_point() + 
  geom_smooth()
# ����� ��������

# �������� ������� �������� ������
lm1 <- lm(Education ~ Examination, swiss)
summary(lm1)
# R^2 ���������� 0,4878. p-value �������

# ��������� ��������� �������������� ������, ������� �������� �� ������ ���� ��������� 1 �������, �� � ����� ������� �������

swiss$Examination_squared <- (swiss$Examination)^2  # ����������� � ������� �������� Examination


lm2 <- lm(Education ~ Examination + Examination_squared, swiss)
summary(lm2)  # Examination - ��������� ���� ��������, � Examination_squared ������� �������������

# �������� ����� �� ��������� ������� 
anova(lm2, lm1)  # ������� ������� ��������� ��������

# ������� � swiss ������������� ��������

swiss$lm1_fitted <- lm1$fitted
swiss$lm2_fitted <- lm2$fitted
swiss$lm1_resid <- lm1$resid  # �������
swiss$lm2_resid <- lm2$resid  # �������
swiss$obs_number <- 1:nrow(swiss)


# �������� ������� ������������� �������� ��� ����� ���� �������
ggplot(swiss, aes(x = Examination, y = Education)) + 
  geom_point(size = 3) + 
  geom_line(aes(x = Examination, y = lm1_fitted), col = 'red', lwd=1) + 
  geom_line(aes(x = Examination, y = lm2_fitted), col = 'blue', lwd=1)
  
# ������, ��� �� ��� X ���� ������������� ��������, � �� ��� y ���� �������
# ������������� �������� � ������� ��� �������� ������:
ggplot(swiss, aes(x = lm1_fitted, y = lm1_resid)) + 
  geom_point(size = 3) + geom_hline(yintercept = 0, col = 'red', lwd = 1)

ggplot(swiss, aes(x = lm2_fitted, y = lm2_resid)) + 
  geom_point(size = 3) + geom_hline(yintercept = 0, col = 'red', lwd = 1)



