from functools import lru_cache

@lru_cache(maxsize=None) # ИЛИ также можно заменить эту строчку на @lru_cache(maxsize=None)
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

print(fib1(80))