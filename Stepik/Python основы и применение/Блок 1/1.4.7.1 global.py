ok_status = True
vowels = ['a', 'u', 'i', 'e', 'o']


def check(word):
    global ok_status  # Обращение к глобальной перменной
    for vowel in vowels:
        if vowel in word:
            return True  # Как только встречается гласная, возвращает True
        ok_status = False  # Если гласных нет, изменяет статус глобальной переменной
        return False  # Если гласных нет, возвращает False


print(check('abacaba'))
print(ok_status)
print(check('www'))
print(ok_status)
