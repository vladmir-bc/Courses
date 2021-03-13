library(ggplot2)

exp_data <- read.csv("https://raw.githubusercontent.com/opetchey/BIO144/master/3_datasets/politeness_data.csv", stringsAsFactors = T)
exp_data$scenario <- as.factor(exp_data$scenario)
str(exp_data)

plot_1 <- ggplot(exp_data, aes(x = scenario, y = frequency, fill = attitude)) + 
  geom_boxplot()
