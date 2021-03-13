library(ggplot2)
library(ggrepel) # для симпатичной подписи точек на графике

x <- runif(10, 1.0,10.0) #заменил rnorm, чтобы график с одинаковыми масштабами 
y <- runif(10, 1.0,10.0) #осей x и у смотрелся получше
test_data <- data.frame(x, y)
rownames(test_data) <- LETTERS[1:10] #если запихнуть в названия строк наши условные названия точек, то они передадутся в лэйблы dist, а оттуда в hclust и в plot

ggplot(test_data, aes(x, y, label = rownames(test_data)))+
  geom_point()+
  geom_text_repel()+
  scale_x_continuous(breaks = 1:10)+ #для одинакового шага осей
  scale_y_continuous(breaks = 1:10)

d = dist(test_data)
fit <- hclust(d, method = "single")
plot(fit) #возьмет лэйблы из первоисточника
rect.hclust(fit, 2) # укажите желаемое число кластеров, сейчас стоит 2


##############################################
library(ape)
set.seed(222)
tr <- rtree(20, tip.label = c("B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U")) 
#левое дерево
plot.phylo(tr) 
#правое дерево 
plot.phylo(tr, use.edge.length=FALSE)