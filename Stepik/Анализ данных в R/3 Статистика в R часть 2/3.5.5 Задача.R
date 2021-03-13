
library(gvlma)
mydata <- read.csv("homosc.csv")
str(mydata)
x <- gvlma(DV ~ IV, data = mydata)
summary(x)
