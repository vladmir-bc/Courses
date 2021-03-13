mtcars

mini_mtcars <- mtcars[c(3,7,10,12, length(mtcars[,1])), ]  # 1 решение, обращаемся к 3, 7, 10, 12 и последней строке и ко всем колонкам
mini_mtcars <- mtcars[c(3,7,10,12, nrow(mtcars)), ]  # 2 решение через nrow

# решение с форума через tail:
mini_mtcars <- rbind(mtcars[c(3,7,10,12),], tail(mtcars, 1))