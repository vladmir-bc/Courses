import random


def quick_sort(mas, l, r):
    def partition(mas, l, r):
        f = random.randint(l, r - 1)
        mas[f], mas[r - 1] = mas[r - 1], mas[f]
        j = l
        counter = 0
        repeats = []
        for i in range(l, r - 1):
            if mas[i] == mas[r - 1]:
                mas[i], mas[j] = mas[j], mas[i]
                j += 1
                counter += 1
            elif mas[i] < mas[r - 1]:
                cntr = i
                try:
                    while (mas[cntr] < mas[cntr - 1]) and (mas[cntr - 1] == mas[r - 1]) and cntr > 0:
                        mas[cntr], mas[cntr - 1] = mas[cntr - 1], mas[cntr]
                        cntr -= 1
                except:
                    None
                mas[i], mas[j] = mas[j], mas[i]
                j += 1
        if counter > 0:
            for repeat in range(l, r - 1):
                if mas[repeat] == mas[r - 1]:
                    repeats.append(repeat)
        mas[r - 1], mas[j] = mas[j], mas[r - 1]
        counter2 = 1
        for el in repeats[::-1]:
            mas[j - counter2], mas[el] = mas[el], mas[j - counter2]
            counter2 += 1
        return j - counter, j

    while l < r:
        m = partition(mas, l, r)
        quick_sort(mas, l, m[0])
        l = m[1] + 1
    return mas


mass = [random.randint(-1, 1) for i in range(5000)]
l = 0
r = len(mass)
print(quick_sort(mass, l, r))

#Проверка:
# for el in range(len(mass)):
#     if el < len(mass) - 1:
#         try:
#             assert mass[el] <= mass[el + 1]
#         except:
#             print(el)
