import random
import sys
from functools import lru_cache


def edit_distance(s1, s2):
    @lru_cache(maxsize=None)
    def d(i, j):  # i, j - длины двух строк, для которых считаем редакционные растояния
        if i == 0 or j == 0:
            return max(i, j)  # если i или j = 0, то расстояние редактирвоания - максимум из i, j
        else:
            return min(d(i, j - 1) + 1,  # вставка и штрафуем на 1
                       d(i - 1, j) + 1,  # удаление и штрафуем на 1
                       d(i - 1, j - 1) + (s1[i - 1] != s2[j - 1]))  # замена, несоответствие

    return d(len(s1), len(s2))


def main():
    s1 = input()
    s2 = input()
    print(edit_distance(s1, s2))


def test(n_iter=100):
    for i in range(n_iter):
        length = random.randint(0, 1000)
        s = "".join(random.choice("01") for _ in range(length))

        assert edit_distance(s, "") == edit_distance("", s) == len(s)
        assert edit_distance(s, s) == 0
    assert edit_distance("ab", "ab") == 0
    assert edit_distance("short", "ports") == 3
    # short-
    # p-orts


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    test()
