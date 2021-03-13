

df <- mtcars
descriptions_stat <- aggregate(cbind(disp, hp) ~ am, df, sd) # 1 решение
descriptions_stat <- aggregate(df[,c(3, 4)], by = list(df$am), FUN = sd) # 2 решение
descriptions_stat <- aggregate(x = df[,c(3, 4)], by = list(df$am), FUN = sd) # 3 решение
