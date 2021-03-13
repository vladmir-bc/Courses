from exceptions import BadName as bad, greet as exc_greet
import exceptions as exc
from exceptions import *
print(exc)
print(bad)


def greet():
    print('Greetings')


# print(BadName)
# print(greet)

print(exc_greet('Volodya'))
