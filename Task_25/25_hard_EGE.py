# *31*65? and количество делителей числа должно равнятся 2**N
from fnmatch import *


def f(n):  # подсчёт количества делителей числа
    c = 0
    for i in range(1, int(n ** 0.5)):
        if n % i == 0:
            c += 1
    c = c * 2
    if n ** 0.5 == int(n ** 0.5):
        c += 1
    return c


def g(n):  # проверка числа на соответствие 2**N
    while n % 2 == 0:
        n /= 2
    if n == 1:
        return True
    return False


for i in range(2031, 10 ** 9, 2031): # поиск подходящих под условия чисел
    if fnmatch(str(i), '*31*65?') and i % 31 == 0 and g(f(i)):
        print(i)
