#########################################################################

library(ggplot2)

mydata <- read.csv("Pillulkin.csv", stringsAsFactors = T)

str(mydata)
mydata$patient <- as.factor(mydata$patient)

str(mydata)
ggplot(mydata, aes(x = pill, y = temperature)) +
  geom_boxplot() + 
  facet_grid(~patient)
fit <- aov(temperature ~ pill + Error(patient/temperature), data = mydata)  # зависимая/независимая переменные
summary(fit)
