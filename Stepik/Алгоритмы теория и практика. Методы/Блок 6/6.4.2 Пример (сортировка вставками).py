def insertion_sort(mas):
    for i in range(1, len(mas)):
        j = i
        while j > 0 and mas[j] < mas[j - 1]:
            mas[j], mas[j - 1] = mas[j - 1], mas[j]
            j = j - 1
    return mas


a = [10, 6]
print(insertion_sort(a))
