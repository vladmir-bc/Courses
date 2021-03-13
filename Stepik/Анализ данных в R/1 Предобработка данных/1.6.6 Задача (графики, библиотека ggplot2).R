library(ggplot2)
df <- ?mtcars
plot1 <- ggplot(df, aes(x=mpg, y=disp, col = hp)) + geom_point()
