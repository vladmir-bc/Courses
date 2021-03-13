mtcars

# mydata[mydata$gender == 'female',1:3]
# subset(mydata, gender == 'female')

mpg_4 <- mtcars$mpg[mtcars$cyl == 4]  # решение 1
mpg_4 <- mtcars[,1][mtcars$cyl == 4]  # решение 2
mpg_4 <- subset(mtcars, mtcars$cyl == 4)[,1]  # решение 3

