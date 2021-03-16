with open('test.txt') as f, open('test_copy.txt', 'w') as w:  # Файл будет закрыт в любом случае, метод .close не нужен
    for line in f:
        w.write(line)