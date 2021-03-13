test_data <- read.csv("https://stepic.org/media/attachments/course/524/test_drugs.csv", stringsAsFactors = T)
max_resid <- function(x){
  tab <- table(x)
  return(c(rownames(tab)[which(chisq.test(tab)$stdres == max(chisq.test(tab)$stdres), arr.ind = T)[1]], colnames(tab)[which(chisq.test(tab)$stdres == max(chisq.test(tab)$stdres), arr.ind = T)[2]]))
  
}



# ѕример правильного решени€ студента курса:
  
max_resid <- function(test_data){    
  d <- table(test_data)    
  chi <- chisq.test(d)    
  ind <- which(chi$stdres==max(chi$stdres), arr.ind = T)    
  return(c(row.names(d)[ind[1]],colnames(d)[ind[2]]))    
}


library(ggplot2)

df <- diamonds
str(diamonds)
df$count <- 1
table(diamonds$color)[1,]
diamonds$color

obj <- ggplot(df, aes(x = factor(color), fill=cut)) + 
  geom_bar(position="dodge", stat="bin")
?geom_bar

ggplot(mtcars, aes(x=factor(cyl)))+
  geom_bar(stat="bin", width=0.7, fill="steelblue")+
  theme_minimal()

library(ggplot2)

# create a dataset
specie <- c(rep("sorgho" , 3) , rep("poacee" , 3) , rep("banana" , 3) , rep("triticum" , 3) )
condition <- rep(c("normal" , "stress" , "Nitrogen") , 4)
value <- abs(rnorm(12 , 0 , 15))
data <- data.frame(specie,condition,value)

# Grouped
ggplot(data, aes(fill=condition, y=value, x=specie)) + 
  geom_bar(position="dodge", stat="identity")