df2 <- iris

ggplot(iris, aes(Sepal.Length, fill = Species)) + geom_histogram()
ggplot(iris, aes(Sepal.Length)) + geom_histogram(aes(fill = Species))
ggplot(iris, aes(Sepal.Length)) + geom_histogram(aes(col = Species))
ggplot(iris, aes(Sepal.Length)) + geom_histogram(fill = Species)
ggplot(iris, aes(Sepal.Length, col = Species)) + geom_histogram()

ggplot(iris, aes(Sepal.Length)) + geom_histogram(fill = Species)

ggplot(iris, aes(Sepal.Length)) + geom_histogram(aes(col = Species))
ggplot(iris, aes(Sepal.Length, fill = Species)) + geom_histogram()
ggplot(iris, aes(Sepal.Length, col = Species)) + geom_histogram()
ggplot(iris, aes(Sepal.Length)) + geom_histogram(aes(fill = Species))

#fill - заливка (цвет внутри фигур)
#col - граница (цвет контура)
#на маленьких графических элементах разница не видна

#Как ответили выше, для geom_histogram col и fill работают так :
  
 # col :
  
  #ggplot(iris, aes(Sepal.Length)) + geom_histogram(aes(col = Species)) # col - граница (цвет контура)

#результат тот же, если записать так :
  
 # ggplot(iris, aes(Sepal.Length, col = Species)) + geom_histogram() # col - граница (цвет контура)

#fill :
  
 # ggplot(iris, aes(Sepal.Length)) + geom_histogram(aes(fill = Species))  # fill - заливка (цвет внутри фигур)

#результат тот же, если записать так :
  
  #ggplot(iris, aes(Sepal.Length, fill = Species)) + geom_histogram()  # fill - заливка (цвет внутри фигур)