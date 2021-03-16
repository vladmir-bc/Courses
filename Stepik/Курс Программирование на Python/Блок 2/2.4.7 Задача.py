s = input()
i = 0
a = 1
if len(s) == 1:  # когда 1 символ в строке
    print(s[i] + str(a), end='')
    exit(0)
elif min(s) == max(s):  # когда вся строка состоит из одинаковых символов
    print(s[i] + str(len(s)), end='')
    exit(0)
while i + 1 < len(s):  # остальные случаи
    a = 1
    if (s[i] != s[i + 1]) and (i + 1 < len(s)):  # если число не равно следующему, выводим его
        print(s[i] + str(a), end='')
        i += 1
        continue
    while (i + 1 < len(s)) and s[i] == s[i + 1]:  # пока число равно следующему, накручиваем
        a += 1
        i += 1
    print(s[i] + str(a), end='')
    i += 1
if s[-1] != s[-2]:
    print(s[i] + str(a), end='')