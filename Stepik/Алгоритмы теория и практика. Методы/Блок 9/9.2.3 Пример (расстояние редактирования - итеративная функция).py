import random


def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    d = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, d[i - 1][j - 1] + (s1[i - 1] != s2[j - 1]))
    return d[m][n]


def main():
    s1 = input()
    s2 = input()
    print(edit_distance(s1, s2))


def test(n_iter=100):
    for i in range(n_iter):
        length = random.randint(0, 64)
        s = "".join(random.choice("01") for _ in range(length))

        assert edit_distance(s, "") == edit_distance("", s) == len(s)
        assert edit_distance(s, s) == 0
    assert edit_distance("ab", "ab") == 0
    assert edit_distance("short", "ports") == 3
    # short-
    # p-orts


if __name__ == '__main__':
    test()
