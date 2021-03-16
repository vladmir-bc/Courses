def selection_sort(mas):
    for i in range(len(mas)):
        k = i
        for j in range(i + 1, len(mas)):
            if mas[j] < mas[k]:
                k = j
        mas[i], mas[k] = mas[k], mas[i]
    return mas


mass = [2, 1, 0, 5, 4, 9, 9, 9, 0, -500, 1000000, 1.01]
print(selection_sort(mass))
