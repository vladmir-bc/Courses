
#########################################################################
library(ggplot2)
mydata <- read.csv("Pillulkin2.csv", stringsAsFactors = T)

str(mydata)
mydata$patient <- as.factor(mydata$patient)
ggplot(mydata, aes(x = pill, y = temperature)) +
  geom_boxplot() + 
  facet_grid(~patient)
fit <- aov(temperature ~ doctor*pill + Error(patient/doctor*pill), data = mydata)
summary(fit)
