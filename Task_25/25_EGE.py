# 1?2139*4 and число//2023

# Вариант 1
for i in range(1021615, 1921399994, 2023):
    n = str(i)
    if n[:1] == '1' and n[2:6] == '2139' and n[-1] == '4':
        print(i)

# Вариант 2
star = ['']
for i in range(10):
    star.append(str(i))
for i in range(10, 100):
    star.append(str(i))
for i in range(100, 1000):
    star.append(str(i))
for i in range(10):
    for j in star:
        a = '1' + str(i) + '2139' + j + '4'
        if int(a) % 2023 == 0:
            print(a)

# Вариант 3
from fnmatch import *

for i in range(2023, 10 ** 10, 2023):
    if fnmatch(str(i), "1?2139*4"):
        print(i)
