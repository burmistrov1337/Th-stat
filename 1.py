# Практическое задание к лекции 1.
# 1) Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

# a) В колоде из 52 карт - 13 карт одной масти.

from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 
m=combinations(13, 4)
print(f'm = {m}')

n=combinations(52, 4)
print(f'n = {n}')

P=m/n
print(f'P(4 трефы) = {round(P,4)}')