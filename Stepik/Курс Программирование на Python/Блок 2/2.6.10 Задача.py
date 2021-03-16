list_1 = [input().split()]
while ['end'] not in list_1:
    row = (input().split())
    list_1 += [row]
list_1.remove(['end'])
for row in range(len(list_1)):
    for column in range(len(list_1[0])):
        list_1[row][column] = int(list_1[row][column])

for row in range(len(list_1)):
    for column in range(len(list_1[0])):
        if row < (len(list_1) - 1) and column < (len(list_1[0]) - 1):
            print(list_1[row][column + 1] + list_1[row][column - 1] + list_1[row - 1][column] + list_1[row + 1][column],
                  end=' ')
        elif row == len(list_1) - 1 and column < (len(list_1[0]) - 1):
            print(
                list_1[row][column + 1] + list_1[row][column - 1] + list_1[row - 1][column] + list_1[-row - 1][column],
                end=' ')
        elif row < (len(list_1) - 1) and column == (len(list_1[0]) - 1):
            print(
                list_1[row][-column - 1] + list_1[row][column - 1] + list_1[row - 1][column] + list_1[row + 1][column],
                end=' ')
        else:
            print(
                list_1[row][-column - 1] + list_1[row][column - 1] + list_1[row - 1][column] + list_1[-row - 1][column],
                end=' ')
    print()
