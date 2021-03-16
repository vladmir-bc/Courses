import sys


def find_pos(xs, query):  # query - искомый элемент
    # Invariant: lo <= pos < hi
    lo, hi = 0, len(xs)
    while lo < hi:
        mid = (lo + hi) // 2
        if query < xs[mid]:  # сравниваем искомый элемент со средним
            hi = mid  # [lo, mid)
        elif query > xs[mid]:
            lo = mid + 1  # [mid + 1, hi)
        else:
            return mid + 1  # по условию задания индекс считается с 1
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
    test()
