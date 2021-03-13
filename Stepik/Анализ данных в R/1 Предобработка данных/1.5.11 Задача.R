df <- airquality
df2 <- subset(df, Month%in%c(7, 8, 9))
result <- aggregate(Ozone ~ Month, df2, FUN = length)
