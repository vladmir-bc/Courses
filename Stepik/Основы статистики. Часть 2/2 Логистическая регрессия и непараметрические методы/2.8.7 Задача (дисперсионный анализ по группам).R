test_data <- read.csv("https://stepic.org/media/attachments/course/524/s_anova_test.csv", stringsAsFactors = T)


smart_anova <- function(test_data){
  if ((shapiro.test(subset(test_data[,1], test_data$y == 'A'))$p.value >= 0.05) & (shapiro.test(subset(test_data[,1], test_data$y == 'B'))$p.value >= 0.05) & (shapiro.test(subset(test_data[,1], test_data$y == 'C'))$p.value >= 0.05) & (bartlett.test(x ~ y, test_data)$p.value >= 0.05)){
    fit <- aov(x ~ y, test_data)
    p_value <- summary(fit)[[1]]$'Pr(>F)'[1]
    return(unlist(data.frame(ANOVA = p_value)))
  }else{
    kw <- kruskal.test(x ~ y, data = test_data)$p.value
    return(unlist(data.frame(KW = kw)))
  }
}
smart_anova(test_data)


# Пример правильного решения:
  
smart_anova <- function(test){  
  p_normal <- unlist(by(test[, 1], test[, 2], function(x) shapiro.test(x)$p.value))   
  sd_equal <- bartlett.test(x ~ y, test)$p.value  
  if (all(p_normal > 0.05) & sd_equal > 0.05){    
    fit <- aov(x ~ y, test)    
    result <- c(ANOVA = summary(fit)[[1]]$'Pr(>F)'[1])    
    return(result)  
  } else {    
    fit <- kruskal.test(x ~ y, test)    
    result <- c(KW = fit$p.value)    
    return(result)    
  }    
}