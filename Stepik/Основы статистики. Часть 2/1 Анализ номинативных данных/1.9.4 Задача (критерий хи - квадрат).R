test_data <- read.csv("https://stepic.org/media/attachments/course/524/test_data.csv", stringsAsFactors = T)

most_significant <-  function(x){
  
  return(names(which(sapply(test_data, function(x) chisq.test(table(x))$p.value) == min(sapply(test_data, function(x) chisq.test(table(x))$p.value)))))
}

most_significant(test_data)