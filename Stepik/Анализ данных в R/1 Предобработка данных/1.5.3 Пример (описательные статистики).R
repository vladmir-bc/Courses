?mtcars

df <- mtcars

str(df)

# сделаем, чтобы номинативные переменные были факторами 
# (тип двигателя: v-образный или s-образный)

df$vs <- factor(df$vs , labels = c("V", "S"))  # labels - названия уровней фактора
df$am <- factor(df$am , labels = c("Automatic", "Manual"))  # автоматическая или ручная коробка передач
