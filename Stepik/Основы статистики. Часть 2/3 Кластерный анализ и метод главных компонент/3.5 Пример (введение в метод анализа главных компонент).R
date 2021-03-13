data(swiss)
fit <- prcomp(swiss, center = T)
plot(fit, type = "l")
summary(fit)
biplot(fit)

##############################################
source('https://raw.githubusercontent.com/vqv/ggbiplot/master/R/ggbiplot.r')

source('https://raw.githubusercontent.com/vqv/ggbiplot/master/R/ggscreeplot.r')

pca_object <- prcomp(iris[,-5], center = T, scale. = T)

ggbiplot(pca_object)

ggscreeplot(pca_object)


# ј можно то же сделать с использованием библиотеки ggbiplot:
library(devtools)
library(ggbiplot)

dt <- swiss
dt$is_catholic <- ifelse(swiss$Catholic > 50, 1, 0)
dt$is_catholic <- factor(dt$is_catholic)
fit <- prcomp(swiss, center = T)
g <- ggbiplot(fit, obs.scale = 1, var.scale = 1,
              group = dt$is_catholic,
              ellipse = TRUE,
              circle = TRUE)
g <- g + scale_color_discrete(name = '')
g <- g + theme(legend.direction = 'horizontal',
               legend.position = 'top')
print(g)


###################################################

library(pca3d)

dt <- swiss
dt$is_catholic <- ifelse(swiss$Catholic > 50, 1, 0)
dt$is_catholic <- factor(dt$is_catholic)
fit <- prcomp(swiss, center = T)
pca3d(fit, group = dt$is_catholic,
      fancy = T, 
      new=T)
