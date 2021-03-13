mtcars
gear <- mtcars$gear %% 2 == 0 * 1
mtcars$even_gear <- gear * 1

# аналогичное решение в одну строчку:
mtcars$even_gear <- 1-mtcars$gear%%2

# решение через as.numeric:
mtcars$even_gear <- as.numeric(mtcars$gear%%2 == 0)  # преобразует логические или символьные значения в цифры
