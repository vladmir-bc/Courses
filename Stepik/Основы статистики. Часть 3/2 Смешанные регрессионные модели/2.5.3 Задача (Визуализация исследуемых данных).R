library(ggplot2)

exp_data <- read.csv("https://raw.githubusercontent.com/opetchey/BIO144/master/3_datasets/politeness_data.csv", stringsAsFactors = T)
exp_data$scenario <- as.factor(exp_data$scenario)
str(exp_data)

plot_2 <- ggplot(data = exp_data, aes(frequency, fill = subject)) + 
  geom_density(alpha = 0.2, na.rm = T) + 
  facet_grid(~ gender)


