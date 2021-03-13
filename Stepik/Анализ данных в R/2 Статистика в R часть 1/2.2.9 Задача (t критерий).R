ToothGrowth
?ToothGrowth
str(ToothGrowth)

df1 <- ToothGrowth
mean_len <- mean(df1$len)  # 18,81

shapiro.test(x = df1$len)  # в качестве аргумента принимается вектор значений
# p-value > 0.05, значит распределение не отличается от нормального
shapiro.test(x = df1$len[(df1$supp == "OJ") & (df1$dose == 0.5)])  # p-value > 0.05, значит распределение не отличается от нормального
shapiro.test(x = df1$len[(df1$supp == "VC") & (df1$dose == 2)])  # p-value > 0.05, значит распределение отличается от нормального

hist(df1$len)
hist(df1$len[(df1$supp == "OJ") & (df1$dose == 0.5)])
hist(df1$len[(df1$supp == "VC") & (df1$dose == 2)])


t_stat <- t.test(df1$len[(df1$supp == "OJ") & (df1$dose == 0.5)], df1$len[(df1$supp == "VC") & (df1$dose == 2)])$statistic

# аналогичное решение чере subset
correct_data <- subset(ToothGrowth, supp=='OJ' & dose==0.5 | supp=='VC' & dose==2)    
t_stat <- t.test(len ~ supp, correct_data)$statistic
