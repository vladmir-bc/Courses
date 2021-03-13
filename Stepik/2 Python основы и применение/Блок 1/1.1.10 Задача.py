number_of_strings = int(input('Введите количество чисел: '))
counter = 0 # Счетчик суммы введенных чисел
for number in range(number_of_strings):
    counter += int(input('Введите число: '))
print('Сумма введенных Вами чисел равна:', counter)