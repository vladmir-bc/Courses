

for (i in 1:nrow(iris)){
  counter <- 0
  if (iris$Sepal.Length[i] > mean(iris$Sepal.Length)){
    counter = counter + 1
  }
  if (iris$Sepal.Width[i] > mean(iris$Sepal.Width)){
    counter = counter + 1
  }
  if (iris$Petal.Length[i] > mean(iris$Petal.Length)){
    counter = counter + 1
  }
  if (iris$Petal.Width[i] > mean(iris$Petal.Width)){
    counter = counter + 1
  }
  if (counter >= 3){
    iris$important_cases[i] <- "Yes"
  } else {
    iris$important_cases[i] <- "No"
  }
}
iris$important_cases <- factor(iris$important_cases)



