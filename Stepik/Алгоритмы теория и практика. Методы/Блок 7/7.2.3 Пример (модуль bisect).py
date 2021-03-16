import sys
from bisect import bisect_left


def find_pos(xs, query):  # query - искомый элемент
    lo = bisect_left(xs, query)  # возвращает индекс lo -
    # индекс, все элементы которого меньше искомого i < lo : xs[i] < query
    # i > lo : xs[i] >= query
    if lo < len(xs) and xs[lo] == query:
        return lo + 1  # 1 - based
    else:
        return -1


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, *xs = next(reader)  # записываем число n, а затем n элементов массива
    k, *queries = next(reader)  # записываем k и k запросов в массив
    for query in queries:  # для каждого запроса
        print(find_pos(xs, query), end=' ')  # найти его индекс в массиве и вывести

def test():
    assert find_pos([], 42) == -1
    assert find_pos([42], 42) == 1
    assert find_pos([42], 24) == -1


if __name__ == '__main__':
    main()
