# print('Введите данные в следующем порядке: число строк, число столбцов, число мин: ')
# n = [int(c) for c in input().split()]
# a = [[0 for j in range(n[1])] for i in range(n[0])]  # матрица из введенных строк и столбцов. Каждый элемент матрицы - 0
# print('Для каждой мины введите строку, столбец: ')
# for i in range(n[2]):
#     print('Введите координаты мины: ', end='')
#     print(i + 1)
#     m = [(int(c) - 1) for c in input().split()]
#     a[m[0]][m[1]] = '*'  # присваиваем элементу с координатой мины значение '*'
# i = 0  # счетчик строк
# j = 0  # счетчик столбцов
# while i < n[0] and j < n[1]:
#     if a[i][j] == '*':
#         if i == n[0] - 1 and j == n[1] - 1:  # Проверяем, последний ли элемент матрицы
#             print(a)
#             exit(0)
#         elif j == n[1] - 1:  # Проверяем, последний ли элемент строки
#             i += 1
#             j = 0
#         else:
#             j += 1
#     else:
#         if i == 0 and j == 0:  # если первый элемент первой строки не равен '*'
#             if i < 1:
#                 b = a[0][:2].count('*')
#                 a[0][0] = b
#                 j += 1
#                 b, c = 0, 0
#             else:
#                 b = a[0][:2].count('*')
#                 c = a[1][:2].count('*')
#                 a[0][0] = b + c
#                 j += 1
#                 b, c = 0, 0
#         elif i == 0 and j == n[1] - 1:  # если последний элемент первой строки не равен '*'
#             b = a[0][-2:].count('*')
#             c = a[1][-2:].count('*')
#             a[0][n[1] - 1] = b + c
#             i += 1
#             j = 0
#             b, c = 0, 0
#         elif i == n[0] - 1 and j == 0:  # если первый элемент последней строки не равен '*'
#             b = a[n[0] - 1][:2].count('*')
#             c = a[n[0] - 2][:2].count('*')
#             a[n[0] - 1][0] = b + c
#             j += 1
#             b, c = 0, 0
#         elif i == n[0] - 1 and j == n[1] - 1:  # если последний элемент последней строки не равен '*'
#             b = a[n[0] - 1][-2:].count('*')
#             c = a[n[0] - 2][-2:].count('*')
#             a[n[0] - 1][n[1] - 1] = b + c
#             print(a)
#             exit(0)
#         elif i == 0 and j != 0 and j != n[1] - 1:  # если первая строка, но не первый и не последений элемент
#             b = a[0][j - 1:j + 2].count('*')
#             c = a[1][j - 1:j + 2].count('*')
#             a[0][j] = b + c
#             j += 1
#             b, c = 0, 0
#         elif i == 0 and j != 0 and j != n[1] - 1:
#             b = a[0][j - 1:j + 2].count('*')
#             c = a[1][j - 1:j + 2].count('*')
#             a[0][j] = b + c
#             j += 1
#             b, c = 0, 0
#         elif j == 0 and i != 0 and i != n[0] - 1:
#             b = a[i - 1][j:j + 2].count('*')
#             c = a[i][j:j + 2].count('*')
#             d = a[i + 1][j:j + 2].count('*')
#             a[i][j] = b + c + d
#             j += 1
#             b, c, d = 0, 0, 0
#         elif j == n[1] - 1 and i != 0 and i != n[0] - 1:
#             b = a[i - 1][-2:].count('*')
#             c = a[i][-2:].count('*')
#             d = a[i + 1][-2:].count('*')
#             a[i][j] = b + c + d
#             i += 1
#             j = 0
#             b, c, d = 0, 0, 0
#         elif i == n[0] - 1 and j != 0 and j != n[1] - 1:
#             b = a[n[0] - 1][j - 1:j + 2].count('*')
#             c = a[n[0] - 2][j - 1:j + 2].count('*')
#             a[i][j] = b + c
#             j += 1
#             b, c = 0, 0
#         else:
#             b = a[i - 1][j - 1:j + 2].count('*')
#             c = a[i][j - 1:j + 2].count('*')
#             d = a[i + 1][j - 1:j + 2].count('*')
#             a[i][j] = b + c + d
#             j += 1
#             b, c, d = 0, 0, 0
#
# print(a)

rows, columns, mines = (int(i) for i in input().split())

field = [[0 for j in range(columns)] for i in range(rows)]
# print(field)

for mine in range(mines):
    row_mine, column_mine = [int(i) for i in input().split()]
    field[row_mine - 1][column_mine - 1] = -1

for row in range(rows):
    for column in range(columns):
        if field[row][column] == 0:
            for d_row in range(-1, 2):
                for d_column in range(-1, 2):
                    i_row = row + d_row
                    j_column = column + d_column
                    if 0 <= i_row < rows and 0 <= j_column < columns and field[i_row][j_column] == -1:
                        field[row][column] += 1

for row in range(rows):
    for column in range(columns):
        if field[row][column] == -1:
            print('*', end='')
        elif field[row][column] == 0:
            print('.', end='')
        else:
            print(field[row][column], end='')
    print()