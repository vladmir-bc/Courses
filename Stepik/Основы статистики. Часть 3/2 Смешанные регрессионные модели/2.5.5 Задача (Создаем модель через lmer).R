library(ggplot2)
library(lme4)

exp_data <- read.csv("https://raw.githubusercontent.com/opetchey/BIO144/master/3_datasets/politeness_data.csv", stringsAsFactors = T)
exp_data$scenario <- as.factor(exp_data$scenario)
str(exp_data)


fit_2 <- lmer(frequency ~ attitude + gender + (1|subject) + (1|scenario), exp_data)
summary(fit_2)
