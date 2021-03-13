age <- c(16, 18, 22, 27)
is_married <- c(F, F, T, T)
name <- c("Olga", "Maria", "Nastya", "Polina")


data <- list(age, is_married, name)  # получилс€ двумерный массив из векторов
data

# ѕравила индексации
data[[1]]  # указываем уровень (первый вектор)

data[[2]]  # указываем уровень (второй вектор)

data[[1]][1]  # выведет 1 элемент 1 вектора

data[[2]][3]  # выведет 3 элемент 2 листа (вектора)

data[[3]][2:3]

# —охраним данные в формате DataFrame
df <- data.frame(Name = name, Age = age, 
                 Is_married = is_married)  # создаст таблицу с 4 строчками и 3 столбцами
typeof(df)  # тип переменной df - list
