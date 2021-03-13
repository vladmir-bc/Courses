mtcars$new_var <- ifelse(mtcars$carb >= 4 | mtcars$cyl > 6, 1, 0)  # 1 вариант

for (i in 1:nrow(mtcars)){  # 2 вариант через цикл for
  if (mtcars$carb[i] >= 4 | mtcars$cyl[i] > 6){
    mtcars$new_var[i] <- 1
  } else {
    mtcars$new_var[i] <- 0
  }
}

