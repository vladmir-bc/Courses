import datetime

date1 = [int(i) for i in input().split()]
first_date = datetime.date(date1[0], date1[1], date1[2])
number_of_days = datetime.timedelta(int(input()))
second_date = first_date + number_of_days
print(second_date.year, second_date.month, second_date.day)

'''Решение преподавателя:

import datetime

y, m, d = map(int, input().split())
days = int(input())

current = datetime.date(year=y, month=m, day=d)
current += datetime.timedelta(days=days)

print("{} {} {}".format(current.year, current.month, current.day))'''