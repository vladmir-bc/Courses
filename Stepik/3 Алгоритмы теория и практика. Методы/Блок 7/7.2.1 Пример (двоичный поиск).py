import sys


def find_pos(xs, query):
    try:
        return xs.index(query) + 1  # index возвращает индекс элемента, начиная с нуля.
    # Т.к. по условию нумирация происходит с 1, добавляем 1
    except ValueError:
        return -1


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, *xs = next(reader)  # записываем число n, а затем n элементов массива
    k, *queries = next(reader)  # записываем k и k запросов в массив
    for query in queries:  # для каждого запроса
        print(find_pos(xs, query), end=' ')  # найти его индекс в массиве и вывести


if __name__ == '__main__':
    main()
