with open('dataset_24465_4.txt') as rd, open('dataset_answer1.txt', 'w') as wr:
    a = []
    for line in rd:
        if '\n' not in line:
            a.append(line + '\n')
            continue
        a.append(line)
    a = a[::-1]
    for line in a:
        wr.write(line)