import itertools


def primes():
    element = 2
    while True:
        count = 0
        for el in range(1, element + 1):
            if element % el == 0:
                count += 1
        if count == 2:
            yield element
        element += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
